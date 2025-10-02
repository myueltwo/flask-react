import { api } from "services/api";
import {CustomFetchBaseQueryError, IAddItemResponse, IPageProps, ListResponse, IItemRequest, IItemEditRequest, IItemWidget} from "shared/types";

const administrationApi = api
    .enhanceEndpoints({
        addTagTypes: ["Groups"],
    })
    .injectEndpoints({
    endpoints: (build) => ({
        getGroups: build.query<ListResponse<IItemWidget>, IPageProps | undefined>({
            query: (params) => ({
                url: "widgets/groups",
                params,
                method: "GET",
            }),
            providesTags: (result) =>
                result
                    ? [
                        ...result.items.map(({ id }) => ({ type: "Groups" as const, id })),
                        { type: 'Groups', id: 'PARTIAL-LIST' },
                    ]
                    : [{ type: 'Groups', id: 'PARTIAL-LIST' }],
        }),
        addGroups: build.mutation<CustomFetchBaseQueryError | IAddItemResponse, IItemRequest>({
            query: (body) => ({
                url: "widgets/groups",
                method: "POST",
                body,
            }),
            invalidatesTags: () => [{ type: 'Groups', id: 'PARTIAL-LIST' }],
        }),
        getGroup: build.query<IItemWidget, string>({
            query: (id) => `widgets/groups/${id}`,
            providesTags: (result) => result ? [{ type: "Groups" as const, id: result.id }]: [],
        }),
        editGroup: build.mutation<CustomFetchBaseQueryError | void, IItemEditRequest>({
            query: ({id, name}) => ({
                url: `widgets/groups/${id}`,
                method: "PUT",
                body: {
                    name,
                },
            }),
            invalidatesTags: (result, error, { id }) => [
                {type: 'Groups', id},
                {type: 'Groups', id: 'PARTIAL-LIST'},
            ],
        }),
        deleteGroup: build.mutation<CustomFetchBaseQueryError | void, string>({
            query: (id) => ({
                url: `widgets/groups/${id}`,
                method: "DELETE",
            }),
            invalidatesTags: (result, error, id) => [
                {type: 'Groups', id},
                {type: 'Groups', id: 'PARTIAL-LIST'},
            ],
        }),
    }),
    overrideExisting: false,
});

export const { useGetGroupQuery, useAddGroupsMutation, useDeleteGroupMutation, useEditGroupMutation, useGetGroupsQuery } = administrationApi;