import React from "react";

export interface IProtectedRoute {
    redirectPath?: string;
    children?: React.ReactNode;
}