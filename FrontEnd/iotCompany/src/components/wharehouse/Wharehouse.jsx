import React, { useEffect, useState } from "react";
import { wharehouseService } from "../../services/wharehouseService";
import "./wharehouse.css";


function wharehouse() {

    const [listWharehouse, setListWharehouse] = useState([]);


    useEffect(() => {
        async function fetchWharehouse() {
            try {
                const allWharehouse= await wharehouseService.getAllWharehouse();
                setListWharehouse(allWharehouse);
            } catch (error) {
                console.error("Error al obtener datos:", error);
            }
        }

        fetchWharehouse();
    }, []);

    return (
        <>
            <div>
                <h1>Almacen</h1>
                <table>
                    <thead>
                        <tr>
                            <th>Dispositivo</th>
                            <th>Industria</th>
                        </tr>
                    </thead>
                    <tbody>
                        {listWharehouse.map((innerArray, index) => (
                            <tr key={index}>
                                {innerArray.map((wharehouse, wharehouseIndex) => (
                                    <td key={wharehouseIndex}>{wharehouse}</td>
                                ))}
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>


        </>
    );
}

export default wharehouse;
