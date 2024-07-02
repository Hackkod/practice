<template>
  <div class="main-layout">
    <LeftSideBar />
    <div class="content">
      <HeaderComponent />
      <div class="main-content">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script>
import LeftSideBar from "@/components/LeftSideBar.vue";
import HeaderComponent from "@/components/HeaderComponent.vue";

export default {
  name: "MainLayout",
  components: {HeaderComponent, LeftSideBar},
}
</script>

<style scoped lang="scss">
.main-layout {
  display: flex;
  height: 100vh;
}

.content {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
}

.main-content{
  flex-grow: 1;
  overflow-y: auto;
}

@media (max-height: 768px) {
  .content {
    width: calc(100% - 280px);
  }
}
</style>