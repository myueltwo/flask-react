import React from 'react';
import {ITableInfoProps} from "../types";
import {SUBJECT} from "shared/constants";
import {Subjects} from "entities/administration";

export const TableInfo: React.FC<ITableInfoProps> = ({entity}) => {
    if (entity === SUBJECT) {
        return <Subjects/>
    }
    return null;
}