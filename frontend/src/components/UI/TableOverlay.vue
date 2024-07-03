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

  :deep(tr) {
    background-color: #fff;
    box-shadow: 0 4px 20px 0 #f2f1f3;
    font-size: 16px;
  }

  :deep(tr:hover) {
    background-color: #faf8ff;
  }

  :deep(th) {
    color: #32312e;
    padding: 12px 8px;
    text-align: left;
    border: none;
    white-space: nowrap;
    background-color: #f9f9f9;
    font-size: 18px;
  }

  :deep(th:first-child) {
    border-radius: 20px 0 0 20px;
    padding-left: 20px;
  }

  :deep(th:last-child) {
    border-radius: 0 20px 20px 0;
  }

  :deep(td) {
    color: #32312e;
    padding: 12px 8px;
    text-align: left;
    border: none;
    white-space: nowrap;
  }

  :deep(td:first-child) {
    border-radius: 20px 0 0 20px;
    padding-left: 20px;
  }

  :deep(td:last-child) {
    border-radius: 0 20px 20px 0;
  }

  :deep(.table-btns) {
    display: flex;
    grid-gap: 35px;

    :deep(button) {
      display: flex;
      align-items: center;
    }
  }
</style>
