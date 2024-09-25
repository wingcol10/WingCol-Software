import React from "react";
import "../hojas-de-estilo/inicio-de-sesion.css";
import { useState } from "react";
import { FaRegUserCircle } from "react-icons/fa";
import { FaLock } from "react-icons/fa";
import { Link } from "react-router-dom";
import axios from "axios";
import logo from "../imagenes/logo.png";

export function Formulario({ setUser }) {
  // State para el usuario
  const [usuario, setUsuario] = useState("");
  const [contraseña, setContraseña] = useState("");
  const [error, setError] = useState(false);

  // Función para manejar el submit
  const handleSubmit = (e) => {
    e.preventDefault();
    if (usuario === "" || contraseña === "") {
      setError(true);
      return;
    }

    setError(false);

    setUser([usuario]);
  };

  const obtenerDatos = () => {
    return axios.get("").then((response) => response.data);
  };

  // Retorno del componente
  return (
    <section>
      <form className="formulario" onSubmit={handleSubmit}>
        <img className="imagen-logo" src={logo} alt="Logo" />
        <h1>Iniciar sesión</h1>
        <div className="input-box">
          <input
            type="email"
            placeholder="Usuario"
            required
            value={usuario}
            onChange={(e) => setUsuario(e.target.value)}
          />
          <FaRegUserCircle className="icono" />
        </div>
        <div className="input-box">
          <input
            type="password"
            placeholder="Contraseña"
            required
            value={contraseña}
            onChange={(e) => setContraseña(e.target.value)}
          />
          <FaLock className="icono" />
        </div>
        <div className="recordar-contraseña">
          <a href="#">¿Olvidaste tu contraseña?</a>
        </div>
        <button>Iniciar sesión</button>
        <div className="link-registrarse">
          <p>
            ¿No tienes ninguna cuenta?{" "}
            <Link to="/registro" variant="#">
              Registrarse
            </Link>
          </p>
        </div>
        {error && <p>Todos los campos son obligatorios</p>}
      </form>
    </section>
  );
}
