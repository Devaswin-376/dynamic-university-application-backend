import { useState } from 'react';
import {Route, Routes} from "react-router-dom";
import './App.css'
import Universities from "./components/Universities.jsx";
import DynamicForm from "./components/DynamicForm.jsx";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Universities />} />
      <Route path="/apply/:universityId" element={<DynamicForm />} />
    </Routes>
  );
}

export default App
