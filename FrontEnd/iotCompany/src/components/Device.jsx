import React, { useEffect, useState } from "react";
import { deviceService } from "../../services/deviceService";
import "./device.css";


function Device() {

//   const [componenteSeleccionado, setComponenteSeleccionado] = useState(null);
//   const [artists, setArtists] = useState([]);
//   const [customers, setCustomers] = useState([]);

//   const handleBotonClick = (componente) => {
//     setComponenteSeleccionado(componente);
//     return componenteSeleccionado;
//   };

//   useEffect(() => {
//     async function fetchUsers() {
//       try {
//         const allPersons = await adminServiceF.getAllPersons();
//         const artistas = allPersons.filter(
//           (persona) => persona.user_type === "Artist"
//         );
//         const clientes = allPersons.filter(
//           (persona) => persona.user_type === "Client"
//         );

//         setArtists(artistas);
//         setCustomers(clientes);
//       } catch (error) {
//         console.error("Error al obtener datos:", error);
//       }
//     }

//     fetchUsers();
//   }, []);

  return (
    <>
      {/* <div className="container">
        <div className="columna1">
          <button
            className="buttonA"
            onClick={() => handleBotonClick("ArtistasComponent")}
          >
            Artistas
          </button>
          <button
            className="buttonA"
            onClick={() => handleBotonClick("ClienteComponent")}
          >
            Clientes
          </button>
        </div>
        <div className="columna2">
          {componenteSeleccionado === "ArtistasComponent" && (
            <AdminArtists artists={artists} />
          )}
          {componenteSeleccionado === "ClienteComponent" && (
            <AdminCustomers customers={customers} />
          )}
        </div>
      </div> */}

      <p>device componente</p>
    </>
  );
}

export default Device;
