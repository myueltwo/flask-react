import axios from "axios";
import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'
import { RootState } from "app/store";
import { setAuthToken, getAuthToken } from "shared/config";
import { ILogin, IAuthTokenState } from "../types";

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

const initialState: IAuthTokenState = {
  value: getAuthToken(),
  status: 'idle',
  error: null,
};

export const authTokenSlice = createSlice({
  name: 'authToken',
  initialState,
  reducers: {

  },
  extraReducers(builder) {
    builder
      .addCase(fetchLogin.pending, (state, action) => {
        state.status = 'loading';
        state.value = "";
        setAuthToken();
      })
      .addCase(fetchLogin.fulfilled, (state, action) => {
        state.status = 'succeeded';
        const { access_token } = action.payload;
        const token = `Bearer ${access_token}`
        state.value = token;
        setAuthToken(token);
      })
      .addCase(fetchLogin.rejected, (state, action) => {
        state.status = 'failed';
        state.error = action.error.message;
      })
      .addCase(fetchLogout.pending, (state, action) => {
        state.value = "";
        setAuthToken();
      })
  }
});

export const selectAuthToken = (state: RootState) => state.authToken.value;
export const selectAuthError = (state: RootState) => state.authToken.error;

export const authTokenReducer = authTokenSlice.reducer;