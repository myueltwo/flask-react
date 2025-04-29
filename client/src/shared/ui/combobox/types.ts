import {SyntheticEvent} from "react";

export interface IItem {
    key: string;
    value: string;
}

export interface IComboboxProps {
    items: IItem[];
    selectedItem?: IItem;
    onChange: (item?: IItem) => void;
    isLoading?: boolean;
    isError?: boolean;
}

export interface ICustomToggleProps {
    onClick: (event: SyntheticEvent) => void;
    search?: string;
    setSearch: (text: string) => void;
    selectedItem?: IItem;
    onRemove: () => void;
}