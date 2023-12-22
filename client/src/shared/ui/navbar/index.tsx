import React from "react";
import {Navbar, Container, Nav} from "react-bootstrap";
import {PersonFill} from "react-bootstrap-icons";
import { useAppSelector } from 'app/hooks';
import { selectAuthToken, selectCurrentUser } from "entities/users";

export const NavbarHeader = () => {
    const authToken = useAppSelector(selectAuthToken);
    const { surname, name, patronymic } = useAppSelector(selectCurrentUser) || {};
    const currentName = [surname, name?.at(0),  patronymic?.at(0)].filter(Boolean).join(" ");
    return (
        <Navbar bg="primary" expand="lg" variant="dark">
            <Container>
                <Navbar.Brand href="/">Score system</Navbar.Brand>
                <Navbar.Toggle/>
                <Navbar.Collapse className="justify-content-end">
                    <Nav className="me-auto">
                        <Nav.Link href="/about">By project</Nav.Link>
                    </Nav>
                    <Nav>
                        {Boolean(authToken) ? (
                            <>
                                <Nav.Link href="/account">
                                    <PersonFill className="d-inline-block"/>
                                    {currentName}
                                </Nav.Link>
                                <Nav.Link href="/logout">Logout</Nav.Link>
                            </>
                        ) : <Nav.Link href="/login">Login</Nav.Link>
                        }
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    );
}