<template>
  <FormComponent @submit.prevent="handleAddProduct">
    <InputComponent
      label="Nom du produit"
      id="productName"
      v-model="newProduct.nom"
      placeholder="Nom du produit"
      type="text"
      required
    />
    <InputComponent
      label="Prix"
      id="productPrix"
      v-model="newProduct.prix"
      type="number"
      step="any"
      placeholder="Prix"
      required
      
    />
    <InputComponent
      label="Stock"
      id="productStock"
      v-model="newProduct.stock"
      type="number"
      step="1"
      placeholder="Stock"
      required
    />
    <InputComponent
      label="Description"
      id="productDescription"
      v-model="newProduct.description"
      type="textarea"
      placeholder="Description"
      
    />
  </FormComponent>
</template>

<script>
import { useProductStore } from '../../stores/productStore'; // Adjust path as needed
import FormComponent from '../common/CommonForm.vue';
import InputComponent from '../common/InputField.vue';

export default {
  name: 'ProductCreate',
  components: { FormComponent, InputComponent },
  data() {
    return {
      newProduct: {
        nom: '',
        description: '',
        prix: 0,
        stock: 0,
      },
    };
  },
  methods: {
    async handleAddProduct() {
      const productStore = useProductStore();
      try {
        await productStore.addProduct({ ...this.newProduct });
        this.resetForm();
        this.$emit('closeModal');
      } catch (error) {
        console.error('Error adding product:', error);
      }
    },
    resetForm() {
      this.newProduct = {
        nom: '',
        description: '',
        prix: 0,
        stock: 0,
      };
    },
  },
};
</script>
