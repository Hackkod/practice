import axios from 'axios';

const API_URL = 'http://localhost:8000/api-token-auth/';

export const login = async (username, password) => {
    try {
        const response = await axios.post(API_URL, { username, password });
        if (response.data.token) {
            localStorage.setItem('token', response.data.token);
            return response.data.token;
        }
    } catch (error) {
        console.error('Ошибка при авторизации', error);
        throw error;
    }
};

export const logout = () => {
    localStorage.removeItem('token')
}

export const getToken = () => {
    return localStorage.getItem('token');
}