import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import PaginaInicial from './pages/Pagina Inicial';
import Produto from './pages/Produto';
import Login from './pages/Login';

export default function App() {
  return (
    <Router>
      <Routes >
        <Route exact path="/" component={PaginaInicial} />
        <Route path="/produto" component={Produto} />
        <Route path="/login" component={Login} />
      </Routes >
    </Router>
  );
};