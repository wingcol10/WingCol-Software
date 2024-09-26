import React, { useState } from "react";
import "../hojas-de-estilo/registro.css";
import logocompleto from "../imagenes/WingcolName.png";
import { Link } from "react-router-dom";
import Select from 'react-select';
import { getNames, getCode } from 'country-list';
import PhoneInput from 'react-phone-number-input';
import 'react-phone-number-input/style.css';

export function Registro() {
  const [formData, setFormData] = useState({
    firstName: '',
    secondName: '',
    lastName: '',
    secondLastName: '',
    phoneNumber: '',
    gender: '',
    email: '',
    documentType: '',
    documentNumber: '',
    address: '',
    billingAddress: '',
    birthDate: '',
    password: '',
    confirmPassword: '',
    selectedCountry: null,
    profilePicture: null,
  });

  const [errorMessage, setErrorMessage] = useState('');

  const countryOptions = getNames().map(country => ({
    value: getCode(country),
    label: country // Muestra el nombre del país y su código
  }));

  
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prevState => ({
      ...prevState,
      [name]: value
    }));
  };

  const handlePhoneNumberChange = (value) => {
    setFormData(prevState => ({
      ...prevState,
      phoneNumber: value
    }));
  };

  const handleCountryChange = (selectedOption) => {
    setFormData(prevState => ({
      ...prevState,
      selectedCountry: selectedOption
    }));
  };

  const handleFileChange = (e) => {
    setFormData(prevState => ({
      ...prevState,
      profilePicture: e.target.files[0]
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (formData.password !== formData.confirmPassword) {
      setErrorMessage('Las contraseñas no coinciden');
      return;
    }
    console.log(formData);
    setErrorMessage(''); 
  };

  return (
    <form className="registro-principal" onSubmit={handleSubmit}>
      <img className="logo-completo" src={logocompleto} alt="Logo" />
      <h1>Registro de usuario</h1>

      <div className="input-box">
        <input type="text" name="firstName" placeholder="Primer nombre" pattern="[a-zA-Z]+" required onChange={handleChange} />
      </div>

      <div className="input-box">
        <input type="text" name="secondName" placeholder="Segundo nombre" pattern="[a-zA-Z]+" onChange={handleChange} />
      </div>

      <div className="input-box">
        <input type="text" name="lastName" placeholder="Primer apellido" pattern="[a-zA-Z]+" required onChange={handleChange} />
      </div>

      <div className="input-box">
        <input type="text" name="secondLastName" placeholder="Segundo apellido" pattern="[a-zA-Z]+" required onChange={handleChange} />
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

      <select name="gender" className="multiples-opciones" onChange={handleChange} required>
        <option value="">Género</option>
        <option value="hombre">Hombre</option>
        <option value="mujer">Mujer</option>
        <option value="otro">Otro</option>
      </select>

      <div className="input-box">
        <input type="email" name="email" placeholder="Correo electrónico" required onChange={handleChange} />
      </div>

      <select name="documentType" className="multiples-opciones" onChange={handleChange} required>
        <option value="">Tipo de documento</option>
        <option value="cedula">Cédula</option>
        <option value="pasaporte">Pasaporte</option>
      </select>

      <div className="input-box">
        <input type="text" name="documentNumber" placeholder="Número de documento" required onChange={handleChange} />
      </div>

      <div className="input-box">
        <input type="text" name="address" placeholder="Dirección" onChange={handleChange} />
      </div>

      <div className="input-box">
        <input type="text" name="billingAddress" placeholder="Dirección de facturación" onChange={handleChange} />
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
        <input type="password" name="password" placeholder="Contraseña" required onChange={handleChange} />
      </div>

      <div className="input-box">
        <input type="password" name="confirmPassword" placeholder="Confirmar contraseña" required onChange={handleChange} />
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
