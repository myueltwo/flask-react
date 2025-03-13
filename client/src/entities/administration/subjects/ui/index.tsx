import React, {useState} from "react";
import {Button} from "react-bootstrap";
import { PencilFill, TrashFill } from "react-bootstrap-icons";
import {useGetSubjectsQuery, useDeleteSubjectMutation} from "../model";
import {TableInfo, ITableInfoProps} from "entities/administration";
import {entitiesProperties} from "../lib";
import {SUBJECT} from "shared/constants";
import {ISubject,} from "../types";
import {CustomFetchBaseQueryError} from "shared/types";
import {EditForm} from "./form/EditForm";
import {AddForm} from "./form/AddForm";

export const Subjects: React.FC = () => {
    const [page, setPage] = useState(1)
    const {data, isLoading, isError, error} = useGetSubjectsQuery({page, per_page: 5});
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
        ...(data ? {
            pagination: {
                has_next: data.has_next,
                has_prev: data.has_prev,
                page: data.page,
                total_pages: data.total_pages,
                onLoad: (page: number) => setPage(page),
            }
        } : {}),
    };
    const formProps = {
        show,
        itemId,
        onHide: handleHideModal
    };
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
                            <Button variant="outline-info" className="mx-1" title="Edit item" onClick={() => handleEditItem(item.id)}>
                                <PencilFill/>
                            </Button>
                            <Button variant="outline-danger" className="mx-1" title="Delete item" onClick={() => handleRemoveItem(item.id)}>
                                <TrashFill/>
                            </Button>
                        </td>
                    </tr>
                ))}
            </TableInfo>
            {show && (itemId ? (<EditForm {...formProps}/>) : (<AddForm {...formProps}/>))}
        </>
    );
}