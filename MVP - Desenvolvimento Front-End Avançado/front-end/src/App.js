import React from 'react';
import { Routes, Route } from 'react-router-dom';

import PaginaInicial from './pages/PaginaInicial';
import Login from './pages/Login';
import Produto from './pages/Produto';
import PaginaNaoEncontrada from './pages/PaginaNaoEncontrada';

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<PaginaInicial />} />
      <Route path="/login" element={<Login />} />
      <Route path="/produto" element={<Produto />} />
      <Route path="*" element={<PaginaNaoEncontrada />} />
    </Routes>
  );
}
