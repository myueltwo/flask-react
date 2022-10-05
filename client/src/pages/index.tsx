import React from 'react';
import {Alert} from "react-bootstrap";

const Home = () => {
    const variant = 'success'

    return (
        <div>
            <h1>home</h1>
            <Alert key={variant} variant={variant}>
                This is a {variant} alert—check it out!
            </Alert>
        </div>
    );
};

export default Home;