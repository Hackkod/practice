<template>
  <label>
    <slot></slot>
  </label>
</template>

<script>
export default {
  name: "ModalLabel"
}
</script>

<style scoped lang="scss">
  label {
    display: block;
    padding-top: 6px;
    color: #4a4a4a;
  }
</style>