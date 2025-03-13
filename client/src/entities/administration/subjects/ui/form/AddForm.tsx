import React from "react";
import { useAddSubjectMutation } from "../../model";
import {IAddForm} from "entities/administration";
import {ChangingForm} from "./ChangingForm";

export const AddForm: React.FC<IAddForm> = ({ ...rest }) => {
    const [addPost, { isLoading: isUpdating, isError, error }] = useAddSubjectMutation();
    const props = {
        onSave: addPost,
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