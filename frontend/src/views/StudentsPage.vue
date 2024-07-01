<template>
  <div class="page-content">
  </div>
</template>

<script>
import axios from "@/plugins/axios";

export default {
  name: 'HomeView',
  components: { },
  data() {
    return {
      students: [],
    }
  },
  created() {
    this.fetchStudents()
  },
  methods: {
    async fetchStudents() {
      try {
        const response = await axios.get('anket_app/students/')
        this.students = response.data
        console.log(this.students)
      } catch (e) {
        alert('Ошибка')
      }
    },
  }
}
</script>

<style lang="scss" scoped>
  .page-content {
    display: flex;
    flex-direction: row;
  }
</style>
