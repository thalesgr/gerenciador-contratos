import './App.css';
import Header from './components/Header';
import Contract from './pages/Contract';
import Home from './pages/Home';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';

function App() {
  return (
    <Router>
      <nav className="navbar navbar-expand-lg navbar-light bg-light mb-4">
        <div className="container">
          <Link className="navbar-brand" to="/">Gestão de Contratos</Link>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav ms-auto">
              <li className="nav-item">
                <Link className="nav-link" to="/">Home</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/contracts/new">Novo Contrato</Link>
              </li>
            </ul>
          </div>
        </div>
      </nav>
      <Header />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/contracts/new" element={<Contract />} />
        <Route path="/contracts/:id" element={<Contract />} />
      </Routes>
    </Router>
  );
}

export default App;
