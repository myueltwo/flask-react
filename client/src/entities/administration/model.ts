import { api } from "services/api";
import {ISubject, ISubjectRequest} from "./types";
import {IPageProps, ListResponse} from "shared/types";

const administrationApi = api.injectEndpoints({
    endpoints: (build) => ({
        getSubjects: build.query<ListResponse<ISubject>, IPageProps | void>({
            query: (body) => ({
                url: "widgets/subjects",
                body,
            }),
            // provideTags: (result) =>
            //     result ? [
            //         ...result.items.map({})
            //     ]
        }),
        addSubject: build.mutation<void, ISubjectRequest>({
            query: ({numberHours, name}) => ({
                url: "widgets/subjects",
                method: "POST",
                body: {
                    count_hours: numberHours,
                    name,
                },
            }),
        }),
    }),
    overrideExisting: false,
});

export const { useGetSubjectsQuery, useAddSubjectMutation } = administrationApi;