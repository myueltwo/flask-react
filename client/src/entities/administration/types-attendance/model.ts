import { api } from "services/api";
import {CustomFetchBaseQueryError, IAddItemResponse, IPageProps, ListResponse, IItemRequest, IItemEditRequest, IItemWidget} from "shared/types";

const administrationApi = api
    .enhanceEndpoints({
        addTagTypes: ["AttendanceTypes"],
    })
    .injectEndpoints({
    endpoints: (build) => ({
        getAttendanceTypes: build.query<ListResponse<IItemWidget>, IPageProps | undefined>({
            query: (params) => ({
                url: "widgets/attendance_type",
                params,
                method: "GET",
            }),
            providesTags: (result) =>
                result
                    ? [
                        ...result.items.map(({ id }) => ({ type: "AttendanceTypes" as const, id })),
                        { type: 'AttendanceTypes', id: 'PARTIAL-LIST' },
                    ]
                    : [{ type: 'AttendanceTypes', id: 'PARTIAL-LIST' }],
        }),
        addAttendanceType: build.mutation<CustomFetchBaseQueryError | IAddItemResponse, IItemRequest>({
            query: (body) => ({
                url: "widgets/attendance_type",
                method: "POST",
                body,
            }),
            invalidatesTags: () => [{ type: 'AttendanceTypes', id: 'PARTIAL-LIST' }],
        }),
        getAttendanceType: build.query<IItemWidget, string>({
            query: (id) => `widgets/attendance_type/${id}`,
            providesTags: (result) => result ? [{ type: "AttendanceTypes" as const, id: result.id }]: [],
        }),
        editAttendanceType: build.mutation<CustomFetchBaseQueryError | void, IItemEditRequest>({
            query: ({id, name}) => ({
                url: `widgets/attendance_type/${id}`,
                method: "PUT",
                body: {
                    name,
                },
            }),
            invalidatesTags: (result, error, { id }) => [
                {type: 'AttendanceTypes', id},
                {type: 'AttendanceTypes', id: 'PARTIAL-LIST'},
            ],
        }),
        deleteAttendanceType: build.mutation<CustomFetchBaseQueryError | void, string>({
            query: (id) => ({
                url: `widgets/attendance_type/${id}`,
                method: "DELETE",
            }),
            invalidatesTags: (result, error, id) => [
                {type: 'AttendanceTypes', id},
                {type: 'AttendanceTypes', id: 'PARTIAL-LIST'},
            ],
        }),
    }),
    overrideExisting: false,
});

export const { useGetAttendanceTypeQuery, useAddAttendanceTypeMutation, useDeleteAttendanceTypeMutation, useEditAttendanceTypeMutation, useGetAttendanceTypesQuery } = administrationApi;