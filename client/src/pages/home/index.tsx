import React from 'react';
import {Alert} from "react-bootstrap";
import { useGetCurrentUserQuery } from "services/api";
import {Admin} from "../admin";

export const Home = () => {
    const variant = 'success'
    const { data } = useGetCurrentUserQuery();

    if (data?.role?.name === "Студент") {
        return <Admin/>
    }

    return (
        <div>
            <h1>home</h1>
            <Alert key={variant} variant={variant}>
                {data?.role?.name}
            </Alert>
        </div>
    );
};
