import React, {useEffect, useState} from "react";
import {Form} from "react-bootstrap";
import {NAME} from "shared/constants";
import {FormModal, useGetSubjectsQuery} from "entities/administration";
import {CustomFetchBaseQueryError} from "shared/types";
import {IChangingFormLab} from "./types";
import {Messages} from "shared/messages";
import {ErrorNotification, Combobox, IItem} from "shared/ui";

export const ChangingForm: React.FC<IChangingFormLab> = ({show, onHide, isError, error, onSave, isUpdating, data, isAdding}) => {
    const [name, setName] = useState("");
    const [subject, setSubject] = useState<undefined | IItem>();
    const [date, setDate] = useState<undefined | Date>();
    const [deadline, setDeadline] = useState<undefined | Date>();
    const [validated, setValidated] = useState(false);
    const { data: dataSubjects, isLoading, isError: isErrorSubject } = useGetSubjectsQuery({per_page: 100});
    const subjects = dataSubjects?.items.map(({id, name}) => ({
        key: id,
        value: name,
    })) || [];

    useEffect(() => {
        if (data) {
            setName(data.name);
            setSubject(data.subject_id);
            setDate(data.datetime);
            setDeadline(data.deadline);
        }
    }, [data]);
    const handleClose = () => {
        onHide();
        setName("");
        setSubject(undefined);
        setDate(undefined);
        setDeadline(undefined);
        setValidated(false);
    };
    const handleSave = () => {
        if ([name, subject, date, deadline].every(Boolean)) {
            const deadlineDate = new Date(deadline);
            deadlineDate.setHours(23, 59, 59)
            const params = {
                ...data,
                name,
                subject_id: subject.key,
                datetime: new Date(date).toISOString(),
                deadline: deadlineDate.toISOString(),
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
                    <Form.Group className="mb-3" controlId="labForm.name">
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
                    <Form.Group className="mb-3" controlId="labForm.subject">
                        <Form.Label>{Messages.subject}</Form.Label>
                        <Combobox items={subjects} onChange={setSubject} selectedItem={subject} isLoading={isLoading} isError={isErrorSubject}/>
                    </Form.Group>
                    <Form.Group className="mb-3" controlId="labForm.date">
                        <Form.Label>{Messages.date}</Form.Label>
                        <Form.Control
                            type="date"
                            placeholder="Enter date of lab"
                            value={date}
                            onChange={(event) => setDate(event.target.value)}
                            required
                        />
                    </Form.Group>
                    <Form.Group className="mb-3" controlId="labForm.deadline">
                        <Form.Label>{Messages.labs.deadline}</Form.Label>
                        <Form.Control
                            type="date"
                            placeholder="Enter date of deadline"
                            value={deadline}
                            onChange={(event) => setDeadline(event.target.value)}
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