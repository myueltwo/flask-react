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

export interface IPaginationProps {
    has_next: boolean;
    has_prev: boolean;
    page: number;
    total_pages: number;
}

export interface ListResponse<T> extends IPaginationProps {
    items: T[];
    total_items: number;
    items_per_page: number;
}

export interface IAddItemResponse {
    message: string;
    status: string;
    widget_id: string;
}

export interface IItemRequest {
    name: string;
}

export interface IItemEditRequest extends IItemRequest {
    id: string;
}

export interface IItemWidget extends IItemEditRequest {}