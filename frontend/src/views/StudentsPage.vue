<template>
  <div>
    <HeaderComponent title="Студенты" :tabs="tabs" />
    <div class="page-content">
      <StudentCard
          @updateStudents="fetchStudents"
          v-for="student in students" :key="student.id"
          :studentName="student.name"
          :studentSurname="student.surname"
          :studentPatronymic="student.patronymic"
          :studentCourse="student.course"
          :studentEstablishment="student.establishment"
          :studentProfilePhoto="student.profile_photo"
          :studentID="student.id"
      />
    </div>
  </div>
</template>

<script>
import axios from "@/plugins/axios";
import StudentCard from "@/components/StudentCard.vue";
import HeaderComponent from "@/components/HeaderComponent.vue";

export default {
  name: 'HomeView',
  components: {HeaderComponent, StudentCard},
  data() {
    return {
      students: [],
      activeTab: 0,
      tabs: [
        { name: 'Карта' },
        { name: 'Таблица' }
      ],
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
      } catch (e) {
        alert('Ошибка')
      }
    },
  }
}
</script>

<style lang="scss" scoped>
  .page-content {
    margin: 20px 0 0 20px;
    display: flex;
    flex-wrap: wrap;
    gap: 18px;
    justify-content: flex-start;
  }
</style>
