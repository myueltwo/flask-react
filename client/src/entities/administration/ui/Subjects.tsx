import React, {useState} from "react";
import {useGetSubjectsQuery} from "../model";
import {TableInfo} from "./TableInfo";
import {entitiesProperties} from "../lib";
import {NAME, NUMBER_OF_HOURS, SUBJECT} from "shared/constants";
import {ISubject, ITableInfoProps} from "../types";
import {CustomFetchBaseQueryError} from "shared/types";
import {Form} from "react-bootstrap";
import {FormModal} from "./Form";

export const Subjects: React.FC = () => {
    const {data, isLoading, isError, error} = useGetSubjectsQuery();
    const fields = entitiesProperties[SUBJECT];

    const [show, setShow] = useState(false);
    const [isAdd, setAdd] = useState(false);
    const handleClose = () => setShow(false);
    const handleAddItem = () => {
        setShow(true);
        setAdd(true);
    };
    const tableInfoProps: ITableInfoProps = {
        fields,
        isLoading,
        isError,
        error: error as CustomFetchBaseQueryError,
        onAddItem: handleAddItem,
    };

    return (
        <>
            <TableInfo {...tableInfoProps}>
                {data?.items.map((item, index) => (
                    <tr key={`row-item-${index}`}>
                        <td key={`field-${index}`}>{index + 1}</td>
                        {fields.map(({id}) => (
                            <td key={`field-${id}`}>{item[id as keyof ISubject]}</td>
                        ))}
                    </tr>
                ))}
            </TableInfo>
            <FormModal show={show} onHide={handleClose} isAdding={isAdd} onSave={handleClose}>
                <Form>
                    <Form.Group className="mb-3" controlId="subjectForm.name">
                        <Form.Label>{NAME}</Form.Label>
                        <Form.Control
                            type="text"
                            placeholder="Enter name"
                            required
                        />
                    </Form.Group>
                    <Form.Group className="mb-3" controlId="subjectForm.number_of_hours">
                        <Form.Label>{NUMBER_OF_HOURS}</Form.Label>
                        <Form.Control
                            type="number"
                            placeholder="Enter number of hours"
                            required
                        />
                    </Form.Group>
                </Form>
            </FormModal>
        </>
    );
}