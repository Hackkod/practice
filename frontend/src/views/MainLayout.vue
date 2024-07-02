<template>
  <div class="main-layout">
    <LeftSideBar />
    <div class="content">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import LeftSideBar from "@/components/LeftSideBar.vue";

export default {
  name: "MainLayout",
  components: {LeftSideBar},
}
</script>

<style scoped lang="scss">
  .main-layout {
    display: flex;
    flex-direction: row;
  }

  .content {
    width: 100%;
  }
</style>