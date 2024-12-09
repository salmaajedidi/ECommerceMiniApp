<template>
  <!-- Error message -->
  <div v-if="store.error" class="alert alert-danger">{{ store.error }}</div>

  <!-- Product List Table -->
  <div class="background-container">

    <GenericFilter 
      id="stock-filter" 
      label="Filtrer par stock:" 
      :options="filterOptions" 
      @filter-change="filterProducts" 
    />

    <table class="table table-striped">
      <thead>
        <tr>
          <th>Nom</th>
          <th>Description</th>
          <th>Prix</th>
          <th>Stock</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <ProductTableRow 
          v-for="product in paginatedProducts" 
          :key="product.id" 
          :product="product" 
          @delete="deleteProduct" 
          @update-stock="updateStock"
        />
      </tbody>
    </table>
    <!-- Pagination -->
    <Pagination 
      :totalItems="store.products.length" 
      :itemsPerPage="itemsPerPage" 
      :currentPage="currentPage" 
      @update:currentPage="updatePage" 
    />
  </div>
</template>

<script>
import { useProductStore } from '../../stores/productStore';
import { onMounted, ref, computed } from 'vue';
import ProductTableRow from './productRow.vue';
import Pagination from '../common/GenericPagination.vue'; 
import GenericFilter from '../common/Filter.vue';

export default {
  name: 'ProductList',
  components: { ProductTableRow, Pagination, GenericFilter },
  setup() {
    const store = useProductStore();
    const currentPage = ref(1);
    const itemsPerPage = 5;

    const filterOptions = [
      { value: '', label: 'Tout les produits' },
      { value: 'true', label: 'En Stock' },
      { value: 'false', label: 'Hors Stock' },
    ];

    // Fetch products on mount
    onMounted(() => {
      store.fetchProducts();
    });

    // Handle filter change
    const filterProducts = (selectedFilter) => {
      store.fetchProducts(selectedFilter);
      currentPage.value = 1; // Reset pagination on filter change
    };

    const deleteProduct = (id) => store.deleteProduct(id);
    const updateStock = (id, stock) => store.updateProductStock(id, stock);
    const updatePage = (newPage) => (currentPage.value = newPage);

    const paginatedProducts = computed(() => {
      const start = (currentPage.value - 1) * itemsPerPage;
      const end = start + itemsPerPage;
      return store.products.slice(start, end);
    });

    return {
      store,
      currentPage,
      itemsPerPage,
      paginatedProducts,
      filterOptions,
      filterProducts,
      deleteProduct,
      updateStock,
      updatePage,
    };
  },
};
</script>

<style scoped>
/* Table Header */
th {
  background-color: #3f475a; 
  color: #ffffff; 
  padding: 12px;
  text-align: left;
  font-size: 0.9rem;
  font-weight: bold;
  border-radius: 8px;
}

/* Table Row */
td {
  vertical-align: middle;
  padding: 12px;
  text-align: left;
  font-size: 1rem;
  color: #3f475a;
  border-bottom: 1px solid #f1f1f1;
}

/* Table Row Hover Effect */
tr:hover {
  background-color: #f1f1f1;
  transform: scale(1.02);
  transition: all 0.3s ease;
}

/* Even row styling */
tr:nth-child(even) {
  background-color: #f9f9f9;
}

/* Table Borders */
table, th, td {
  border: 1px solid #ddd;
  border-radius: 8px;
}

th, td {
  border-radius: 6px;
}

/* Stock Input Styling */
.stock-input {
  width: 80px;
  padding: 6px;
  font-size: 1rem;
  border: 1px solid #ced4da;
  border-radius: 5px;
  transition: border-color 0.3s;
}

.stock-input:focus {
  border-color: #80bdff;
  outline: none;
}

/* Button Styling */
button i {
  font-size: 1.25rem;
}

button {
  border: none;
  background: none;
  color: #e74c3c;
  cursor: pointer;
  transition: color 0.3s ease;
}

button:hover {
  color: #c0392b;
}

/* Responsive design: Table for smaller screens */
@media (max-width: 768px) {
  table {
    font-size: 0.9rem;
  }

  td, th {
    padding: 10px;
  }
}

</style>
