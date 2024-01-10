import axios, {AxiosError} from "axios";
import {createSlice, createAsyncThunk, PayloadAction} from '@reduxjs/toolkit'
import { RootState } from "app/store";
import { setAuthToken, getAuthToken } from "shared/config";
import {IError} from "shared/types";
import {ILogin, IAuthTokenState, IResetPassword} from "../types";
import { fetchUser } from "./user";

export const fetchLogin = createAsyncThunk(
    'authToken/fetchLogin',
    async (data: ILogin) => {
      const response = await axios.post('/auth/login', data);
      return response.data;
    });

export const fetchLogout = createAsyncThunk(
    'authToken/fetchLogout',
    async () => {
      const response = await axios.post('/auth/logout');
      return response.data;
    });

export const fetchResetPassword = createAsyncThunk(
    "auth/fetchResetPassword",
    async (data: IResetPassword, { rejectWithValue }) => {
        try {
            const response = await axios.post('/auth/reset_password', data);
            return response.data;
        } catch (error) {
            return rejectWithValue({ message: (error as AxiosError<IError>).response?.data.message  });
        }
    }
);

const initialState: IAuthTokenState = {
  value: getAuthToken(),
  status: 'idle',
  error: null,
};

const updateAuthToken = (state: IAuthTokenState, action: PayloadAction<any, string, { arg: ILogin | IResetPassword }>) => {
    state.status = 'succeeded';
    const {access_token} = action.payload;
    const token = `Bearer ${access_token}`
    setAuthToken(token);
    state.value = token;
};

export const authTokenSlice = createSlice({
    name: 'authToken',
    initialState,
    reducers: {},
    extraReducers(builder) {
        builder
            .addCase(fetchLogin.pending, (state, action) => {
                state.status = 'loading';
                state.value = "";
                setAuthToken();
            })
            .addCase(fetchLogin.fulfilled, updateAuthToken)
            .addCase(fetchResetPassword.fulfilled, updateAuthToken)
            .addCase(fetchLogin.rejected, (state, action) => {
                state.status = 'failed';
                state.error = action.error.message;
            })
            .addCase(fetchLogout.pending, (state, action) => {
                state.value = "";
                setAuthToken();
            })
            .addCase(fetchUser.rejected, (state, action) => {
                state.value = "";
                setAuthToken();
            })
    }
});

export const selectAuthToken = (state: RootState) => state.authToken.value;
export const selectAuthError = (state: RootState) => state.authToken.error;

export const authTokenReducer = authTokenSlice.reducer;