import React, {useState, FormEvent, useEffect} from "react";
import {Form, Button, Alert, Container, Row} from 'react-bootstrap';
import {useNavigate} from "react-router-dom";
import styled from "styled-components";
import { useLoginMutation } from "services/api";
import { getAuthToken } from "shared";
import { Messages } from "shared/messages";
import { CustomFetchBaseQueryError } from "shared/types";

export const Login = () => {
    const [ fetchLogin, { error, isError } ] = useLoginMutation();
    const [login, setLogin] = useState("");
    const [password, setPassword] = useState("");
    const [validated, setValidated] = useState(false);
    const authToken = getAuthToken();
    const variant = authToken ? "success" : "danger";
    const navigate = useNavigate();

    const handleSubmit = (event: FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        const form = event.currentTarget;
        if (!form.checkValidity()) {
            event.stopPropagation();
        }
        fetchLogin({login, password});
        setValidated(true);
    }

    useEffect(() => {
        if (authToken) {
            navigate("/");
        }
    }, [authToken]);

    return (
        <Container>
            <h1>
                Log In
            </h1>
            <Row>
                <FormWrap noValidate validated={validated} onSubmit={handleSubmit}>
                    <Form.Group className="mb-3" controlId="loginForm.login">
                        <Form.Label>Login</Form.Label>
                        <Form.Control
                            type="text"
                            placeholder="Enter login"
                            required
                            value={login}
                            onChange={(event) => setLogin(event.target.value)}
                        />
                    </Form.Group>
                    <Form.Group className="mb-3" controlId="loginForm.password">
                        <Form.Label>Password</Form.Label>
                        <Form.Control
                            type="password"
                            placeholder="Enter password"
                            required
                            value={password}
                            onChange={(event) => setPassword(event.target.value)}
                        />
                    </Form.Group>
                    {isError && (
                        <Alert key={variant} variant={variant}>
                            {(error as CustomFetchBaseQueryError).data.message || Messages.somethingWrong}
                        </Alert>
                    )}
                    <Button type="submit">Enter</Button>
                </FormWrap>
            </Row>
        </Container>
    );
};

const FormWrap = styled(Form)`
    max-width: 50%;
`;