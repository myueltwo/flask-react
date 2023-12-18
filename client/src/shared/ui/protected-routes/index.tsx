import React from "react";
import {
  Navigate,
  Outlet,
} from 'react-router-dom';
import { useAppSelector } from 'app/hooks';
import { selectCurrentUser } from "entities/users";
import {IProtectedRoute} from "./types";

export const ProtectedRoute: React.FC<IProtectedRoute> = ({
  redirectPath = '/login',
  children,
}) => {
  const user = useAppSelector(selectCurrentUser);
  if (!user) {
    return <Navigate to={redirectPath} replace />;
  }

  return <Outlet />;
};
