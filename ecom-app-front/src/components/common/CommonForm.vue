<template>
  <form>
    <slot></slot>
    <div class="form-actions">
      <CommonButton
        :tag="'button'"
        type="submit"  
        :customClasses="'btn-submit'"
      >
        {{ submitText }}
      </CommonButton>
    </div>
  </form>
</template>

<script>
import CommonButton from './CommonButton.vue';

export default {
  name: 'CommonForm',
  components: { CommonButton },
  props: {
    submitText: {
      type: String,
      default: 'Soumettre',
    },
  },
};
</script>

<style scoped>
.form-actions {
  margin-top: 20px;
  text-align: center;
}

.btn-submit {
  font-size: 16px;
  width: 100%;
}
</style>
