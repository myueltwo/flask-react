import {
    LAB,
    ATTENDANCE,
    ATTENDANCE_TYPE,
    SUBJECT,
    ACTIVITY_SUB_TYPE,
    GRADE,
    GROUP,
    ROLE,
    ACTIVITY_TYPE,
    USER,
    TYPE_GRADE,
    RATE_ACTIVITY,
} from "shared/constants";

export const getListItems = () => [
    {
        name: 'Subjects',
        id: SUBJECT
    }, {
        name: 'Laboratory practice',
        id: LAB
    }, {
        name: 'Schedule',
        id: ATTENDANCE
    }, {
        name: 'Type of attendance',
        id: ATTENDANCE_TYPE
    }, {
        name: 'Grades',
        id: GRADE
    }, {
        name: 'Type of grades',
        id: TYPE_GRADE
    }, {
        name: 'Groups',
        id: GROUP
    }, {
        name: 'Roles',
        id: ROLE
    }, {
        name: 'Users',
        id: USER
    }, {
        name: 'Type of activities',
        id: ACTIVITY_TYPE
    }, {
        name: 'Subtype of activities',
        id: ACTIVITY_SUB_TYPE
    }, {
        name: 'Rating of activities',
        id: RATE_ACTIVITY
    }
];