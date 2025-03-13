import {CustomFetchBaseQueryError, ObjectList} from "shared/types";
import {IPaginationProps} from "shared/ui";
import {FetchBaseQueryError} from "@reduxjs/toolkit/query";
import {SerializedError} from "@reduxjs/toolkit";

export interface ITableInfoProps {
    fields?: ObjectList[];
    isLoading: boolean;
    isError?: boolean;
    error?: CustomFetchBaseQueryError;
    onAddItem: () => void;
    pagination?: IPaginationProps;
}

export interface IModalForm {
    show: boolean;
    onHide: () => void;
    isAdding?: boolean;
    onSave: () => void;
    isUpdating: boolean;
}

export interface IAddForm {
    show: boolean;
    onHide: () => void;
}

export interface IChangingForm<T> extends IAddForm {
    data?: T;
    onSave: (data: T) => { unwrap(): Promise<any> };
    isError?: boolean;
    error?: FetchBaseQueryError | SerializedError | undefined;
    isUpdating: boolean;
    isAdding?: boolean;
}

export interface IEditForm extends IAddForm {
    itemId: string;
}