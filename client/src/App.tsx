import React from 'react';
import './App.scss';
import {BrowserRouter as Router, Routes, Route}
    from 'react-router-dom';
import NavbarHeader from "./components/Navbar/Navbar";
import About from "./pages/about";
import Account from "./pages/account";
import Home from "./pages";
import {Login} from "pages/login";

function App() {
    return (
        <Router>
            <NavbarHeader/>
            <Routes>
                <Route index={false} path='/' element={<Home/>}/>
                <Route path='/about' element={<About/>}/>
                <Route path='/account' element={<Account/>}/>
                <Route path='/login' element={<Login/>}/>
            </Routes>
        </Router>
    );
}

export default App;
