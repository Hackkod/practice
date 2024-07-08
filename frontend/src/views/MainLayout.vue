<template>
  <div class="main-layout">
    <LeftSideBar />
    <div class="content">
      <router-view></router-view>
    </div>
    <paginator-table />
  </div>
</template>

<script>
import LeftSideBar from "@/components/LeftSideBar.vue";
import PaginatorTable from "@/components/PaginatorTable.vue";

export default {
  name: "MainLayout",
  components: { PaginatorTable, LeftSideBar },
};
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
