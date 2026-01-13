import React, {useState} from "react";
import {useGetActivityTypesQuery, useDeleteActivityTypeMutation} from "../model";
import { WidgetList } from "shared/ui";
import {EditForm, AddForm} from "./form";
import {CustomFetchBaseQueryError} from "shared/types";

export const ActivityTypes: React.FC = () => {
    const [page, setPage] = useState(1);
    const [itemId, setItemId] = useState<string>("");
    const [show, setShow] = useState(false);
    const {data, isLoading, isError, error} = useGetActivityTypesQuery({page});
    const [deleteItem] = useDeleteActivityTypeMutation();
    const props = {
        data, isLoading, isError, error: error as CustomFetchBaseQueryError, deleteItem, setPage, page, setItemId, setShow,
    };
    const formProps = {
        show,
        itemId,
        onHide: () => {
            setShow(false);
            setItemId("");
        },
    };
    return (
        <WidgetList {...props}>
            {show && (itemId ? (<EditForm {...formProps}/>) : (<AddForm {...formProps}/>))}
        </WidgetList>
    );
}