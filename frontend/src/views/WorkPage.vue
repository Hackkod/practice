<template>
  <left-side-bar></left-side-bar>
  <work-create-btn @workAdded="addWorkToList"/>
  <work-list :works="works" @updateWorks="fetchWorks"/>
</template>

<script>
import axios from "@/plugins/axios";
import WorkList from "@/components/WorkList.vue";
import WorkCreateBtn from "@/components/WorkCreateBtn.vue";
import LeftSideBar from "@/components/LeftSideBar.vue";

export default {
  components: {LeftSideBar, WorkCreateBtn, WorkList},
  data() {
    return {
      works: [],
    }
  },
  created() {
    this.fetchWorks();
  },
  methods: {
    async fetchWorks() {
      try {
        const response = await axios.get('event_app/works/');
        this.works = response.data;
      } catch (e) {
          alert('Ошибка при получении списка работ')
      }
    },
    addWorkToList(work) {
      this.works.push(work);
    },
  }
}
</script>

<style lang="scss" scoped>

</style>