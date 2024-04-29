import React, { useEffect, useState } from "react";
import { industryService } from "../../services/industryService";
import "./industry.css";


function Industry() {

    const [listIndustry, setListIndustry] = useState([]);


    useEffect(() => {
        async function fetchIndustry() {
            try {
                const allIndustry = await industryService.getAllIndustry();
                setListIndustry(allIndustry);
            } catch (error) {
                console.error("Error al obtener datos:", error);
            }
        }

        fetchIndustry();
    }, []);

    return (
        <>
            <div>
                <h1>Lista de Industrias</h1>
                <table>
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Nombre de la industria</th>
                        </tr>
                    </thead>
                    <tbody>
                        {listIndustry.map((innerArray, index) => (
                            <tr key={index}>
                                {innerArray.map((industry, industryIndex) => (
                                    <td key={industryIndex}>{industry}</td>
                                ))}
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>


        </>
    );
}

export default Industry;
