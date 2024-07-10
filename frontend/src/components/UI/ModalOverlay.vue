<template>
  <div class="modal-overlay" @dblclick.self="close" @click.self="handleClick">
    <v-form class="modal-content" ref="form">
      <slot></slot>
      <div v-if="!readonly" class="form-btns">
        <v-btn size="large" class="cancel-btn" @click="close">Отмена</v-btn>
        <v-btn size="large" class="submit-btn" @click="submitForm"
          >Сохранить</v-btn
        >
      </div>
    </v-form>
  </div>
</template>

<script>
export default {
  name: "ModalOverlay",
  props: {
    readonly: Boolean,
  },
  emits: ["close", "submit"],
  methods: {
    close() {
      this.$emit("close");
    },
    handleClick() {
      if (this.readonly) {
        this.close();
      }
    },
    async submitForm() {
      const { valid } = await this.$refs.form.validate();
      if (valid) {
        this.$emit("submit", this.form);
      }
    },
  },
};
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background: #f0f4ff;
  padding: 20px 25px;
  border-radius: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.form-btns {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
}

button {
  width: 47%;
  font-size: 16px;
  border: 3px solid;
  border-radius: 10px;
  cursor: pointer;
}

.submit-btn {
  background: #f0ecff;
  color: #bdabff;
  border-color: #bdabff;
}

.cancel-btn {
  background: #ffecec;
  color: #ffabab;
  border-color: #ffabab;
}

button:hover {
  opacity: 0.9;
}
</style>
