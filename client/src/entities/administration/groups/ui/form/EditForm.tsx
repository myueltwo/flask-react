import React from "react";
import { useGetGroupQuery, useEditGroupMutation } from "../../model";
import { IItemRequest } from "shared/types";
import {IEditForm} from "entities/administration";
import {ChangingForm} from "shared/ui";

export const EditForm: React.FC<IEditForm> = ({ itemId, ...rest }) => {
    const { data, isError, error } = useGetGroupQuery(itemId);
    const [editPost, {isError: isErrorEdit, error: errorEdit, isLoading: isUpdating}] = useEditGroupMutation();
    const props = {
        data,
        onSave: (params: IItemRequest) => editPost({id: itemId, ...params}),
        isError: isError || isErrorEdit,
        error: error || errorEdit,
        isUpdating,
        ...rest,
    }

    return (
        <ChangingForm {...props}/>
    );
};