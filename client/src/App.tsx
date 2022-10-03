import React from 'react';
import {Alert} from "react-bootstrap";
import './App.scss';

function App() {
    const variant = 'success'
    return (
        <div className="App">
            <Alert key={variant} variant={variant}>
                    This is a {variant} alert—check it out!
                </Alert>
            <header className="App-header">
                dfsdf

            </header>
        </div>
    );
}

export default App;
