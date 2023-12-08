import { Status } from "shared/types";

export interface ILogin {
    login: string;
    password: string;
}

export interface IUser {
    id:	string;
    login: string;
    name?: string;
    password: string;
    patronymic:	string;
    surname: string;
    token_expires_in: string;
}

export interface IAuthTokenState {
    value: string;
    status: Status;
    error?: string | null;
}