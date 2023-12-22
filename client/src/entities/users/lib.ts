import {IUser} from "./types";

export const buildFullName = ({name, surname, patronymic}: IUser) => {
    return [surname, name, patronymic].filter(Boolean).join(" ");
}