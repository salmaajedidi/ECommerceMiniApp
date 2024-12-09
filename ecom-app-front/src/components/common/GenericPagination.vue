<template>
    <div class="pagination-controls">
      <CommonButton
        :tag="'button'"
        :type="'button'"
        :customClasses="'pagination-button'"
        @click="prevPage"
        :disabled="currentPage === 1"
      >
        <
      </CommonButton>
      
      <span>Page {{ currentPage }} sur {{ totalPages }}</span>
      
      <CommonButton
        :tag="'button'"
        :type="'button'"
        :customClasses="'pagination-button'"
        @click="nextPage"
        :disabled="currentPage === totalPages"
      >
        >
      </CommonButton>
    </div>
  </template>
  
  <script>
  import { ref, computed } from 'vue';
  import CommonButton from './CommonButton.vue'; // Assuming CommonButton is in the same folder
  
  export default {
    name: 'Pagination',
    components: { CommonButton },
    props: {
      totalItems: {
        type: Number,
        required: true,
      },
      itemsPerPage: {
        type: Number,
        required: true,
      },
      currentPage: {
        type: Number,
        required: true,
      },
    },
    emits: ['update:currentPage'],
    setup(props, { emit }) {
      const totalPages = computed(() => {
        return Math.ceil(props.totalItems / props.itemsPerPage);
      });
  
      const prevPage = () => {
        if (props.currentPage > 1) {
          emit('update:currentPage', props.currentPage - 1);
        }
      };
  
      const nextPage = () => {
        if (props.currentPage < totalPages.value) {
          emit('update:currentPage', props.currentPage + 1);
        }
      };
  
      return {
        totalPages,
        prevPage,
        nextPage,
      };
    },
  };
  </script>
  
  <style scoped>
  .pagination-controls {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 20px;
  }
  
  .pagination-button {
    padding: 5px 15px;
    margin: 0 10px;
    border: none;
    cursor: pointer;
  }
  
  .pagination-button:disabled {
    display: none;
  }
  </style>
  