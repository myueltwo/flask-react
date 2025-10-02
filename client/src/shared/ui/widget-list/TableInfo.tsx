import React, {FC, PropsWithChildren} from "react";
import {Button, Container, Table, Placeholder, Alert} from "react-bootstrap";
import {Messages} from "shared/messages";
import {Pagination} from "shared/ui";
import {ITableInfoProps} from "./types";

export const TableInfo: FC<PropsWithChildren<ITableInfoProps>> = ({isLoading, fields, children, isError, error, onAddItem, pagination}) => {
    if (!fields) {
        return (
            <Container>
                <div className="my-1">{Messages.noDataFound}</div>
            </Container>
        );
    }
    if (isError) {
        return (
            <Container>
                <Alert variant="danger" className="my-1">
                    {error?.data?.message || Messages.somethingWrong}
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