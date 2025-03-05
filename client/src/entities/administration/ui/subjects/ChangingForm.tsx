import React, {useState} from "react";
import {Form} from "react-bootstrap";
import {NAME, NUMBER_OF_HOURS} from "shared/constants";
import {FormModal} from "../Form";
import {IChangingForm} from "../../types";
import {useAddSubjectMutation} from "../../model";

export const ChangingForm: React.FC<IChangingForm> = ({isAdding, show, onHide}) => {
    const [addPost, { isLoading: isUpdating }] = useAddSubjectMutation();

    const [name, setName] = useState("");
    const [validated, setValidated] = useState(false);
    const [numberHours, setNumberHours] = useState<undefined | number>();
    const handleClose = () => {
        onHide();
        setName("");
        setNumberHours(undefined);
        setValidated(false);
    };
    const handleSave = () => {
        if (name && numberHours !== undefined) {
            addPost({name, numberHours})
                .unwrap()
                .finally(handleClose);
        } else {
            setValidated(true);
        }
    }
    return (
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
    );
}