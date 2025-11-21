import axios from 'axios';

export const getContracts = async (filters = {}) => {
    const url = 'http://localhost:5000/contracts';

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
    const url = `http://localhost:5000/contracts/${id}`;
    try {
        const response = await axios.get(url);
        return response.data;
    } catch (error) {
        console.error(`Error fetching contract with id ${id}:`, error);
        throw error;
    }
}

export const saveContract = async (contract) => {
    const url = contract.id ? `http://localhost:5000/contracts/${contract.id}` : 'http://localhost:5000/contracts';
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
    const url = `http://localhost:5000/contracts/${id}`;
    try {
        await axios.delete(url);
    } catch (error) {
        console.error(`Error deleting contract with id ${id}:`, error);
        throw error;
    }
}