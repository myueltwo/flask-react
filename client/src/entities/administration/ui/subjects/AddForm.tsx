import React from "react";
import { useAddSubjectMutation } from "../../model";
import {IAddForm} from "../../types";
import {ChangingForm} from "./ChangingForm";

export const AddForm: React.FC<IAddForm> = ({ ...rest }) => {
    const [addPost, { isLoading: isUpdating, isError, error }] = useAddSubjectMutation();
    const props = {
        onSave: addPost,
        ...rest,
        isError,
        error,
        isUpdating,
    }

    return (
        <ChangingForm {...props}/>
    );
};