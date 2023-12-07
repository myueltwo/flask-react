import axios from "axios";
import {ILogin} from "./types";

export const loginAction = (data: ILogin) => axios.post('/auth/login', data);
