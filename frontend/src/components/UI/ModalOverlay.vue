<template>
  <div class="modal-overlay" @click.self="close">
    <div class="modal-content">
      <slot></slot>
      <div class="form-btns">
        <button type="submit" @click="submit">Сохранить</button>
        <button type="button" @click="close">Отмена</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ModalOverlay',
  methods: {
    close() {
      this.$emit('close');
    },
    submit() {
      this.$emit('submit');
    }
  }
}
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
  padding: 40px;
  border-radius: 20px;
  width: 600px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.form-btns {
  display: flex;
  justify-content: space-between;
  margin-top: 30px;
}

button {
  width: 47%;
  padding: 10px;
  font-size: 20px;
  border: 3px solid;
  border-radius: 12px;
  cursor: pointer;
}

button[type="submit"] {
  background: #f0ecff;
  color: #bdabff;
  border-color: #bdabff;
}

button[type="button"] {
  background: #f0ecff;
  color: #ccc;
  border-color: #ccc;
}

button:hover {
  opacity: 0.9;
}
</style>
