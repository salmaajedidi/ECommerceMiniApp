<template>
  <component
    :is="tag"
    :to="to"
    :href="href"
    class="button"
    :class="customClasses"
    :type="type"
    v-bind="attrs"
  >
    <slot></slot>
  </component>
</template>

<script>
export default {
  name: "CommonButton",
  props: {
    tag: {
      type: String,
      default: "button",
      validator: (value) => ["button", "router-link"].includes(value),
    },
    to: {
      type: [String, Object], 
      default: null,
    },
    href: {
      type: String, 
      default: null,
    },
    customClasses: {
      type: String,
      default: "",
    },
    type: {
      type: String, 
      default: "button",
    },
    attrs: {
      type: Object,
      default: () => ({}), 
    },
  },
  
};
</script>

<style scoped>
  .button {
    padding: 12px 20px;
    font-size: .8rem;
    font-weight: 500;
    text-align: center;
    text-transform: uppercase;
    background-color: rgba(216,137,54,.9019607843);
    color: white;
    border: 2px solid rgba(216,137,54,.9019607843);
    border-radius: 15px;
    transition: all 0.3s ease;
    box-shadow: 0px 4px 6px rgba(216,137,54,.5);
  }

  /* Hover Effect */
  .button:hover {
    background-color: rgba(216,137,54,.9019607843);
    border-color: rgba(216,137,54,.9019607843);
    box-shadow: 0px 6px 12px rgba(216,137,54,.5);
    transform: translateY(-2px);
  }

  /* Focus Effect */
  .button:focus {
    outline: none;
    box-shadow: 0px 0px 8px rgba(216,137,54,.5);
  }

  /* Active Button State */
  .button:active {
    background-color: rgba(216,137,54,.9019607843);
    border-color: rgba(216,137,54,.9019607843);
    transform: translateY(1px);
  }
</style>
