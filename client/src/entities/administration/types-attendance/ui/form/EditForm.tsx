import React from "react";
import { useGetAttendanceTypeQuery, useEditAttendanceTypeMutation } from "../../model";
import { IItemRequest } from "shared/types";
import {IEditForm} from "entities/administration";
import {ChangingForm} from "shared/ui";

export const EditForm: React.FC<IEditForm> = ({ itemId, ...rest }) => {
    const { data, isError, error } = useGetAttendanceTypeQuery(itemId);
    const [editPost, {isError: isErrorEdit, error: errorEdit, isLoading: isUpdating}] = useEditAttendanceTypeMutation();
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