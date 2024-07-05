<template>
  <div class="modal-overlay" @click.self="close">
    <form @submit.prevent="save" class="modal-content">
      <slot></slot>
      <div v-if="!readonly" class="form-btns">
        <button type="button" @click="close">Отмена</button>
        <button type="submit">Сохранить</button>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: 'ModalOverlay',
  props: {
    readonly: Boolean
  },
  methods: {
    close() {
      this.$emit('close');
    },
    submit(event) {
      if (event.target.checkValidity()) {
        this.$emit('submit', this.form);
      } else {
        alert('Пожалуйста, заполните все обязательные поля.');
      }
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
  padding: 8px;
  font-size: 16px;
  border: 3px solid;
  border-radius: 10px;
  cursor: pointer;
}

button[type="submit"] {
  background: #f0ecff;
  color: #bdabff;
  border-color: #bdabff;
}

button[type="button"] {
  background: #ffecec;
  color: #ffabab;
  border-color: #ffabab;
}

button:hover {
  opacity: 0.9;
}

:deep(.form-group) {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  margin-bottom: 15px;
  font-size: 16px;
}

:deep(label) {
  display: block;
  padding-top: 6px;
  color: #4a4a4a;
  margin-right: 20px;
}

:deep(input) {
  width: 230px;
  padding: 4px;
  border: 1px solid #ccc;
  border-radius: 10px;
  background: #ffffff;
  color: #32312e;
  outline: none;
}

:deep(input::placeholder) {
  color: #bbb; /* Ваш желаемый цвет */
}

:deep(select) {
  width: 230px;
  padding: 4px;
  border: 1px solid #ccc;
  border-radius: 10px;
  background: #ffffff;
  color: #32312e;
}

:deep(textarea) {
  width: 230px;
  min-height: 90px;
  padding: 4px;
  border: 1px solid #ccc;
  border-radius: 10px;
  background: #ffffff;
  color: #32312e;
  outline: none;
}

:deep(textarea::placeholder) {
  color: #bbb; /* Ваш желаемый цвет */
}

</style>
