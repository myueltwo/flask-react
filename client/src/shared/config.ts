import axios from "axios";

axios.defaults.baseURL = 'http://127.0.0.1:5000/api/v1';
// axios.defaults.headers.common['Authorization'] = AUTH_TOKEN;
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
axios.defaults.headers.common['Access-Control-Allow-Origin'] = 'http://127.0.0.1:5000';

export const addAuthToken = (authToken: string) => {
    axios.defaults.headers.common['Authorization'] = authToken;
};