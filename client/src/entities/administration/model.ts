import { api } from "services/api";
import {ISubject, ISubjectRequest, ISubjectEditRequest} from "./types";
import {CustomFetchBaseQueryError, IAddItemResponse, IPageProps, ListResponse} from "shared/types";

const administrationApi = api
    .enhanceEndpoints({
        addTagTypes: ["Subjects"],
    })
    .injectEndpoints({
    endpoints: (build) => ({
        getSubjects: build.query<ListResponse<ISubject>, IPageProps | void>({
            query: (body) => ({
                url: "widgets/subjects",
                body,
            }),
            providesTags: (result) =>
                result
                    ? [
                        ...result.items.map(({ id }) => ({ type: "Subjects" as const, id })),
                        { type: 'Subjects', id: 'PARTIAL-LIST' },
                    ]
                    : [{ type: 'Subjects', id: 'PARTIAL-LIST' }],
        }),
        addSubject: build.mutation<CustomFetchBaseQueryError | IAddItemResponse, ISubjectRequest>({
            query: ({numberHours, name}) => ({
                url: "widgets/subjects",
                method: "POST",
                body: {
                    count_hours: numberHours,
                    name,
                },
            }),
            invalidatesTags: () => [{ type: 'Subjects', id: 'PARTIAL-LIST' }],
        }),
        getSubject: build.query<ISubject, string>({
            query: (id) => `widgets/subjects/${id}`,
            providesTags: (result) => result ? [{ type: "Subjects" as const, id: result.id }]: [],
        }),
        editSubject: build.mutation<CustomFetchBaseQueryError | void, ISubjectEditRequest>({
            query: ({id, numberHours, name}) => ({
                url: `widgets/subjects/${id}`,
                method: "PUT",
                body: {
                    count_hours: numberHours,
                    name,
                },
            }),
            invalidatesTags: (result, error, { id }) => [
                {type: 'Subjects', id},
                {type: 'Subjects', id: 'PARTIAL-LIST'},
            ],
        }),
        deleteSubject: build.mutation<CustomFetchBaseQueryError | void, string>({
            query: (id) => ({
                url: `widgets/subjects/${id}`,
                method: "DELETE",
            }),
            invalidatesTags: (result, error, id) => [
                {type: 'Subjects', id},
                {type: 'Subjects', id: 'PARTIAL-LIST'},
            ],
        }),
    }),
    overrideExisting: false,
});

export const { useGetSubjectsQuery, useAddSubjectMutation, useDeleteSubjectMutation, useEditSubjectMutation, useGetSubjectQuery } = administrationApi;