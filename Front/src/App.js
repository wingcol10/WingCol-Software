import { useState } from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate,
} from "react-router-dom";
import { Formulario } from "./componentes/inicio-de-sesion";
import { Home } from "./componentes/home";
import { Registro } from "./componentes/registro";

export default function App() {
  const [user, setUser] = useState([]);

  return (
    <Router>
      <div className="App">
        <Routes>
          <Route
            path="/"
            element={
              !user.length ? (
                <Formulario setUser={setUser} />
              ) : (
                <Navigate to="/home" replace />
              )
            }
          />
          <Route
            path="/home"
            element={
              user.length ? (
                <Home user={user} setUser={setUser} />
              ) : (
                <Navigate to="/" replace />
              )
            }
          />
          <Route path="/registro" element={<Registro />} />
        </Routes>
      </div>
    </Router>
  );
}
