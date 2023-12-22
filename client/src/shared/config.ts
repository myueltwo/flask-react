import axios from "axios";

export const getAuthToken = () => localStorage.getItem("authToken") ?? "";
export const setAuthToken = (authToken?: string) => {
    const token = authToken ?? "";
    localStorage.setItem("authToken", token);
    axios.defaults.headers.common['Authorization'] = token;
};

axios.defaults.baseURL = 'http://127.0.0.1:5000/api/v1';
axios.defaults.headers.common['Authorization'] = getAuthToken();
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
axios.defaults.headers.common['Access-Control-Allow-Origin'] = 'http://127.0.0.1:5000';
