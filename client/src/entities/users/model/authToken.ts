import axios from "axios";
import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'
import { RootState } from "app/store";
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
  value: "",
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
        state.status = 'loading'
      })
      .addCase(fetchLogin.fulfilled, (state, action) => {
        state.status = 'succeeded';
        const { access_token } = action.payload;
        state.value = `Bearer ${access_token}`;
      })
      .addCase(fetchLogin.rejected, (state, action) => {
        state.status = 'failed';
        state.value = "";
        state.error = action.error.message;
      })
      .addCase(fetchLogout.pending, (state, action) => {
        state.value = "";
      })
  }
});

export const selectAuthToken = (state: RootState) => state.authToken.value;
export const selectAuthError = (state: RootState) => state.authToken.error;

export const authTokenReducer = authTokenSlice.reducer;