import React from "react";
import { useGetLabQuery, useEditLabMutation } from "../../model";
import {ILabRequest} from "../../types";
import {IEditForm} from "entities/administration";
import {ChangingForm} from "./ChangingForm";

export const EditForm: React.FC<IEditForm> = ({ itemId, ...rest }) => {
    const { data, isError, error } = useGetLabQuery(itemId);
    const [editItem, {isError: isErrorEdit, error: errorEdit, isLoading: isUpdating}] = useEditLabMutation();
    const props = {
        data,
        onSave: (params: Omit<ILabRequest, "id">) => editItem({id: itemId, ...params}),
        isError: isError || isErrorEdit,
        error: error || errorEdit,
        isUpdating,
        ...rest,
    }

    return (
        <ChangingForm {...props}/>
    );
};