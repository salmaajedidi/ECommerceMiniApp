<template>
    <div class="filter-container">
      <label :for="id">{{ label }}</label>
      <select :id="id" @change="onFilterChange" v-model="selectedOption">
        <option 
          v-for="option in options" 
          :key="option.value" 
          :value="option.value">
          {{ option.label }}
        </option>
      </select>
    </div>
  </template>
  
  <script>
  export default {
    name: 'GenericFilter',
    props: {
      id: {
        type: String,
        required: true,
      },
      label: {
        type: String,
        default: 'Filter',
      },
      options: {
        type: Array,
        required: true,
      },
    },
    emits: ['filter-change'],
    data() {
      return {
        selectedOption: '', 
      };
    },
    methods: {
      onFilterChange() {
        this.$emit('filter-change', this.selectedOption);
      },
    },
  };
  </script>
  
  <style scoped>
  .filter-container {
    margin-bottom: 15px;
    display: flex;
    align-items: center;
    gap: 10px;
  }
  
  .filter-container label {
    font-weight: bold;
  }
  
  .filter-container select {
    padding: 5px 10px;
    border-radius: 5px;
    border: 1px solid #ced4da;
  }
  </style>
  