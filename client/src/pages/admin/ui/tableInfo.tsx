import React from 'react';
import {ITableInfoProps} from "../types";
import {SUBJECT, LAB, ATTENDANCE_TYPE, TYPE_GRADE, GROUP, ROLE} from "shared/constants";
import {Subjects, Labs, TypeAttendance, TypesGrade, Groups, Roles} from "entities/administration";

export const TableInfo: React.FC<ITableInfoProps> = ({entity}) => {
    switch (entity) {
        case SUBJECT:
            return <Subjects/>;
        case LAB:
            return <Labs/>;
        case ATTENDANCE_TYPE:
            return <TypeAttendance/>;
        case TYPE_GRADE:
            return <TypesGrade/>;
        case GROUP:
            return <Groups/>;
        case ROLE:
            return <Roles/>;
        default:
            return null;
    }
};