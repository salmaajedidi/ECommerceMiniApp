import { defineStore } from 'pinia';
import api from '../api';

export const useProductStore = defineStore('productStore', {
  state: () => ({
    products: [],
    loading: false,
    error: null,
  }),
  actions: {
    async fetchProducts(filter = null) {
      this.loading = true;
      try {
        let url = 'products/';
        if (filter) {
          url += `?in_stock=${filter}`;
        }
        const response = await api.get(url);
        this.products = response.data.reverse();
      } catch (error) {
        this.error = 'Failed to fetch products.';
      } finally {
        this.loading = false;
      }
    },
    async addProduct(product) {
      this.loading = true;
      try {

        await api.post('products/', product);
        this.fetchProducts(); // Refresh the product list
      } catch (error) {
        this.error = 'Failed to add product.';
      } finally {
        this.loading = false;
      }
    },
    async updateProductStock(id, stock) {
      this.loading = true;
      try {
        await api.put(`products/${id}`, { stock });  
        this.fetchProducts(); 
      } catch (error) {
        this.error = 'Failed to update stock.'; 
        console.error(error.response);  
      } finally {
        this.loading = false;
      }
    },
    async deleteProduct(id) {
      this.loading = true;
      try {
        await api.delete(`products/${id}`);
        this.fetchProducts(); 
      } catch (error) {
        this.error = 'Failed to delete product.';
      } finally {
        this.loading = false;
      }
    },
  },
});
