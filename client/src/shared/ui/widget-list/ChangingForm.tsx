import React, {useEffect, useState} from "react";
import {Form} from "react-bootstrap";
import {NAME} from "shared/constants";
import {CustomFetchBaseQueryError, IItemRequest, IItemEditRequest} from "shared/types";
import {ErrorNotification} from "shared/ui";
import {FormModal} from "./Form";
import { IChangingForm } from "./types";

export const ChangingForm: React.FC<IChangingForm<IItemRequest | IItemEditRequest>> = ({show, onHide, isError, error, onSave, isUpdating, data, isAdding}) => {
    const [name, setName] = useState("");
    const [validated, setValidated] = useState(false);

    useEffect(() => {
        if (data) {
            setName(data.name);
        }
    }, [data]);
    const handleClose = () => {
        onHide();
        setName("");
        setValidated(false);
    };
    const handleSave = () => {
        if (name) {
            const params = {
                ...data,
                name,
            };
            onSave(params)
                .unwrap()
                .finally(handleClose);
        } else {
            setValidated(true);
        }
    }
    return (
        <>
            <FormModal show={show} onHide={handleClose} isAdding={isAdding} onSave={handleSave} isUpdating={isUpdating}>
                <Form validated={validated}>
                    <Form.Group className="mb-3" controlId="subjectForm.name">
                        <Form.Label>{NAME}</Form.Label>
                        <Form.Control
                            type="text"
                            placeholder="Enter name"
                            value={name}
                            onChange={(event) => setName(event.target.value)}
                            required
                            autoFocus
                        />
                    </Form.Group>
                </Form>
            </FormModal>
            {isError && (
                <ErrorNotification error={error as CustomFetchBaseQueryError}/>
            )}
        </>
    );
}