import type { AxiosInstance } from 'axios';
import axios from 'axios';

const api: AxiosInstance = axios.create({
  baseURL: '/api',
  headers: {
    'Content-Type': 'application/json',
  },
});

export default api;
