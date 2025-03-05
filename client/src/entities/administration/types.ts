import {CustomFetchBaseQueryError, ObjectList} from "shared/types";
import {ChangingForm} from "./ui/subjects/ChangingForm";

export interface ISubject {
    count_hours: number;
    link?: string;
    name: string;
}

export interface ISubjectRequest {
    name: string;
    numberHours: number;
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

export interface IChangingForm extends Omit<IModalForm, "onSave" | "isUpdating"> {}