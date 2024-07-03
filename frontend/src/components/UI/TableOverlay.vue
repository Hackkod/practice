<template>
  <div class="work-list">
    <table class="work-table">
      <slot></slot>
    </table>
  </div>
</template>

<script>
export default {
  name: 'table-overlay',
}
</script>

<style scoped>
  .work-list {
    background-image: linear-gradient(#faf8ff, #faf8ff);
    background-size: calc(100% - 40px) calc(100% - 60px);
    background-position: center;
  }

  .work-table {
    backdrop-filter: blur(20px);
    width: 100%;
    padding: 0 20px;
    border-collapse: separate;
    border-spacing: 0 14px;
  }
</style>
