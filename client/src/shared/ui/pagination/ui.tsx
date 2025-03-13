import React from "react";
import {Pagination as PaginationComponent} from "react-bootstrap";
import {IPaginationProps} from "./types";
import {getPages} from "./lib";

export const Pagination: React.FC<IPaginationProps> = ({
    has_prev,
    page,
    total_pages,
    has_next,
    onLoad
}) => {
    const pages = getPages(page, total_pages);
    const onClickPage = (page: string | number) => {
        if (typeof page !== "string") {
             onLoad(page);
        }
    }
    const content = (
        <>
            {has_prev && <PaginationComponent.Prev onClick={() => onLoad(page-1)}/>}
            {pages.map((value) => (
                <PaginationComponent.Item
                    key={`page-${value}`}
                    active={value === page}
                    disabled={value === "..."}
                    onClick={() => onClickPage(value)}
                >
                    {value}
                </PaginationComponent.Item>))
            }
            {has_next && <PaginationComponent.Next onClick={() => onLoad(page+1)}/>}
        </>
    )
    return (
        <PaginationComponent>
            {content}
        </PaginationComponent>
    );
}