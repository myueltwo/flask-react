import React from "react";
import {
  Navigate,
  Outlet,
} from 'react-router-dom';
import { useGetCurrentUserQuery } from "services/api";
import {IProtectedRoute} from "./types";

export const ProtectedRoute: React.FC<IProtectedRoute> = ({
  redirectPath = '/login',
}) => {
  const { isUninitialized, isLoading, isError } = useGetCurrentUserQuery();

  if (isUninitialized || isLoading) {
    return null;
  } else if (isError) {
    return <Navigate to={redirectPath} replace />;
  }

  return <Outlet />;
};
