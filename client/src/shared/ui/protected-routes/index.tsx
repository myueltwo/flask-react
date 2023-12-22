import React, { useEffect } from "react";
import {
  Navigate,
  Outlet,
} from 'react-router-dom';
import { useAppSelector, useAppDispatch } from 'app/hooks';
import { selectCurrentUser, selectCurrentUserPending, fetchUser } from "entities/users";
import {IProtectedRoute} from "./types";

export const ProtectedRoute: React.FC<IProtectedRoute> = ({
  redirectPath = '/login',
}) => {
  const dispatch = useAppDispatch();
  const user = useAppSelector(selectCurrentUser);
  const userPending = useAppSelector(selectCurrentUserPending);

  useEffect(() => {
    if (userPending === "idle") {
      dispatch(fetchUser());
    }
  }, []);

  if (["idle", "loading"].includes(userPending)) {
    return null;
  }

  if (!user && userPending === "succeeded" || userPending === "failed") {
    return <Navigate to={redirectPath} replace />;
  }

  return <Outlet />;
};
