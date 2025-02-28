import React from "react";
import {Card, Placeholder} from "react-bootstrap";

export const buildCardInfo = (fullName: string, roleName: string, groupName: string) => (
    <>
        <Card.Title>
            {fullName}
        </Card.Title>
        <Card.Text>
            {roleName}
            {groupName}
            <br/>
        </Card.Text>
    </>
);

export const buildSkeletonInfo = () => (
    <>
        <Placeholder as={Card.Title} animation="glow">
            <Placeholder xs={12}/>
        </Placeholder>
        <Placeholder as={Card.Text} animation="glow">
            <Placeholder xs={8}/>
            <Placeholder xs={8}/>
        </Placeholder>
    </>
);