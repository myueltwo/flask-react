import React from "react";
import {Toast, ToastContainer} from "react-bootstrap";
import {Messages} from "../../messages";
import {IErrorNotification} from "./types";

export const ErrorNotification: React.FC<IErrorNotification> = ({error}) => (
    <ToastContainer position="top-end" className="p-3" style={{zIndex: 1000}}>
        <Toast delay={3000} bg="danger" autohide>
            <Toast.Header>
                <strong className="me-auto">Error</strong>
            </Toast.Header>
            <Toast.Body
                className="text-white">{error?.data?.message || Messages.somethingWrong}</Toast.Body>
        </Toast>
    </ToastContainer>
)