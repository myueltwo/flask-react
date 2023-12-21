import axios from "axios";
import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'
import { RootState } from "app/store";
import { setAuthToken } from "shared/config";
import { IUserState } from "../types";

export const fetchUser = createAsyncThunk(
    "currentUser/fetchUser",
    async() => {
        const response = await axios.get('/auth/user');
      return response.data;
    }
);

const initialState: IUserState = {
  data: null,
  status: 'idle',
  error: null,
};

export const currentUserSlice = createSlice({
  name: 'currentUser',
  initialState,
  reducers: {},
  extraReducers(builder) {
    builder
      .addCase(fetchUser.pending, (state, action) => {
        state.status = 'loading'
      })
      .addCase(fetchUser.fulfilled, (state, action) => {
        state.status = 'succeeded';
        state.data = action.payload;
      })
      .addCase(fetchUser.rejected, (state, action) => {
        setAuthToken();
        state.status = 'failed';
        state.data = null;
        state.error = action.error.message;
      })
  }
});

export const selectCurrentUser = (state: RootState) => state.currentUser.data;
export const selectCurrentUserPending = (state: RootState) => state.currentUser.status;
export const selectCurrentUserError = (state: RootState) => state.currentUser.error;

export const currentUserReducer = currentUserSlice.reducer;