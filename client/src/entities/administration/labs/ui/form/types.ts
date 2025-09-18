import {IChangingForm} from "entities/administration";
import {ILab, ILabRequest} from "../../types";

export interface IChangingFormLab extends IChangingForm<ILab | Omit<ILab, "id">, ILabRequest | Omit<ILabRequest, "id">> {}