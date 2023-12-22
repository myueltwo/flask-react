import React, {FC, FormEvent, useState} from "react";
import {Button, Form} from "react-bootstrap";
import styled from "styled-components";
import {IResetToken} from "./types";

export const ResetToken: FC<IResetToken> = ({onCancel}) => {
    const [password, setPassword] = useState("");
    const [repeatPassword, setRepeatPassword] = useState("");
    const [validated, setValidated] = useState(false);

    const handleSubmit = (event: FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        event.stopPropagation();

        if (password === repeatPassword) {
            setValidated(true);
            onCancel(true);
        }
    };

    return (
        <FormWrap noValidate validated={validated} onSubmit={handleSubmit}>
            <Form.Group className="mb-3" controlId="ResetToken.newPassword">
                <Form.Label>New password</Form.Label>
                <Form.Control
                    type="password"
                    placeholder="Enter new password"
                    required
                    value={password}
                    onChange={(event) => setPassword(event.target.value)}
                />
            </Form.Group>
            <Form.Group className="mb-3" controlId="ResetToken.repeatPassword">
                <Form.Label>Repeat password</Form.Label>
                <Form.Control
                    type="password"
                    placeholder="Repeat password"
                    required
                    value={repeatPassword}
                    onChange={(event) => setRepeatPassword(event.target.value)}
                />
            </Form.Group>
            {/*{Boolean(authError) && (*/}
            {/*    <Alert key={variant} variant={variant}>*/}
            {/*        {authError}*/}
            {/*    </Alert>*/}
            {/*)}*/}
            <ButtonsWrap>
                <Button type="submit">Enter</Button>
                <Button variant="secondary" onClick={() => onCancel()}>Cancel</Button>
            </ButtonsWrap>
        </FormWrap>
    );
};

const FormWrap = styled(Form)`
    max-width: 70%;
`;

const ButtonsWrap = styled.div`
    display: flex;
    gap: 1rem;
`