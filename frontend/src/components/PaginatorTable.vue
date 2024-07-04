<template>
  <div class="wrapper">
    <div class="paginator-menu">
      <button @click="previousPage" :disabled="!previous" class="btn prev"></button>
      <button @click="nextPage" :disabled="!next" class="btn next"></button>
    </div>
  </div>
</template>

<script>
export default {
  name: "PaginatorTable",
  props: {
    next: String,
    previous: String,
  },
  data() {
      return{

      }
  },
  methods: {
    previousPage() {
      this.$emit('changePage', this.previous);
    },
    nextPage() {
      this.$emit('changePage', this.next);
    }
  }
}
</script>

<style lang="scss" scoped>

.paginator-menu {
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  top: 700px;
  width: 82.8%;
  padding: 0 20px;
}

.btn{
  border: none;
  cursor: pointer;
  width: 22px;
  height: 22px;
  margin: 0 10px;
  background-color: #32312e;
}

.btn.prev {
  -webkit-mask-image: url(@/assets/img/left-slide.svg);
  mask-image: url(@/assets/img/left-slide.svg);
}

.btn.next {
  -webkit-mask-image: url(@/assets/img/right-slide.svg);
  mask-image: url(@/assets/img/right-slide.svg);
}

button:disabled {
  cursor: not-allowed;
  background-color: #bbbbbb;
}

.btn:hover {
  opacity: 0.8;
}

.btn:active {
  transform: scale(0.95);
}
</style>