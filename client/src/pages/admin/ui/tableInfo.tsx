import React from 'react';
import {ITableInfoProps} from "../types";
import {SUBJECT, LAB, ATTENDANCE_TYPE} from "shared/constants";
import {Subjects, Labs, TypeAttendance} from "entities/administration";

export const TableInfo: React.FC<ITableInfoProps> = ({entity}) => {
    switch (entity) {
        case SUBJECT:
            return <Subjects/>;
        case LAB:
            return <Labs/>;
        case ATTENDANCE_TYPE:
            return <TypeAttendance/>;
        default:
            return null;
    }
};