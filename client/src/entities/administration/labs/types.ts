export interface ILabRequest {
    datetime: Date,
    deadline: Date,
    id: string;
    name: string;
    subject_id: string;
}

export interface ILab extends ILabRequest {
    subject: {
        id: string;
        name: string;
    }
}