import axios from 'axios';

const API_URL = 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const menuAPI = {
  // Obtener todas las categorias
  getCategories: () => api.get('/categories/'),
  
  // Obtener todos los productos
  getProducts: () => api.get('/products/'),
  
  // Obtener productos por categoria
  getProductsByCategory: () => api.get('/products/by_category/'),
  
  // Crear un nuevo pedido
  createOrder: (orderData) => api.post('/orders/', orderData),
  
  // Obtener un pedido especifico
  getOrder: (orderId) => api.get(`/orders/${orderId}/`),
  
  // Obtener todos los pedidos
  getOrders: () => api.get('/orders/'),
};

export default api;
