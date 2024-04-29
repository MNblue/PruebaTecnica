import React, { useEffect, useState } from "react";
import { deviceService } from "../../services/deviceService";
import "./device.css";


function Device() {

    const [listDevice, setListDevice] = useState([]);


    useEffect(() => {
        async function fetchDevices() {
            try {
                const allDevice = await deviceService.getAllDevice();
                setListDevice(allDevice);
            } catch (error) {
                console.error("Error al obtener datos:", error);
            }
        }

        fetchDevices();
    }, []);

    return (
        <>
            <div>
                <h1>Lista de Dispositivos</h1>
                <table>
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Nombre del Dispositivo</th>
                            <th>Fecha de Adición</th>
                            <th>Tarifa</th>
                        </tr>
                    </thead>
                    <tbody>
                        {listDevice.map((innerArray, index) => (
                            <tr key={index}>
                                {innerArray.map((device, deviceIndex) => (
                                    <td key={deviceIndex}>{device}</td>
                                ))}
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>


        </>
    );
}

export default Device;
