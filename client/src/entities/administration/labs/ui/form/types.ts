import {IChangingForm} from "entities/administration";
import {ILabRequest} from "../../types";

export interface IChangingFormLab extends IChangingForm<ILabRequest | Omit<ILabRequest, "id">> {}