import {IPaginationProps} from "shared/ui";
import {FetchBaseQueryError} from "@reduxjs/toolkit/query";
import {SerializedError} from "@reduxjs/toolkit";
import {CustomFetchBaseQueryError, ObjectList} from "../../types";

export interface IWidgetListProps<T = any> {
    data: T;
    isLoading: boolean;
    isError: boolean;
    error: CustomFetchBaseQueryError;
    deleteItem: (id: string) => void;
    page: number;
    setPage: (page: number) => void;
    setItemId: (id: string) => void;
    setShow: (show: boolean) => void;
}


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

export interface IChangingForm<T, N = T> extends IAddForm {
    data?: T;
    onSave: (data: N) => { unwrap(): Promise<any> };
    isError?: boolean;
    error?: FetchBaseQueryError | SerializedError | undefined;
    isUpdating: boolean;
    isAdding?: boolean;
}

export interface IEditForm extends IAddForm {
    itemId: string;
}

export interface IActions {
    itemId: string;
    onEdit: (itemId: string) => void;
    onRemove: (itemId: string) => void;
}