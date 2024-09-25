import React from "react";
import "../hojas-de-estilo/home.css";

export function Home({ user, setUser }) {
  const handleLogout = () => {
    setUser([]);
  };

  return (
    <div className="home">
      <h1>Bienvenido, estamos trabajando en la pagina</h1>
      <h2>{user}</h2>
      <button onClick={handleLogout}>Cerrar sesión</button>
    </div>
  );
}
