<template>
  <h3>
    <slot></slot>
  </h3>
</template>

<script>
export default {
  name: "ModalHeader",
};
</script>

<style lang="scss" scoped>
h3 {
  color: #32312e;
  font-size: 20px;
  margin-bottom: 20px;
  text-align: center;
}
</style>
