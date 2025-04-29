import React from 'react';
import {ITableInfoProps} from "../types";
import {SUBJECT, LAB} from "shared/constants";
import {Subjects, Labs} from "entities/administration";

export const TableInfo: React.FC<ITableInfoProps> = ({entity}) => {
    if (entity === SUBJECT) {
        return <Subjects/>
    }
    if (entity === LAB) {
        return <Labs/>
    }
    return null;
}