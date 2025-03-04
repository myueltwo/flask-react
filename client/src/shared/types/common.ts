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

export type ObjectList<T = string> = {
    [key: string]: T;
}

export interface IPageProps {
    page: number;
    per_page?: number;
}

export interface ListResponse<T> {
    has_next: boolean;
    has_prev: boolean;
    items: T[];
    items_per_page: number;
    page: number;
    total_items: number;
    total_pages: number;
}