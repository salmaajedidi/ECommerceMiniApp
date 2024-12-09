<template>
  <tr class="product-row">

    <td>
      <span class="product-name">{{ product.nom }}</span>
      <Badge 
        :label="product.stock > 0 ? 'En Stock' : 'Hors Stock'" 
        :type="product.stock > 0 ? 'success' : 'danger'" 
      />
    </td>

    <td>{{ product.description }}</td>

    <td>{{ product.prix }} TND</td>

    <td class="adjust-cell">
      <CounterInput
        v-model="product.stock"
        :min="0"
        @update:modelValue="updateStock"
      />
    </td>

    <td class="adjust-cell">
      <CommonButton
        customClasses="btn-delete"
        @click="openDeleteModal"
      >
        <i class="fa fa-trash"></i>
      </CommonButton>
    </td>
  </tr>

  <GenericModal
      :showModal="showModal"
      :hideActions="hideActions"
      title="Confirmer la suppression"
      confirmText="Oui, supprimer"
      cancelText="Annuler"
      confirmType="button"
      cancelType="button"
      @close="closeModal"
      @confirm="confirmDelete"
     
    >
      <p>Êtes-vous sûr de vouloir supprimer ce produit ?</p>
    </GenericModal>
</template>

<script>
import Badge from '../common/Badge.vue';
import CounterInput from '../common/CounterInput.vue';
import CommonButton from '../common/CommonButton.vue';
import GenericModal from '../common/GenericModal.vue';

export default {
  name: 'ProductTableRow',
  components: { Badge, CounterInput, CommonButton, GenericModal },
  props: {
    product: Object,
  },
  emits: ['delete', 'update-stock'],
  data() {
    return {
      showModal: false,
      hideActions: true,
    };
  },
  methods: {
    updateStock(newStock) {
      this.$emit('update-stock', this.product.id, newStock);
    },

    openDeleteModal() {
      this.showModal = true;
    },
    closeModal() {
      this.showModal = false;
    },
    confirmDelete() {
      this.$emit('delete', this.product.id);
      this.closeModal();
    },
  },
};
</script>

<style scoped>
/* Table Row Styling */
.product-row {
  font-size: 16px;
  background-color: #f8f9fa;
  transition: background-color 0.3s;
  vertical-align: middle;
}

.product-row:hover {
  background-color: #f1f3f5;
}

/* Product Name and Badge */
.product-name {
  font-weight: 600;
  color: #343a40;
}

/* Stock Cell Styling */
.adjust-cell {
  white-space: nowrap;
  width: 1%;
  text-align: center;
  padding-left: 20px;
  padding-right: 20px;
}

/* Delete Button */
.btn-delete {
  color: #fff!important;
  font-size: 16px!important;
  display: inline-flex!important;
  padding: 8px 10px!important;
  border-radius: 25%!important;
  background: #e74c3c!important;
  box-shadow: 0px 0px 10px rgba(197, 197, 197, 0.4)!important;
  border: none!important;
}
</style>



