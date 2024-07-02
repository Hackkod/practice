<template>
  <div class="page-content">
    <StudentCard
        v-for="student in students" :key="student.id"
        :studentName="student.name"
        :studentSurname="student.surname"
        :studentPatronymic="student.patronymic"
        :studentCourse="student.course"
        :studentEstablishment="student.establishment"
        :studentProfilePhoto="student.profile_photo"
    />
  </div>
</template>

<script>
import axios from "@/plugins/axios";
import StudentCard from "@/components/StudentCard.vue";

export default {
  name: 'HomeView',
  components: {StudentCard},
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
    margin: 40px 0 0 40px;
    display: flex;
    flex-wrap: wrap;
    gap: 30px;
    justify-content: flex-start;
  }
</style>
