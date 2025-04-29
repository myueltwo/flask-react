import React, {useEffect, useState} from "react";
import {Form} from "react-bootstrap";
import {NAME, NUMBER_OF_HOURS} from "shared/constants";
import {FormModal, IChangingForm} from "entities/administration";
import {CustomFetchBaseQueryError} from "shared/types";
import { ISubjectRequest, ISubjectEditRequest } from "../../types";
import {ErrorNotification} from "shared/ui";

export const ChangingForm: React.FC<IChangingForm<ISubjectRequest | ISubjectEditRequest>> = ({show, onHide, isError, error, onSave, isUpdating, data, isAdding}) => {
    const [name, setName] = useState("");
    const [numberHours, setNumberHours] = useState<undefined | number>();
    const [validated, setValidated] = useState(false);

    useEffect(() => {
        if (data) {
            setName(data.name);
            setNumberHours(data.numberHours);
        }
    }, [data]);
    const handleClose = () => {
        onHide();
        setName("");
        setNumberHours(undefined);
        setValidated(false);
    };
    const handleSave = () => {
        if (name && numberHours !== undefined) {
            const params = {
                ...data,
                name,
                numberHours,
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
                    <Form.Group className="mb-3" controlId="subjectForm.number_of_hours">
                        <Form.Label>{NUMBER_OF_HOURS}</Form.Label>
                        <Form.Control
                            type="number"
                            placeholder="Enter number of hours"
                            value={numberHours}
                            onChange={(event) => setNumberHours(event.target.value ? parseInt(event.target.value, 10) : undefined)}
                            required
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