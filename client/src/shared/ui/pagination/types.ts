import {IPaginationProps as IPagination} from "shared/types";

export interface IPaginationProps extends IPagination {
    onLoad: (page: number) => void;
}