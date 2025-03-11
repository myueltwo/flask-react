import React, {useEffect, useState} from "react";
import {Form, Toast, ToastContainer} from "react-bootstrap";
import {NAME, NUMBER_OF_HOURS, SOMETHING_WRONG} from "shared/constants";
import {FormModal} from "../Form";
import {IChangingForm} from "../../types";
import {CustomFetchBaseQueryError} from "shared/types";

export const ChangingForm: React.FC<IChangingForm> = ({show, onHide, isError, error, onSave, isUpdating, data, isAdding}) => {
    const [name, setName] = useState("");
    const [numberHours, setNumberHours] = useState<undefined | number>(data?.numberHours);
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
                <ToastContainer position="top-end" className="p-3" style={{zIndex: 1}}>
                    <Toast delay={3000} bg="danger" autohide>
                        <Toast.Header>
                            <strong className="me-auto">Error</strong>
                        </Toast.Header>
                        <Toast.Body className="text-white">{(error as CustomFetchBaseQueryError)?.data?.message || SOMETHING_WRONG}</Toast.Body>
                    </Toast>
                </ToastContainer>
            )}
        </>
    );
}