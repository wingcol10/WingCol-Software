import React from "react";
import "../hojas-de-estilo/home.css";
import { Link } from "react-router-dom";

export function Home({ user, setUser }) {
  const handleLogout = () => {
    setUser([]); // Aquí es donde se produce el error si setUser no es una función
  };

  return (
    <div className="home">
      <h1>Bienvenido, estamos trabajando en la pagina</h1>
      <h2>{user.name}</h2> {/* Accediendo al nombre del usuario */}
      <Link to={"/"}>
        <button onClick={handleLogout}>Cerrar sesión</button>
      </Link>
    </div>
  );
}
