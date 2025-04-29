import React from "react";
import { useAddLabMutation } from "../../model";
import {IAddForm} from "entities/administration";
import {ChangingForm} from "./ChangingForm";

export const AddForm: React.FC<IAddForm> = ({ ...rest }) => {
    const [addItem, { isLoading: isUpdating, isError, error }] = useAddLabMutation();
    const props = {
        onSave: addItem,
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