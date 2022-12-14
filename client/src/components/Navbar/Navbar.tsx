import React from "react";
import {Navbar, Container, Nav} from "react-bootstrap";
import {PersonFill} from "react-bootstrap-icons";

function NavbarHeader() {
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
                        <Nav.Link href="/account">
                            <PersonFill className="d-inline-block"/>
                            current user
                        </Nav.Link>
                        <Nav.Link href="#logout">Logout</Nav.Link>
                        <Nav.Link href="#login">Login</Nav.Link>
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    );
}

export default NavbarHeader;