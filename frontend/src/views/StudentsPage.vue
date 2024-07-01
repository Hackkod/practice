<template>
  <LeftSideBar></LeftSideBar>
</template>

<script>
import axios from "@/plugins/axios";
import LeftSideBar from "@/components/LeftSideBar.vue";

export default {
  name: 'HomeView',
  components: {LeftSideBar},
  created() {
    this.fetchStudents()
  },
  methods: {
    async fetchStudents() {
      try {
        const response = await axios.get('anket_app/students/')
        this.students = response.data
      } catch (e) {
        alert('Ошибка')
      }
    },
  }
}
</script>

<style lang="scss" scoped>

</style>
