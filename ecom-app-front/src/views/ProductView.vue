<template>
  <main>
    <div class="container mt-5">
      <!-- Title and Add Button in a Flex Container -->
      <div class="d-flex justify-content-between align-items-center mb-4 background-container">
        <div class="logo-container">
          <img src="../assets/logo.svg" alt="Logo" class="logo" />
          <h1>Liste des produits</h1>

        </div>
        <CommonButton
          @click="openAddModal"
          customClasses="btn btn-primary custom-btn"
        >
          Ajouter un produit
        </CommonButton>
      </div>

      <ProductList />
    </div>

    <GenericModal
      :showModal="showAddModal"
      :hideActions="hideActions"
      title="Ajouter un produit"
      customClasses="addmodal"
      @close="closeAddModal"
    >
      <ProductCreate @closeModal="closeAddModal"/>
    </GenericModal>
  </main>
</template>

<script setup>
import ProductList from '../components/product/ProductList.vue';
import CommonButton from '../components/common/CommonButton.vue';
</script>
<script>
import ProductCreate from '../components/product/ProductCreate.vue';
import GenericModal from '../components/common/GenericModal.vue';

export default {
  components: { GenericModal, ProductCreate, ProductList },
  data() {
    return {
      showAddModal: false,
      hideActions: false,
      newProduct: {
        nom: '',
        description: '',
        prix: 0,
        stock: 0,
      },
    };
  },
  methods: {
    openAddModal() {
      this.showAddModal = true;
    },

    closeAddModal() {
      this.showAddModal = false;
    },
    
  },
};
</script>
<style scoped>
.addmodal{
  text-align: left;
}
.logo-container {
  display: flex;
  justify-content: center;
  align-items: center;
  vertical-align: middle;
}

.logo {
  width: 40px;
  height: auto;
  margin-right: 1.1em;
  margin-bottom: 7px
}

@media (max-width: 768px) {
  .logo {
    width: 20px; 
  }
}
</style>