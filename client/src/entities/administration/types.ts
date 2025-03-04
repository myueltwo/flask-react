import {CustomFetchBaseQueryError, ObjectList} from "shared/types";

export interface ISubject {
    count_hours: number;
    link?: string;
    name: string;
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
}