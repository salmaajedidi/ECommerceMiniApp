<template>
    <div class="counter-input-group">
      <button class="btn-decrement" @click="decrement">−</button>
      <input
        type="number"
        class="counter-input"
        v-model.number="internalValue"
        @input="updateValue"
        :min="min"
        :max="max"
      />
      <button class="btn-increment" @click="increment">+</button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'CounterInput',
    props: {
      modelValue: {
        type: Number,
        required: true,
      },
      min: {
        type: Number,
        default: 0,
      },
      max: {
        type: Number,
        default: Infinity,
      },
      step: {
        type: Number,
        default: 1,
      },
    },
    emits: ['update:modelValue'],
    data() {
      return {
        internalValue: this.modelValue,
      };
    },
    watch: {
      modelValue(newValue) {
        this.internalValue = newValue;
      },
    },
    methods: {
      updateValue() {
        this.internalValue = Math.min(Math.max(this.internalValue, this.min), this.max);
        this.$emit('update:modelValue', this.internalValue);
      },
      decrement() {
        const newValue = Math.max(this.internalValue - this.step, this.min);
        this.$emit('update:modelValue', newValue);
        this.internalValue = newValue;
      },
      increment() {
        const newValue = Math.min(this.internalValue + this.step, this.max);
        this.$emit('update:modelValue', newValue);
        this.internalValue = newValue;
      },
    },
  };
  </script>
  
  <style scoped>
  .counter-input-group {
    display: inline-flex;
    align-items: center;
  }
  
  .counter-input {
    width: 50px;
    height: 35px;
    text-align: center;
    font-size: 14px;
    font-weight: 600;
    border: 1px solid #ced4da;
    background-color: #fff;
    border-left: none;
    border-right: none;
    outline: none;
    border-radius: 0;
    transition: all 0.3s ease;
  }
  
  .counter-input:focus {
    border-color: #80bdff;
    box-shadow: 0 0 5px rgba(0, 123, 255, 0.5);
  }
  
  .btn-decrement,
  .btn-increment {
    width: 35px;
    height: 35px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    font-weight: bold;
    color: #495057;
    background-color: #e9ecef;
    border: 1px solid #ced4da;
    cursor: pointer;
    transition: all 0.3s ease;
  }
  
  .btn-decrement {
    border-top-left-radius: 5px;
    border-bottom-left-radius: 5px;
  }
  
  .btn-increment {
    border-top-right-radius: 5px;
    border-bottom-right-radius: 5px;
  }
  
  .btn-decrement:hover,
  .btn-increment:hover {
    background-color: #dee2e6;
  }

  .counter-input {
    -moz-appearance: textfield; /* Removes spinners in Firefox */
    -webkit-appearance: none; /* Removes spinners in Chrome, Safari, Edge */
    appearance: none; /* General appearance reset */
  }

  .counter-input::-webkit-inner-spin-button,
  .counter-input::-webkit-outer-spin-button {
    -webkit-appearance: none; /* Specifically targets Chrome and Safari */
    margin: 0; /* Ensures no extra spacing */
    }

  </style>
  