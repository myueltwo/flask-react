import React from "react";
import {useGetSubjectsQuery} from "../model";
import {TableInfo} from "./TableInfo";
import {entitiesProperties} from "../lib";
import {SUBJECT} from "shared/constants";
import {ISubject} from "../../types";
import {CustomFetchBaseQueryError} from "shared/types";

export const Subjects: React.FC = () => {
    const { data, isLoading, isError, error } = useGetSubjectsQuery();
    const fields = entitiesProperties[SUBJECT];
    const tableInfoProps = {
        fields,
        isLoading,
        isError,
        error: error as CustomFetchBaseQueryError,
    }
    return (
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
    );
}