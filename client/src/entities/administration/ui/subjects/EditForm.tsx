import React from "react";
import { useGetSubjectQuery, useEditSubjectMutation } from "../../model";
import {IEditForm, ISubjectRequest} from "../../types";
import {ChangingForm} from "./ChangingForm";

export const EditForm: React.FC<IEditForm> = ({ itemId, ...rest }) => {
    const { data, isError, error } = useGetSubjectQuery(itemId);
    const [editPost, {isError: isErrorEdit, error: errorEdit, isLoading: isUpdating}] = useEditSubjectMutation();
    const props = {
        ...(data ? {data: {name: data.name, numberHours: data.count_hours}} : {}),
        onSave: (params: ISubjectRequest) => editPost({id: itemId, ...params}),
        isError: isError || isErrorEdit,
        error: error || errorEdit,
        isUpdating,
        ...rest,
    }

    return (
        <ChangingForm {...props}/>
    );
};