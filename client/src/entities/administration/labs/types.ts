import {IItemWidget} from "shared/types";

export interface ILabRequest {
    datetime: string,
    deadline: string,
    id: string;
    name: string;
    subject_id: string;
}

export interface ILab extends ILabRequest {
    subject: IItemWidget;
}