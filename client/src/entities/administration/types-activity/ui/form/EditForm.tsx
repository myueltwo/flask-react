import React from "react";
import { useGetActivityTypeQuery, useEditActivityTypeMutation } from "../../model";
import { IItemRequest } from "shared/types";
import {IEditForm} from "entities/administration";
import {ChangingForm} from "shared/ui";

export const EditForm: React.FC<IEditForm> = ({ itemId, ...rest }) => {
    const { data, isError, error } = useGetActivityTypeQuery(itemId);
    const [editPost, {isError: isErrorEdit, error: errorEdit, isLoading: isUpdating}] = useEditActivityTypeMutation();
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