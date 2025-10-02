import { api } from "services/api";
import {ILabRequest, ILab} from "./types";
import {CustomFetchBaseQueryError, IAddItemResponse, IPageProps, ListResponse} from "shared/types";

const administrationApi = api
    .enhanceEndpoints({
        addTagTypes: ["Labs"],
    })
    .injectEndpoints({
    endpoints: (build) => ({
        getLabs: build.query<ListResponse<ILab>, IPageProps | undefined>({
            query: (params) => ({
                url: "widgets/labs",
                params,
                method: "GET",
            }),
            providesTags: (result) =>
                result
                    ? [
                        ...result.items.map(({ id }) => ({ type: "Labs" as const, id })),
                        { type: 'Labs', id: 'PARTIAL-LIST' },
                    ]
                    : [{ type: 'Labs', id: 'PARTIAL-LIST' }],
        }),
        addLab: build.mutation<CustomFetchBaseQueryError | IAddItemResponse, Omit<ILabRequest, "id">>({
            query: (body) => ({
                url: "widgets/labs",
                method: "POST",
                body,
            }),
            invalidatesTags: () => [{ type: 'Labs', id: 'PARTIAL-LIST' }],
        }),
        getLab: build.query<ILab, string>({
            query: (id) => `widgets/labs/${id}`,
            providesTags: (result) => result ? [{ type: "Labs" as const, id: result.id }]: [],
        }),
        editLab: build.mutation<CustomFetchBaseQueryError | void, ILabRequest>({
            query: ({id, ...body}) => ({
                url: `widgets/labs/${id}`,
                method: "PUT",
                body,
            }),
            invalidatesTags: (result, error, { id }) => [
                {type: 'Labs', id},
                {type: 'Labs', id: 'PARTIAL-LIST'},
            ],
        }),
        deleteLab: build.mutation<CustomFetchBaseQueryError | void, string>({
            query: (id) => ({
                url: `widgets/labs/${id}`,
                method: "DELETE",
            }),
            invalidatesTags: (result, error, id) => [
                {type: 'Labs', id},
                {type: 'Labs', id: 'PARTIAL-LIST'},
            ],
        }),
    }),
    overrideExisting: false,
});

export const { useGetLabsQuery, useAddLabMutation, useDeleteLabMutation, useEditLabMutation, useGetLabQuery } = administrationApi;