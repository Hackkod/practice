<template>
  <div class="main-layout">
    <LeftSideBar></LeftSideBar>
    <div class="content">
      <HeaderComponent :pageName="pageName" />
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import LeftSideBar from "@/components/LeftSideBar.vue";
import HeaderComponent from "@/components/HeaderComponent.vue";

export default {
  name: "MainLayout",
  components: {HeaderComponent, LeftSideBar},
  computed: {
    pageName() {
      return this.$route.meta.pageName || '';
    }
  }
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