<template>
  <div v-if="showModal" class="modal" @click.self="closeModal" :class="customClasses">
    <div class="modal-content">
      <!-- Close Button -->
      <div class="modal-close" @click="closeModal">×</div>
      <h3>{{ title }}</h3><br />
      <slot></slot>
      <div class="modal-actions" v-if="hideActions">
        <CommonButton
          :tag="'button'"
          :type="confirmType"
          :customClasses="'btn-confirm'"
          @click="confirmAction"
        >
          {{ confirmText }}
        </CommonButton>

        <CommonButton
          :tag="'button'"
          :type="cancelType"
          :customClasses="'btn-cancel'"
          @click="closeModal"
        >
          {{ cancelText }}
        </CommonButton>
      </div>
    </div>
  </div>
</template>

<script>
import CommonButton from "./CommonButton.vue";

export default {
  name: "GenericModal",
  components: { CommonButton },
  props: {
    title: {
      type: String,
      required: true,
    },
    customClasses: {
      type: String,
      default: "",
    },
    confirmText: {
      type: String,
      default: "Submit",
    },
    cancelText: {
      type: String,
      default: "Close",
    },
    showModal: {
      type: Boolean,
      required: true,
    },
    hideActions: {
      type: Boolean,
      required: true,
    },
    confirmType: {
      type: String,
      default: "button",
    },
    cancelType: {
      type: String,
      default: "button",
    },
  },
  emits: ["close", "confirm"],
  methods: {
    closeModal() {
      this.$emit("close");
    },
    confirmAction() {
      this.$emit("confirm");
    },
  },
};
</script>

<style scoped>
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.modal-content {
  position: relative; /* Important for positioning the close button */
  background-color: #fff;
  padding: 30px 40px;
  border-radius: 8px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
  max-width: 400px;
}

.modal-close {
  position: absolute;
  top: 10px;
  right: 10px;
  font-size: 24px;
  font-weight: bold;
  cursor: pointer;
  color: #888;
  transition: color 0.3s ease;
}

.modal-close:hover {
  color: #333;
}

.modal-actions {
  text-align: center;
  margin-top: 20px;
}

h3 {
  text-align: center;
}

.btn-confirm,
.btn-cancel {
  padding: 10px 15px;
  font-size: 16px;
  cursor: pointer;
  border: none;
  border-radius: 5px;
  margin: 0 10px;
}

.btn-cancel {
  background-color: #ffffff;
  color: rgba(216, 137, 54, 0.9);
  border: 1px solid rgba(216, 137, 54, 0.9);
}

.btn-cancel:hover {
  background-color: #ffffff;
  color: rgba(216, 137, 54, 0.9);
  border: 1px solid rgba(216, 137, 54, 0.9);
}
</style>
