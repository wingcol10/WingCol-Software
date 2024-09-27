import React, { useState } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { Formulario } from "./componentes/inicio-de-sesion";
import { Home } from "./componentes/home";
import { Registro } from "./componentes/registro";

export default function App() {
  const [user, setUser] = useState(null); // Inicializa el estado

  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<Formulario setUser={setUser} />} />
          <Route
            path="/home"
            element={<Home user={user} setUser={setUser} />}
          />{" "}
          {/* Pasando setUser aquí */}
          <Route path="/registro" element={<Registro />} />
        </Routes>
      </div>
    </Router>
  );
}
