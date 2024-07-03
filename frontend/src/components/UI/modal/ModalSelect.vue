<template>
  <select :value="modelValue" @change="updateValue" v-bind="$attrs">
    <slot></slot>
  </select>
</template>

<script>
export default {
  name: 'ModalSelect',
  props: {
    modelValue: {
      type: [String, Number],
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
select {
  width: 230px;
  padding: 4px;
  border: 1px solid #ccc;
  border-radius: 10px;
  background: #ffffff;
  color: #32312e;
}
</style>
