<template>
  <textarea
    :value="modelValue"
    @input="updateValue"
    v-bind="$attrs"
  />
</template>

<script>
export default {
  name: "ModalTextarea",
  props: {
    modelValue: {
      String,
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

<style lang="scss" scoped>
textarea {
  width: 230px;
  padding: 4px;
  border: 1px solid #ccc;
  border-radius: 10px;
  background: #ffffff;
  color: #32312e;
}
</style>