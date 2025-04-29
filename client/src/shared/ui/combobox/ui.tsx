import React, {SyntheticEvent, useRef, useState} from "react";
import {Dropdown, Form, CloseButton, Alert} from 'react-bootstrap';
import {Messages} from "shared/messages";
import {IComboboxProps, ICustomToggleProps} from "./types";
import styled from "styled-components";

const CustomToggle = React.forwardRef<any, ICustomToggleProps>(({
                                                                    onClick,
                                                                    search,
                                                                    setSearch,
                                                                    selectedItem,
                                                                    onRemove
                                                                }, ref) => {
    const refInput = useRef(null);
    const onRemoveHandle = (e: SyntheticEvent) => {
        onRemove();
        setSearch("");
        onClick(e);
        if (refInput?.current) {
            refInput.current.focus();
        }
    }
    return (
        <CustomToggleWrap ref={ref}>
            <Form.Control
                type="text"
                placeholder={Messages.search}
                onChange={(e) => setSearch(e.target.value)}
                onClick={(e) => {
                    e.preventDefault();
                    onClick(e);
                }}
                value={selectedItem ? selectedItem.value : search}
                ref={refInput}
            />
            {selectedItem && (<StyledCloseButton onClick={onRemoveHandle}/>)}
        </CustomToggleWrap>
    );
});

const CustomToggleWrap = styled.div`
    display: flex;
`;

const StyledCloseButton = styled(CloseButton)`
    position: absolute;
    right: 1rem;
    top: 0.74rem;
    width: 0.5rem;
    height: 0.5rem;
`;

export const Combobox: React.FC<IComboboxProps> = ({items, selectedItem, onChange, isLoading, isError, error}) => {
    const [search, setSearch] = useState('');
    const filteredItems = search ? items.filter(({value}) => value.includes(search)) : items;

    return (
        <Dropdown>
            <Dropdown.Toggle as={CustomToggle} search={search} setSearch={setSearch} selectedItem={selectedItem}
                             onRemove={onChange}/>
            <StyledDropdownMenu>
                {isLoading && Messages.loading}
                {isError && (
                    <Alert key="danger" variant="danger" className="mx-2">
                        {Messages.somethingWrong}
                    </Alert>
                )}
                {filteredItems.map(({value, key}) => (
                    <Dropdown.Item key={key} href="#" onClick={() => onChange({key, value})}>{value}</Dropdown.Item>
                ))}
            </StyledDropdownMenu>
        </Dropdown>
    );
};

const StyledDropdownMenu = styled(Dropdown.Menu)`
    width: 100%;
`;