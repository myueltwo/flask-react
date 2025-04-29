import React, {FC, PropsWithChildren} from "react";
import {Modal, Button, Spinner} from "react-bootstrap";
import {IModalForm} from "../types";
import {ADD_ITEM, UPDATE_ITEM} from "shared/constants";
import {Messages} from "shared/messages";

export const FormModal: FC<PropsWithChildren<IModalForm>> = ({
    show,
    onHide,
    children,
    isAdding = false,
    onSave,
    isUpdating
}) => {
    const title = isAdding ? ADD_ITEM : UPDATE_ITEM;
    const {actions} = Messages;
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
                    {actions.close}
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
                    {actions.save}
                </Button>
            </Modal.Footer>
        </Modal>
    );
}