<template>
  <work-create-btn @workAdded="addWorkToList"/>
  <work-list :works="works"/>
</template>

<script>
import axios from "@/plugins/axios";
import WorkList from "@/components/WorkList.vue";
import WorkCreateBtn from "@/components/WorkCreateBtn.vue";

export default {
  components: {WorkCreateBtn, WorkList},
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
    }
  }
}
</script>

<style lang="scss" scoped>

</style>