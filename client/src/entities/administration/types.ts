import {CustomFetchBaseQueryError, ObjectList} from "shared/types";
import {FetchBaseQueryError} from "@reduxjs/toolkit/query";
import {SerializedError} from "@reduxjs/toolkit";

export interface ISubject {
    count_hours: number;
    link?: string;
    name: string;
    id: string;
}

export interface ISubjectRequest {
    name: string;
    numberHours: number;
}

export interface ISubjectEditRequest extends ISubjectRequest {
    id: string;
}

export interface ITableInfoProps {
    fields?: ObjectList[];
    isLoading: boolean;
    isError?: boolean;
    error?: CustomFetchBaseQueryError;
    onAddItem: () => void;
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

export interface IChangingForm extends IAddForm {
    data?: ISubjectRequest;
    onSave: (data: ISubjectEditRequest | ISubjectRequest) => { unwrap(): Promise<any> };
    isError?: boolean;
    error?: FetchBaseQueryError | SerializedError | undefined;
    isUpdating: boolean;
    isAdding?: boolean;
}

export interface IEditForm extends IAddForm {
    itemId: string;
}