import { api } from "services/api";
import {CustomFetchBaseQueryError, IAddItemResponse, IPageProps, ListResponse, IItemRequest, IItemEditRequest, IItemWidget} from "shared/types";

const administrationApi = api
    .enhanceEndpoints({
        addTagTypes: ["ActivityTypes"],
    })
    .injectEndpoints({
    endpoints: (build) => ({
        getActivityTypes: build.query<ListResponse<IItemWidget>, IPageProps | undefined>({
            query: (params) => ({
                url: "widgets/activity_type",
                params,
                method: "GET",
            }),
            providesTags: (result) =>
                result
                    ? [
                        ...result.items.map(({ id }) => ({ type: "ActivityTypes" as const, id })),
                        { type: 'ActivityTypes', id: 'PARTIAL-LIST' },
                    ]
                    : [{ type: 'ActivityTypes', id: 'PARTIAL-LIST' }],
        }),
        addActivityType: build.mutation<CustomFetchBaseQueryError | IAddItemResponse, IItemRequest>({
            query: (body) => ({
                url: "widgets/activity_type",
                method: "POST",
                body,
            }),
            invalidatesTags: () => [{ type: 'ActivityTypes', id: 'PARTIAL-LIST' }],
        }),
        getActivityType: build.query<IItemWidget, string>({
            query: (id) => `widgets/activity_type/${id}`,
            providesTags: (result) => result ? [{ type: "ActivityTypes" as const, id: result.id }]: [],
        }),
        editActivityType: build.mutation<CustomFetchBaseQueryError | void, IItemEditRequest>({
            query: ({id, name}) => ({
                url: `widgets/activity_type/${id}`,
                method: "PUT",
                body: {
                    name,
                },
            }),
            invalidatesTags: (result, error, { id }) => [
                {type: 'ActivityTypes', id},
                {type: 'ActivityTypes', id: 'PARTIAL-LIST'},
            ],
        }),
        deleteActivityType: build.mutation<CustomFetchBaseQueryError | void, string>({
            query: (id) => ({
                url: `widgets/activity_type/${id}`,
                method: "DELETE",
            }),
            invalidatesTags: (result, error, id) => [
                {type: 'ActivityTypes', id},
                {type: 'ActivityTypes', id: 'PARTIAL-LIST'},
            ],
        }),
    }),
    overrideExisting: false,
});

export const { useGetActivityTypeQuery, useAddActivityTypeMutation, useDeleteActivityTypeMutation, useEditActivityTypeMutation, useGetActivityTypesQuery } = administrationApi;