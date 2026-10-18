import type { AxiosInstance } from 'axios';
import axios from 'axios';

const api: AxiosInstance = axios.create({
  baseURL: '/sebastian',
  headers: {
    'Content-Type': 'application/json',
  },
});

export default api;
