import { api } from "services/api";
import {CustomFetchBaseQueryError, IAddItemResponse, IPageProps, ListResponse, IItemRequest, IItemEditRequest, IItemWidget} from "shared/types";

const administrationApi = api
    .enhanceEndpoints({
        addTagTypes: ["TypesGrade"],
    })
    .injectEndpoints({
    endpoints: (build) => ({
        getTypesGrade: build.query<ListResponse<IItemWidget>, IPageProps | undefined>({
            query: (params) => ({
                url: "widgets/type_grades",
                params,
                method: "GET",
            }),
            providesTags: (result) =>
                result
                    ? [
                        ...result.items.map(({ id }) => ({ type: "TypesGrade" as const, id })),
                        { type: 'TypesGrade', id: 'PARTIAL-LIST' },
                    ]
                    : [{ type: 'TypesGrade', id: 'PARTIAL-LIST' }],
        }),
        addTypeGrade: build.mutation<CustomFetchBaseQueryError | IAddItemResponse, IItemRequest>({
            query: (body) => ({
                url: "widgets/type_grades",
                method: "POST",
                body,
            }),
            invalidatesTags: () => [{ type: 'TypesGrade', id: 'PARTIAL-LIST' }],
        }),
        getTypeGrade: build.query<IItemWidget, string>({
            query: (id) => `widgets/type_grades/${id}`,
            providesTags: (result) => result ? [{ type: "TypesGrade" as const, id: result.id }]: [],
        }),
        editTypeGrade: build.mutation<CustomFetchBaseQueryError | void, IItemEditRequest>({
            query: ({id, name}) => ({
                url: `widgets/type_grades/${id}`,
                method: "PUT",
                body: {
                    name,
                },
            }),
            invalidatesTags: (result, error, { id }) => [
                {type: 'TypesGrade', id},
                {type: 'TypesGrade', id: 'PARTIAL-LIST'},
            ],
        }),
        deleteTypeGrade: build.mutation<CustomFetchBaseQueryError | void, string>({
            query: (id) => ({
                url: `widgets/type_grades/${id}`,
                method: "DELETE",
            }),
            invalidatesTags: (result, error, id) => [
                {type: 'TypesGrade', id},
                {type: 'TypesGrade', id: 'PARTIAL-LIST'},
            ],
        }),
    }),
    overrideExisting: false,
});

export const { useGetTypeGradeQuery, useAddTypeGradeMutation, useDeleteTypeGradeMutation, useEditTypeGradeMutation, useGetTypesGradeQuery } = administrationApi;