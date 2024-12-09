<template>
    <div class="form-group">
      <label :for="id">{{ label }}</label>
      <input
        v-if="type !== 'textarea'"
        min="0"
        :type="type"
        :step="step"
        :id="id"
        :value="modelValue" 
        @input="$emit('update:modelValue', $event.target.value)"  
        :placeholder="placeholder"
        :required="required"
      />
      <textarea
        v-else
        :id="id"
        :value="modelValue" 
        @input="$emit('update:modelValue', $event.target.value)"  
        :placeholder="placeholder"
        :required="required"
      ></textarea>
    </div>
  </template>
  
  <script>
  export default {
    name: 'InputComponent',
    props: {
      label: {
        type: String,
        required: true,
      },
      id: {
        type: String,
        required: true,
      },
      type: {
        type: String,
        default: 'text', // Default to text input
      },
      step: {
        type: String,
        default: 'text', // Default to text input
      },
      modelValue: {
        type: [String, Number],
        required: true,
      },
      placeholder: {
        type: String,
        default: '',
      },
      required: {
        type: Boolean,
        default: false,
      },
    },
  };
  </script>
  
  <style scoped>
  .form-group {
    margin-bottom: 15px;
  }
  
  label {
    display: block;
    margin-bottom: 5px;
    font-weight: 600;
  }
  
  input,
  textarea {
    width: 100%;
    padding: 8px;
    border-radius: 4px;
    border: 1px solid #ccc;
  }
  
  textarea {
    resize: vertical;
    min-height: 100px;
  }
  
  input:focus,
  textarea:focus {
    border-color: #80bdff;
    box-shadow: 0 0 5px rgba(0, 123, 255, 0.5);
  }
  </style>
  