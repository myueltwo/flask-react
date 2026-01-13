import { api } from "services/api";
import {CustomFetchBaseQueryError, IAddItemResponse, IPageProps, ListResponse, IItemRequest, IItemEditRequest, IItemWidget} from "shared/types";

const administrationApi = api
    .enhanceEndpoints({
        addTagTypes: ["ActivitySubTypes"],
    })
    .injectEndpoints({
    endpoints: (build) => ({
        getActivitySubTypes: build.query<ListResponse<IItemWidget>, IPageProps | undefined>({
            query: (params) => ({
                url: "widgets/activity_sub_type",
                params,
                method: "GET",
            }),
            providesTags: (result) =>
                result
                    ? [
                        ...result.items.map(({ id }) => ({ type: "ActivitySubTypes" as const, id })),
                        { type: 'ActivitySubTypes', id: 'PARTIAL-LIST' },
                    ]
                    : [{ type: 'ActivitySubTypes', id: 'PARTIAL-LIST' }],
        }),
        addActivitySubType: build.mutation<CustomFetchBaseQueryError | IAddItemResponse, IItemRequest>({
            query: (body) => ({
                url: "widgets/activity_sub_type",
                method: "POST",
                body,
            }),
            invalidatesTags: () => [{ type: 'ActivitySubTypes', id: 'PARTIAL-LIST' }],
        }),
        getActivitySubType: build.query<IItemWidget, string>({
            query: (id) => `widgets/activity_sub_type/${id}`,
            providesTags: (result) => result ? [{ type: "ActivitySubTypes" as const, id: result.id }]: [],
        }),
        editActivitySubType: build.mutation<CustomFetchBaseQueryError | void, IItemEditRequest>({
            query: ({id, name}) => ({
                url: `widgets/activity_sub_type/${id}`,
                method: "PUT",
                body: {
                    name,
                },
            }),
            invalidatesTags: (result, error, { id }) => [
                {type: 'ActivitySubTypes', id},
                {type: 'ActivitySubTypes', id: 'PARTIAL-LIST'},
            ],
        }),
        deleteActivitySubType: build.mutation<CustomFetchBaseQueryError | void, string>({
            query: (id) => ({
                url: `widgets/activity_sub_type/${id}`,
                method: "DELETE",
            }),
            invalidatesTags: (result, error, id) => [
                {type: 'ActivitySubTypes', id},
                {type: 'ActivitySubTypes', id: 'PARTIAL-LIST'},
            ],
        }),
    }),
    overrideExisting: false,
});

export const { useGetActivitySubTypeQuery, useAddActivitySubTypeMutation, useDeleteActivitySubTypeMutation, useEditActivitySubTypeMutation, useGetActivitySubTypesQuery } = administrationApi;