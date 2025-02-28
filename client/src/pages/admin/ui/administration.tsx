import React, {useState} from 'react';
import {ListGroup, Container, Row, Col} from "react-bootstrap";
import {getListItems} from "../lib";
import {TableInfo} from "./tableInfo";

export const Administration = () => {
    const listItems = getListItems();
    const [listSelected, setListSelected] = useState(listItems[0].id);

    const handleClick = (key: string | null) => {
        if (key) {
            setListSelected(key);
        }
    }

    return (
        <Container>
            <Row>
                <Col sm={3}>
                    <ListGroup variant="flush" onSelect={handleClick} activeKey={listSelected}>
                        {listItems.map(({name, id}) => (
                            <ListGroup.Item action eventKey={id}>{name}</ListGroup.Item>
                        ))}
                    </ListGroup>
                </Col>
                <Col sm={9}>
                    <TableInfo/>
                </Col>
            </Row>
        </Container>
    );
}