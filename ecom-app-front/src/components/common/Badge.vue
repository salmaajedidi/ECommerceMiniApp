<template>
    <span
      class="badge availability-badge"
      :class="[type, customClasses]"
    >
      {{ label }}
    </span>
  </template>
  
  <script>
  export default {
    name: 'Badge',
    props: {
      label: {
        type: String,
        required: true,
      },
      type: {
        type: String,
        default: 'default',
        validator: (value) => ['success', 'danger', 'default'].includes(value),
      },
      customClasses: {
        type: String,
        default: '',
      },
    },
  };
  </script>
  
  <style scoped>
  .availability-badge {
    float: right;
    font-size: 12px;
    padding: 5px 8px;
    border-radius: 12px;
    font-weight: 500;
  }
  
  .badge.success {
    background-color: #28a745;
    color: #fff;
  }
  
  .badge.danger {
    background-color: #dc3545;
    color: #fff;
  }
  
  .badge.default {
    background-color: #6c757d;
    color: #fff;
  }
  </style>
  