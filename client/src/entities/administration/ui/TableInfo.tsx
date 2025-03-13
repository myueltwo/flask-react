import React, {FC, PropsWithChildren} from "react";
import {ITableInfoProps} from "../types";
import {Button, Container, Table, Placeholder, Alert} from "react-bootstrap";
import {NO_DATA_FOUND, SOMETHING_WRONG} from "shared/constants";
import {Pagination} from "shared/ui";

export const TableInfo: FC<PropsWithChildren<ITableInfoProps>> = ({isLoading, fields, children, isError, error, onAddItem, pagination}) => {
    if (!fields) {
        return (
            <Container>
                <div className="my-1">{NO_DATA_FOUND}</div>
            </Container>
        );
    }
    if (isError) {
        return (
            <Container>
                <Alert variant="danger" className="my-1">
                    {error?.data?.message || SOMETHING_WRONG}
                </Alert>
            </Container>
        )
    }
    return (
        <Container>
            {isLoading ? (<Placeholder.Button variant="primary" xs={6}/>)
                : (<Button variant="outline-info" className="my-1" onClick={onAddItem}>Add item</Button>)
            }
            <Table striped bordered hover>
                <thead>
                <tr>
                    <th>#</th>
                    {fields.map(({id, name}) => (
                        <th key={id}>{name}</th>
                    ))}
                    <th>Actions</th>
                </tr>
                </thead>
                <tbody>
                    {children}
                </tbody>
            </Table>
            {pagination && <Pagination {...pagination}/>}
        </Container>
    );
}