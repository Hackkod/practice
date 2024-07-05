<template>
  <div class="wrapper">
    <div class="paginator-menu">
      <button @click="changePage(currentPage - 1)" :disabled="currentPage === 1" class="btn prev"></button>
      <button
          v-for="page in visiblePages"
          :key="page"
          @click="changePage(page)"
          :class="['btn number', { active: currentPage === page }]"
      >{{ page }}</button>
      <button @click="changePage(currentPage + 1)" :disabled="currentPage === totalPages" class="btn next"></button>
    </div>
  </div>
</template>

<script>
export default {
  name: "PaginatorTable",
  props: {
    totalPages: {
      type: Number,
      required: true
    },
    currentPage: {
      type: Number,
      required: true
    }
  },
  computed: {
    visiblePages() {
      let pages = [];
      if (this.totalPages <= 5) {
        for (let i = 1; i <= this.totalPages; i++) {
          pages.push(i);
        }
      } else {
        if (this.currentPage <= 3) {
          for (let i = 1; i <= 4; i++) {
            pages.push(i);
          }
          pages.push('...');
          pages.push(this.totalPages);
        } else if (this.currentPage > this.totalPages - 3) {
          pages.push(1);
          pages.push('...');
          for (let i = this.totalPages - 3; i <= this.totalPages; i++) {
            pages.push(i);
          }
        } else {
          pages.push(1);
          pages.push('...');
          for (let i = this.currentPage - 2; i <= this.currentPage + 2; i++) {
            pages.push(i);
          }
          pages.push('...');
          pages.push(this.totalPages);
        }
      }
      return pages;
    }
  },
  data() {
      return{
      }
  },
  methods: {
    changePage(page) {
      if (page !== '...' && page !== this.currentPage) {
        this.$emit('changePage', page);
      }
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
  color: #bbbbbb;
  display: flex;
  justify-content: center;
  align-items: center;
}

.btn.number{
  background-color: transparent;
  font-size: 18px;
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

.btn.active {
  color: #32312e;
  width: 28px;
  height: 28px;
  border: none;
  background-color: #e9e3ff;
  border-radius: 5px;
  font-weight: bold;
}
</style>