import "./App.css";
import React from "react";
import ReactDOM from "react-dom/client";
import {BrowserRouter} from 'react-router-dom'
import { Routes } from 'react-router'
import Device from "./components/Device";


ReactDOM.createRoot(document.getElementById("root")).render(
  
    <BrowserRouter>
        <Routes>
        <Route path="/device" element={<Device/>} />

          {/* <Route path="/" element={<User />} />
          <Route path="/admin" element={<Home/>} /> */}


        </Routes>
      </BrowserRouter>
)