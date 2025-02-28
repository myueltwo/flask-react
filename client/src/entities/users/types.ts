import { Status, IGroup, IRole } from "shared/types";

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
    group?: IGroup;
    role: IRole;
}

export interface IUserInside extends  IUser {
    fullName?: string;
}

export interface IAuthTokenState {
    value: string;
    status: Status;
    error?: string | null;
}

export interface IUserState {
    data: IUserInside | null;
    status: Status;
    error?: string | null;
}

export interface IResetPassword {
    new_password?: string;
    repeat_password?: string;
}

export interface ILoginResponse {
    access_token: string;
}
