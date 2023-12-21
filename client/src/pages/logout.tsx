import React, {useEffect} from "react";
import {useNavigate} from "react-router-dom";
import {useAppDispatch} from 'app/hooks';
import {fetchLogout} from "entities/users";
import {getAuthToken} from "shared/config";

export const Logout = () => {
    const dispatch = useAppDispatch();
    const navigate = useNavigate();
    if (getAuthToken()) {
        dispatch(fetchLogout());
    }

    useEffect(() => {
        navigate("/login");
    }, []);
    return null;
}