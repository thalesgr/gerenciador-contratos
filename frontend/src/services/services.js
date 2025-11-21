import axios from 'axios';

const BASE_URL =
  window.location.hostname === 'localhost'
    ? 'http://localhost:5000'
    : 'https://flask-contracts-36130776084.us-central1.run.app';


export const getContracts = async (filters = {}) => {
    const url =  `${BASE_URL}/contracts`

    const params = new URLSearchParams();

    Object.entries(filters).forEach(([key, value]) => {
        if (value !== '' && value !== undefined && value !== null) {
            params.append(key, value);
        }
    });

    const fullUrl = params.toString() ? `${url}?${params.toString()}` : url;

    try {
        const response = await axios.get(fullUrl);
        return response.data;
    } catch (error) {
        console.error("Error fetching contracts:", error);
        throw error;
    }
}

export const getContractById = async (id) => {
    const url = `${BASE_URL}/contracts/${id}`;
    try {
        const response = await axios.get(url);
        return response.data;
    } catch (error) {
        console.error(`Error fetching contract with id ${id}:`, error);
        throw error;
    }
}

export const saveContract = async (contract) => {
    const url = contract.id ? `${BASE_URL}/contracts/${contract.id}` : `${BASE_URL}/contracts`;
    try {
        if (contract.id) {
            // Update existing contract
            const response = await axios.put(url, contract);
            return response.data;
        } else {
            // Create new contract
            const response = await axios.post(url, contract);
            return response.data;
        }
    } catch (error) {
        console.error("Error saving contract:", error);
        throw error;
    }
}

export const deleteContract = async (id) => {
    const url = `${BASE_URL}/contracts/${id}`;
    try {
        await axios.delete(url);
    } catch (error) {
        console.error(`Error deleting contract with id ${id}:`, error);
        throw error;
    }
}