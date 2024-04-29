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

export const industryService = {

    async getAllIndustry() {
        try {
            let response = await apiClient.get("/industry");
            return response.data;
        } catch (error) {
            console.error("Error al obtener las industrias:", error);
            throw error;
        }
    }
}