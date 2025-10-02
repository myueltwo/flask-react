import React from "react";
import { useAddAttendanceTypeMutation } from "../../model";
import {IAddForm} from "entities/administration";
import {ChangingForm} from "shared/ui";

export const AddForm: React.FC<IAddForm> = ({ ...rest }) => {
    const [addWidget, { isLoading: isUpdating, isError, error }] = useAddAttendanceTypeMutation();
    const props = {
        onSave: addWidget,
        isAdding: true,
        ...rest,
        isError,
        error,
        isUpdating,
    }

    return (
        <ChangingForm {...props}/>
    );
};