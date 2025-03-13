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