import React, {useState} from "react";
import { PencilFill, TrashFill } from "react-bootstrap-icons";
import {useGetSubjectsQuery, useDeleteSubjectMutation} from "../../model";
import {TableInfo} from "../TableInfo";
import {entitiesProperties} from "../../lib";
import {SUBJECT} from "shared/constants";
import {ISubject, ITableInfoProps} from "../../types";
import {CustomFetchBaseQueryError} from "shared/types";
import {ChangingForm} from "./ChangingForm";
import {EditForm} from "./EditForm";
import {AddForm} from "./AddForm";

export const Subjects: React.FC = () => {
    const {data, isLoading, isError, error} = useGetSubjectsQuery();
    const [deleteSubject] = useDeleteSubjectMutation();
    const fields = entitiesProperties[SUBJECT];

    const [show, setShow] = useState(false);
    const [itemId, setItemId] = useState<string>("");
    const handleAddItem = () => {
        setShow(true);
    };
    const handleHideModal = () => {
        setShow(false);
        setItemId("");
    }
    const tableInfoProps: ITableInfoProps = {
        fields,
        isLoading,
        isError,
        error: error as CustomFetchBaseQueryError,
        onAddItem: handleAddItem,
    };
    const formProps = {
        show,
        itemId,
        onHide: handleHideModal
    };
    const addFormProps = {
        isAdding: true,
        ...formProps,
    }
    const handleEditItem = (id: string) => {
        setShow(true);
        setItemId(id);
    };
    const handleRemoveItem = (id: string) => {
        deleteSubject(id);
    }

    return (
        <>
            <TableInfo {...tableInfoProps}>
                {data?.items.map((item, index) => (
                    <tr key={`row-item-${index}`}>
                        <td key={`field-${index}`}>{index + 1}</td>
                        {fields.map(({id}) => (
                            <td key={`field-${id}`}>{item[id as keyof ISubject]}</td>
                        ))}
                        <td>
                            <a className="btn btn-outline-info mx-1" onClick={() => handleEditItem(item.id)} role="button"
                               title="Edit item">
                                <PencilFill/>
                            </a>
                            <a className="btn btn-outline-danger mx-1" onClick={() => handleRemoveItem(item.id)} role="button"
                               title="Delete item">
                                <TrashFill/>
                            </a>
                        </td>
                    </tr>
                ))}
            </TableInfo>
            {show && (itemId ? (<EditForm {...formProps}/>) : (<AddForm {...addFormProps}/>))}
        </>
    );
}