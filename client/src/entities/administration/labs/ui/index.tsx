import React, {useState} from "react";
import {useGetLabsQuery, useDeleteLabMutation} from "../model";
import {TableInfo, ITableInfoProps, Actions} from "entities/administration";
import {entitiesProperties} from "../lib";
import {ILab} from "../types";
import {CustomFetchBaseQueryError} from "shared/types";
import {AddForm, EditForm} from "./form";

export const Labs: React.FC = () => {
    const [page, setPage] = useState(1)
    const {data, isLoading, isError, error} = useGetLabsQuery({page, per_page: 5});
    const [deleteSubject] = useDeleteLabMutation();
    const fields = entitiesProperties;

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
                        {fields.map(({id}) => {
                            if (id === "subject") {
                                return (<td key={`field-${id}`}>{item[id as keyof ILab].name}</td>);
                            }
                            return (<td key={`field-${id}`}>{item[id as keyof Omit<ILab, "subject">]}</td>);
                        })}
                        <td>
                            <Actions itemId={item.id} onEdit={handleEditItem} onRemove={handleRemoveItem} />
                        </td>
                    </tr>
                ))}
            </TableInfo>
            {show && (itemId ? (<EditForm {...formProps}/>) : (<AddForm {...formProps}/>))}
        </>
    );
}