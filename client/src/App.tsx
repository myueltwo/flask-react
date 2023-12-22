import React from 'react';
import './App.scss';
import {BrowserRouter as Router, Routes, Route}
    from 'react-router-dom';
import {
    About,
    Home,
    Login,
    Logout,
    Account,
} from "pages";
import { ProtectedRoute, NavbarHeader } from "shared/ui";

function App() {
    return (
        <Router>
            <NavbarHeader/>
            <Routes>
                <Route path='/about' element={<About/>}/>
                <Route path='/login' element={<Login/>}/>
                <Route path='/logout' element={<Logout/>}/>
                <Route element={<ProtectedRoute/>}>
                    <Route index={false} path='/' element={<Home/>}/>
                    <Route path='/account' element={<Account/>}/>
                </Route>
            </Routes>
        </Router>
    );
}

export default App;
