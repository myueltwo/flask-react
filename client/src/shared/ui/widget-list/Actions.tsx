import React from "react";
import {Button} from "react-bootstrap";
import {PencilFill, TrashFill} from "react-bootstrap-icons";
import {IActions} from "./types";

export const Actions: React.FC<IActions> = ({onEdit, onRemove, itemId}) => (
    <>
        <Button variant="outline-info" className="mx-1" title="Edit item" onClick={() => onEdit(itemId)}>
            <PencilFill/>
        </Button>
        <Button variant="outline-danger" className="mx-1" title="Delete item" onClick={() => onRemove(itemId)}>
            <TrashFill/>
        </Button>
    </>
);