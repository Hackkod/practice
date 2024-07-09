<template>
  <v-app>
    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',
}

// Остановить ошибку resizeObserver
const debounce = (callback, delay) => {
  let tid;
  return function (...args) {
    const ctx = this;
    if (tid) clearTimeout(tid);
    tid = setTimeout(() => {
      callback.apply(ctx, args);
    }, delay);
  };
};

const OriginalResizeObserver = window.ResizeObserver;

window.ResizeObserver = class ResizeObserver extends OriginalResizeObserver {
  constructor(callback) {
    super(debounce(callback, 20));
  }
};
</script>

<style>
*{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Roboto', sans-serif;
}
</style>