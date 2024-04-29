// import React, { useEffect, useState } from "react";
// import { deviceService } from "../services/deviceService";
// import "./device.css";


// function Industry() {

//     const [listIndustry, setListIndustry] = useState([]);


//     useEffect(() => {
//         async function fetchIndustry() {
//             try {
//                 const allIndustry = await deviceService.getAllIndustry();
//                 setListIndustry(allIndustry);
//             } catch (error) {
//                 console.error("Error al obtener datos:", error);
//             }
//         }

//         fetchIndustry();
//     }, []);

//     return (
//         <>
//             <div>
//                 <h1>Lista de Dispositivos</h1>
//                 <table>
//                     <thead>
//                         <tr>
//                             <th>ID</th>
//                             <th>Nombre del Dispositivo</th>
//                             <th>Fecha de Adición</th>
//                             <th>Tarifa</th>
//                         </tr>
//                     </thead>
//                     <tbody>
//                         {listIndustry.map((innerArray, index) => (
//                             <tr key={index}>
//                                 {innerArray.map((industry, industryIndex) => (
//                                     <td key={industryIndex}>{industry}</td>
//                                 ))}
//                             </tr>
//                         ))}
//                     </tbody>
//                 </table>
//             </div>


//         </>
//     );
// }

// export default Industry;
