import React, {PropsWithChildren} from "react";
import { Actions} from "./Actions";
import { TableInfo } from "./TableInfo";
import {NAME} from "shared/constants";
import {IItemEditRequest, IItemWidget} from "shared/types";
import {IWidgetListProps, ITableInfoProps} from "./types";
import {Messages} from "../../messages";

export const WidgetList: React.FC<PropsWithChildren<IWidgetListProps>> = ({
    data, isLoading, isError, error, deleteItem, setPage, page,
    setItemId, setShow, children,
}) => {
    const fields = [{
        id: "name",
        name: NAME,
    }];

    const handleAddItem = () => {
        setShow(true);
    };
    const tableInfoProps: ITableInfoProps = {
        fields,
        isLoading,
        isError,
        error: error,
        onAddItem: handleAddItem,
        pagination: {
            has_next: data?.has_next || false,
            has_prev: data?.has_prev || false,
            page: data?.page || page,
            total_pages: data?.total_pages || 0,
            onLoad: (page: number) => setPage(page),
        }
    };

    const handleEditItem = (id: string) => {
        setShow(true);
        setItemId(id);
    };
    const handleRemoveItem = (id: string) => {
        deleteItem(id);
    }

    return (
        <>
            <TableInfo {...tableInfoProps}>
                {Boolean(data?.items?.length) ? (data.items as IItemEditRequest[]).map((item, index) => (
                    <tr key={`row-item-${index}`}>
                        <td key={`field-${index}`}>{index + 1}</td>
                        {fields.map(({id}) => (
                            <td key={`field-${id}`}>{item[id as keyof IItemWidget]}</td>
                        ))}
                        <td>
                            <Actions itemId={item.id} onEdit={handleEditItem} onRemove={handleRemoveItem} />
                        </td>
                    </tr>
                )) : Messages.noDataFound }
            </TableInfo>
            {children}
        </>
    );
}