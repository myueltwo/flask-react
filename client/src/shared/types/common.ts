import { FetchBaseQueryError } from "@reduxjs/toolkit/query";

export type Status = 'idle' | 'loading' | 'failed' | 'succeeded';

export interface IError {
    message: string;
}

export type CustomFetchBaseQueryError = FetchBaseQueryError & {
    data: {
        message: string;
    }
};
