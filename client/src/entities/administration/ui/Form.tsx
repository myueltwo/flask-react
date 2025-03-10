import React, {FC, PropsWithChildren} from "react";
import {Modal, Button, Spinner} from "react-bootstrap";
import {IModalForm} from "../types";
import {ADD_ITEM, UPDATE_ITEM, CLOSE, SAVE} from "shared/constants";

export const FormModal: FC<PropsWithChildren<IModalForm>> = ({
    show,
    onHide,
    children,
    isAdding = false,
    onSave,
    isUpdating
}) => {
    const title = isAdding ? ADD_ITEM : UPDATE_ITEM;
    return (
        <Modal show={show} onHide={onHide}>
            <Modal.Header>
                <Modal.Title>{title}</Modal.Title>
            </Modal.Header>
            <Modal.Body>
                {children}
            </Modal.Body>
            <Modal.Footer>
                <Button variant="secondary" onClick={onHide}>
                    {CLOSE}
                </Button>
                <Button variant="primary" onClick={onSave} disabled={isUpdating}>
                    {isUpdating && (
                        <Spinner
                            as="span"
                            animation="border"
                            size="sm"
                            role="status"
                            aria-hidden="true"
                        />
                    )}
                    {SAVE}
                </Button>
            </Modal.Footer>
        </Modal>
    );
}