import React from 'react';
import './App.scss';
import {BrowserRouter as Router, Routes, Route}
    from 'react-router-dom';
import About from "pages/about";
import Account from "pages/account";
import Home from "pages";
import {Login} from "pages/login";
import {Logout} from "pages/logout";
import { ProtectedRoute, NavbarHeader } from "shared/ui";

function App() {
    return (
        <Router>
            <NavbarHeader/>
            <Routes>
                <Route index={false} path='/' element={<Home/>}/>
                <Route path='/about' element={<About/>}/>
                <Route path='/login' element={<Login/>}/>
                <Route path='/logout' element={<Logout/>}/>
                <Route element={<ProtectedRoute/>}>
                    <Route path='/account' element={<Account/>}/>
                </Route>
            </Routes>
        </Router>
    );
}

export default App;
