import React, { useState } from "react";
import "../hojas-de-estilo/registro.css";
import logocompleto from "../imagenes/WingcolName.png";
import { Link } from "react-router-dom";
import Select from "react-select";
import { getNames, getCode } from "country-list";
import PhoneInput from "react-phone-number-input";
import "react-phone-number-input/style.css";

export function Registro() {
  const [formData, setFormData] = useState({
    firstName: "",
    secondName: "",
    lastName: "",
    secondLastName: "",
    phoneNumber: "",
    gender: "",
    email: "",
    documentType: "",
    documentNumber: "",
    address: "",
    billingAddress: "",
    birthDate: "",
    password: "",
    confirmPassword: "",
    selectedCountry: null,
    profilePicture: null,
  });

  const [errorMessage, setErrorMessage] = useState("");

  const countryOptions = getNames().map((country) => ({
    value: getCode(country),
    label: country, // Muestra el nombre del país y su código
  }));
  const [documentPattern, setDocumentPattern] = useState("");

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevState) => ({
      ...prevState,
      [name]: value,
    }));
  };

  const handleDocumentTypeChange = (e) => {
    const { value } = e.target;
    setFormData((prevState) => ({
      ...prevState,
      documentType: value,
    }));

    // Actualizar el patrón según el tipo de documento seleccionado
    if (value === "cedula") {
      setDocumentPattern("^[0-9]+$"); // Solo números
    } else if (value === "pasaporte") {
      setDocumentPattern("^[A-Za-z]{3}[0-9]{6}$"); // 3 letras y 6 números
    } else {
      setDocumentPattern(""); // Vacío si no hay selección
    }
  };

  const handlePhoneNumberChange = (value) => {
    setFormData((prevState) => ({
      ...prevState,
      phoneNumber: value,
    }));
  };

  const handleCountryChange = (selectedOption) => {
    setFormData((prevState) => ({
      ...prevState,
      selectedCountry: selectedOption,
    }));
  };

  const handleFileChange = (e) => {
    setFormData((prevState) => ({
      ...prevState,
      profilePicture: e.target.files[0],
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (formData.password !== formData.confirmPassword) {
      setErrorMessage("Las contraseñas no coinciden");
      return;
    }

    setErrorMessage("");

    const dataToSend = {
      firstName: formData.firstName,
      secondName: formData.secondName,
      lastName: formData.lastName,
      secondLastName: formData.secondLastName,
      phoneNumber: formData.phoneNumber,
      gender: formData.gender,
      email: formData.email,
      documentType: formData.documentType,
      documentNumber: formData.documentNumber,
      address: formData.address,
      billingAddress: formData.billingAddress,
      birthDate: formData.birthDate,
      password: formData.password,
      // Si quieres incluir la foto de perfil, necesitarías usar FormData
      // profilePicture: formData.profilePicture,
      // selectedCountry: formData.selectedCountry, // Si también lo necesitas
    };

    try {
      const response = await fetch("http://tu-backend-url/api/register/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(dataToSend),
      });

      if (!response.ok) {
        const errorData = await response.json();
        setErrorMessage(errorData.message || "Error al registrar el usuario.");
        return;
      }

      // Si el registro es exitoso, puedes redirigir al usuario o mostrar un mensaje
      console.log("Usuario registrado exitosamente.");
      // Redireccionar o mostrar un mensaje de éxito aquí
    } catch (error) {
      console.error(error);
      setErrorMessage("Hubo un problema con el registro. Intenta más tarde.");
    }
  };

  return (
    <form className="registro-principal" onSubmit={handleSubmit}>
      <img className="logo-completo" src={logocompleto} alt="Logo" />
      <h1>Registro de usuario</h1>

      <div className="input-box">
        <input
          type="text"
          name="firstName"
          placeholder="Primer nombre"
          pattern="[a-zA-Z]+"
          required
          maxLength={50}
          onChange={handleChange}
        />
      </div>

      <div className="input-box">
        <input
          type="text"
          name="secondName"
          placeholder="Segundo nombre"
          pattern="[a-zA-Z]+"
          maxLength={50}
          onChange={handleChange}
        />
      </div>

      <div className="input-box">
        <input
          type="text"
          name="lastName"
          placeholder="Primer apellido"
          maxLength={50}
          pattern="[a-zA-Z]+"
          required
          onChange={handleChange}
        />
      </div>

      <div className="input-box">
        <input
          type="text"
          name="secondLastName"
          placeholder="Segundo apellido"
          maxLength={50}
          pattern="[a-zA-Z]+"
          required
          onChange={handleChange}
        />
      </div>

      <div className="input-box">
        <PhoneInput
          international
          countryCallingCodeEditable={false}
          value={formData.phoneNumber}
          onChange={handlePhoneNumberChange}
          placeholder="Número de teléfono"
          maxLength={18}
          required
        />
      </div>

      <select
        name="gender"
        className="multiples-opciones"
        onChange={handleChange}
        required
      >
        <option value="">Género</option>
        <option value="hombre">Hombre</option>
        <option value="mujer">Mujer</option>
        <option value="otro">Otro</option>
      </select>

      <div className="input-box">
        <input
          type="email"
          name="email"
          placeholder="Correo electrónico"
          required
          maxLength={50}
          onChange={handleChange}
        />
      </div>

      <select
        name="documentType"
        className="multiples-opciones"
        onChange={handleDocumentTypeChange}
        required
      >
        <option value="">Tipo de documento</option>
        <option value="cedula">Cédula</option>
        <option value="pasaporte">Pasaporte</option>
      </select>

      <div className="input-box">
        <input
          type="text"
          name="documentNumber"
          placeholder="Número de documento"
          pattern={documentPattern}
          minLength={10}
          required
          onChange={handleChange}
          title={
            formData.documentType === "cedula"
              ? "Solo números"
              : "3 letras y 6 números"
          }
        />
      </div>

      <div className="input-box">
        <input
          type="text"
          name="address"
          placeholder="Dirección"
          maxLength={50}
          onChange={handleChange}
        />
      </div>

      <div className="input-box">
        <input
          type="text"
          name="billingAddress"
          placeholder="Dirección de facturación"
          maxLength={50}
          onChange={handleChange}
        />
      </div>

      <div className="input-box">
        <input
          className="fecha-nacimiento"
          type="date"
          name="birthDate"
          min={"1940-01-01"}
          max={"2006-12-31"}
          required
          onChange={handleChange}
        />
      </div>

      <div className="input-box">
        <input
          type="password"
          name="password"
          placeholder="Contraseña"
          maxLength={15}
          required
          onChange={handleChange}
        />
      </div>

      <div className="input-box">
        <input
          type="password"
          name="confirmPassword"
          placeholder="Confirmar contraseña"
          maxLength={15}
          required
          onChange={handleChange}
        />
      </div>

      <div className="selector-paises">
        <Select
          value={formData.selectedCountry}
          onChange={handleCountryChange}
          options={countryOptions}
          placeholder="Seleccionar país de nacimiento."
          isSearchable={true}
          className="react-select-container"
          classNamePrefix="react-select"
        />
      </div>

      <div className="error">
        {errorMessage && <p className="error-message">{errorMessage}</p>}
      </div>

      <div className="foto-de-perfil">
        <label htmlFor="file">Elija una imagen de perfil </label>
        <input type="file" accept="image/*" onChange={handleFileChange} />
      </div>

      <div className="boton-registro">
        <button type="submit">Registrarse</button>
      </div>
    </form>
  );
}
