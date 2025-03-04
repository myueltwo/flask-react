import { IGroup, IRole } from "shared/types";

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

export interface IResetPassword {
    new_password?: string;
    repeat_password?: string;
}

export interface ILoginResponse {
    access_token: string;
}
