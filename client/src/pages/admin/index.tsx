import React, {useState} from 'react';
import {Nav, Container} from "react-bootstrap";
import {Administration} from "./ui/administration";

export const Admin = () => {
    const [tab, setTab] = useState("rating");

    const handleClick = (key: string | null) => {
        if (key) {
            setTab(key);
        }
    }
    return (
        <Container className="pt-2">
            <Nav className="justify-content-end" variant="tabs" activeKey={tab} onSelect={handleClick}>
                <Nav.Item >
                    <Nav.Link eventKey="rating">Rating</Nav.Link>
                </Nav.Item>
                <Nav.Item >
                    <Nav.Link eventKey="admin">Administration</Nav.Link>
                </Nav.Item>
            </Nav>
            {tab === "admin" && (
                <Administration/>
            )}
        </Container>
    );
}