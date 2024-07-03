<template>
  <div>
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: "ModalFormGroup",
}
</script>

<style lang="scss" scoped>
div {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  margin-bottom: 15px;
  font-size: 16px;
}
</style>