import { api } from "services/api";
import {ISubject} from "./types";
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
    }),
    overrideExisting: false,
});

export const { useGetSubjectsQuery } = administrationApi;