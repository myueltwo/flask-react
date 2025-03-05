import React, {useState} from "react";
import {useGetSubjectsQuery} from "../../model";
import {TableInfo} from "../TableInfo";
import {entitiesProperties} from "../../lib";
import {SUBJECT} from "shared/constants";
import {ISubject, ITableInfoProps} from "../../types";
import {CustomFetchBaseQueryError} from "shared/types";
import {ChangingForm} from "./ChangingForm";

export const Subjects: React.FC = () => {
    const {data, isLoading, isError, error} = useGetSubjectsQuery();
    const fields = entitiesProperties[SUBJECT];

    const [show, setShow] = useState(false);
    const [isAdd, setAdd] = useState(false);
    const handleAddItem = () => {
        setShow(true);
        setAdd(true);
    };
    const tableInfoProps: ITableInfoProps = {
        fields,
        isLoading,
        isError,
        error: error as CustomFetchBaseQueryError,
        onAddItem: handleAddItem,
    };

    return (
        <>
            <TableInfo {...tableInfoProps}>
                {data?.items.map((item, index) => (
                    <tr key={`row-item-${index}`}>
                        <td key={`field-${index}`}>{index + 1}</td>
                        {fields.map(({id}) => (
                            <td key={`field-${id}`}>{item[id as keyof ISubject]}</td>
                        ))}
                    </tr>
                ))}
            </TableInfo>
            <ChangingForm show={show} isAdding={isAdd} onHide={() => setShow(false)}/>
        </>
    );
}