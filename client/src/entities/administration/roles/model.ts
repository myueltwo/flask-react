import { api } from "services/api";
import {CustomFetchBaseQueryError, IAddItemResponse, IPageProps, ListResponse, IItemRequest, IItemEditRequest, IItemWidget} from "shared/types";

const administrationApi = api
    .enhanceEndpoints({
        addTagTypes: ["Roles"],
    })
    .injectEndpoints({
    endpoints: (build) => ({
        getRoles: build.query<ListResponse<IItemWidget>, IPageProps | undefined>({
            query: (params) => ({
                url: "widgets/roles",
                params,
                method: "GET",
            }),
            providesTags: (result) =>
                result
                    ? [
                        ...result.items.map(({ id }) => ({ type: "Roles" as const, id })),
                        { type: 'Roles', id: 'PARTIAL-LIST' },
                    ]
                    : [{ type: 'Roles', id: 'PARTIAL-LIST' }],
        }),
        addRole: build.mutation<CustomFetchBaseQueryError | IAddItemResponse, IItemRequest>({
            query: (body) => ({
                url: "widgets/roles",
                method: "POST",
                body,
            }),
            invalidatesTags: () => [{ type: 'Roles', id: 'PARTIAL-LIST' }],
        }),
        getRole: build.query<IItemWidget, string>({
            query: (id) => `widgets/roles/${id}`,
            providesTags: (result) => result ? [{ type: "Roles" as const, id: result.id }]: [],
        }),
        editRole: build.mutation<CustomFetchBaseQueryError | void, IItemEditRequest>({
            query: ({id, name}) => ({
                url: `widgets/roles/${id}`,
                method: "PUT",
                body: {
                    name,
                },
            }),
            invalidatesTags: (result, error, { id }) => [
                {type: 'Roles', id},
                {type: 'Roles', id: 'PARTIAL-LIST'},
            ],
        }),
        deleteRole: build.mutation<CustomFetchBaseQueryError | void, string>({
            query: (id) => ({
                url: `widgets/roles/${id}`,
                method: "DELETE",
            }),
            invalidatesTags: (result, error, id) => [
                {type: 'Roles', id},
                {type: 'Roles', id: 'PARTIAL-LIST'},
            ],
        }),
    }),
    overrideExisting: false,
});

export const { useGetRoleQuery, useAddRoleMutation, useDeleteRoleMutation, useEditRoleMutation, useGetRolesQuery } = administrationApi;