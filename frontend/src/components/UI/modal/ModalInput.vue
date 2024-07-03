<template>
  <input
      :value="modelValue"
      @input="updateValue"
      v-bind="$attrs"
  />
</template>

<script>
export default {
  name: "ModalInput",
  props: {
    modelValue: {
      type: String,
      required: true
    }
  },
  methods: {
    updateValue(event) {
      this.$emit('update:modelValue', event.target.value);
    }
  }
}
</script>

<style scoped>
input {
  width: 230px;
  padding: 4px;
  border: 1px solid #ccc;
  border-radius: 10px;
  background: #ffffff;
  color: #32312e;
}
</style>
