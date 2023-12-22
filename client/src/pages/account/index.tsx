import React, {useState} from "react";
import {Card, Container, Row, Col} from "react-bootstrap";
import {Person} from "react-bootstrap-icons";
import {useAppSelector} from 'app/hooks';
import {selectCurrentUser} from "entities/users";
import {ResetToken} from "./resetToken";

export const Account = () => {
    const {fullName, role, group} = useAppSelector(selectCurrentUser) || {};
    const roleName = `Role: ${role?.name || ""}`;
    const groupName = group ? `Group: ${group.name}` : "";
    const [openForm, setOpenForm] = useState(false);
    const handleClickForm = () => {
        setOpenForm(true);
    }
    const handleCancel = () => {
        setOpenForm(false);
    }

    return (
        <Container>
            <Card className="mb-3 m-2">
                <Card.Body>
                    <Container>
                        <Row>
                            <Col md={4}>
                                <Person size={116}/>
                            </Col>
                            <Col md={8}>
                                <Card.Title>
                                    {fullName}
                                </Card.Title>
                                <Card.Text>
                                    {roleName}
                                    {groupName}
                                    <br/>
                                </Card.Text>
                                {openForm ? (
                                    <ResetToken onCancel={handleCancel}/>
                                ) : (
                                    <a className="text-muted" href="#" onClick={handleClickForm}>
                                        Do you want to change password?
                                    </a>
                                )}
                            </Col>
                        </Row>
                    </Container>
                </Card.Body>
            </Card>
        </Container>
    );
};
