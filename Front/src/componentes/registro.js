import React, { useState } from "react";
import "../hojas-de-estilo/registro.css";
import logocompleto from "../imagenes/WingcolName.png";
import { Link } from "react-router-dom";

export function Registro() {
  return (
    <form className="registro-principal">
      <img className="logo-completo" src={logocompleto} alt="Logo" />
      <h1>Registro</h1>
      <div className="input-box">
        <input type="text" placeholder="Primer nombre" required />
      </div>

      <div className="input-box">
        <input type="text" placeholder="Segundo nombre" />
      </div>

      <div className="input-box">
        <input type="text" placeholder="Primer apellido" required />
      </div>

      <div className="input-box">
        <input type="text" placeholder="Segundo apellido" required />
      </div>

      <div className="input-box">
        <input
          type="tel"
          placeholder="Número de teléfono"
          minLength={10}
          maxLength={10}
          required
        />
      </div>

      <select className="multiples-opciones">
        <option>Genero</option>
        <option value="hombre">Hombre</option>
        <option value="mujer">Mujer</option>
        <option value="otro">Otro</option>
      </select>

      <div className="input-box">
        <input type="email" placeholder="Correo electrónico" required />
      </div>

      <select className="multiples-opciones">
        <option>Tipo de documento</option>
        <option value="cedula">Cédula</option>
        <option value="pasaporte">Pasaporte</option>
      </select>

      <div className="input-box">
        <input type="text" placeholder="Número de documento" required />
      </div>

      <div className="input-box">
        <input type="text" placeholder="Dirección" />
      </div>

      <div className="input-box">
        <input type="text" placeholder="Dirección de facturación" />
      </div>

      <div className="input-box">
        <input
          className="fecha-nacimiento"
          type="date"
          min={"1940-01-01"}
          max={"2006-12-31"}
          placeholder="Fecha de nacimiento"
          required
        />
      </div>

      <div className="input-box">
        <input type="password" placeholder="Contraseña" required />
      </div>

      <div className="input-box">
        <input type="password" placeholder="Confirmar contraseña" required />
      </div>

      <div className="boton-registro">
        <Link to="/">
          <button type="submit">Registrarse</button>
        </Link>
      </div>
    </form>
  );
}
