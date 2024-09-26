import React, { useState } from "react";
import "../hojas-de-estilo/inicio-de-sesion.css";
import { FaRegUserCircle } from "react-icons/fa";
import { FaLock } from "react-icons/fa";
import { Link, useNavigate } from "react-router-dom";
import logo from "../imagenes/logo.png";

export function Formulario({ setUser }) {
  // State para el usuario y la contraseña
  const [usuario, setUsuario] = useState("");
  const [contraseña, setContraseña] = useState("");
  const [error, setError] = useState(""); // Cambiado a cadena para mostrar mensajes específicos

  // useNavigate para redireccionar después del inicio de sesión exitoso
  const navigate = useNavigate();

  // Función para manejar el submit
  const handleSubmit = async (e) => {
    e.preventDefault();
    if (usuario === "" || contraseña === "") {
      setError("Todos los campos son obligatorios");
      return;
    }

    try {
      // Enviar la solicitud al backend utilizando fetch
      const response = await fetch("http://tu-backend-url/api/login/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          email: usuario,
          password: contraseña,
        }),
      });

      if (response.ok) {
        const data = await response.json();

        // Asumiendo que el backend responde con un token JWT en data.token
        const token = data.token;

        // Guardar el token en localStorage
        localStorage.setItem("token", token);

        // Asumimos que el backend también responde con un objeto de usuario (opcional)
        const user = data.user;

        // Guarda el usuario en el estado de la app
        setUser(user);

        // Redireccionar a la página principal (o la que elijas)
        navigate("/home"); // Cambia "/home" por la ruta a la que quieras redirigir al usuario
      } else {
        setError("Credenciales incorrectas, por favor intenta de nuevo.");
      }
    } catch (error) {
      console.error(error);
      setError("Hubo un problema con el inicio de sesión. Intenta más tarde.");
    }
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
        {error && <p className="error-message">{error}</p>}{" "}
        {/* Mostrar mensajes de error */}
      </form>
    </section>
  );
}
