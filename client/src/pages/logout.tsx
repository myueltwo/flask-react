import React, { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useLogoutMutation } from "services/api";
import { setAuthToken } from "../shared";

export const Logout: React.FC = () => {
    const [ fetchLogout, { isUninitialized } ] = useLogoutMutation();
    const navigate = useNavigate();
    if (isUninitialized) {
        fetchLogout();
        setAuthToken();
    }

    useEffect(() => {
        navigate("/login");
    }, []);
    return null;
};