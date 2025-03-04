import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";
import type {
  BaseQueryFn,
  FetchArgs,
  FetchBaseQueryError,
} from '@reduxjs/toolkit/query';
import {ILogin, ILoginResponse, IResetPassword, IUser, IUserInside} from "shared/types";
import { getAuthToken, setAuthToken } from "../shared";
import { buildFullName } from "shared/libs";

const baseQuery = fetchBaseQuery({
    baseUrl: 'http://127.0.0.1:5000/api/v1',
    prepareHeaders: (headers) => {
        const token = getAuthToken();

        // If we have a token set in state, let's assume that we should be passing it.
        if (token) {
            headers.set('authorization', `Bearer ${token}`)
        }
    }
});
const baseQueryWithAuthTokenExpired: BaseQueryFn<
    string | FetchArgs,
    unknown,
    FetchBaseQueryError
> = async (args, api, extraOptions) => {
    let result = await baseQuery(args, api, extraOptions)
  if (result.error && result.error.status === 401) {
    // try to remove token
    setAuthToken();
  }
  return result;
};

export const api = createApi({
    baseQuery: baseQueryWithAuthTokenExpired,
    reducerPath: 'userApi',
    tagTypes: ["UNAUTHORIZED"],
    endpoints: (build) =>  ({
        login: build.mutation<string, ILogin>({
            query: (body) => ({
                url: '/auth/login',
                method: 'POST',
                body,
            }),
            invalidatesTags: (result) => (result ? ['UNAUTHORIZED'] : []),
            transformResponse: (response: ILoginResponse) => {
                const token = response.access_token;
                setAuthToken(token);
                return token;
            },
        }),
        resetPassword: build.mutation<string, IResetPassword>({
            query: (body) => ({
                url: "/auth/reset_password",
                method: "POST",
                body,
            }),
        }),
        logout: build.mutation<void, void>({
            query: () => ({
                url: "/auth/logout",
                method: "POST",
            }),
        }),
        getCurrentUser: build.query<IUserInside, void>({
            query: () => ({url: "/auth/user"}),
            transformResponse: (user: IUser) => ({
                ...user,
                fullName: buildFullName(user),
            }),
        })
    }),
});

export const { useLoginMutation, useLogoutMutation, useGetCurrentUserQuery, useResetPasswordMutation } = api;