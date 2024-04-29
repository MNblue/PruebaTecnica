import axios from "axios";

const apiClient = axios.create({
    baseURL: 'http://localhost:5000/',
    withCredentials: false,
    headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
        // 'Access-Control-Allow-Origin': '*'
    }
});

export const wharehouseService = {

    async getAllWharehouse() {
        try {
            let response = await apiClient.get("/wharehouse");
            return response.data;
        } catch (error) {
            console.error("Error al obtener elementos del almacen:", error);
            throw error;
        }
    }
}