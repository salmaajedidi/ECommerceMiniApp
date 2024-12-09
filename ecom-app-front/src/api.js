import axios from 'axios';

const api = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/', // Django rest framework API base URL
  headers: {
    'Content-Type': 'application/json', 
  },
});

// Optional: Add interceptors for error handling
api.interceptors.response.use(
  response => response, 
  error => {
    console.error('API error:', error); 
    return Promise.reject(error);
  }
);

export default api;
