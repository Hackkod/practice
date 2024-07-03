<template>
  <div>
    <HeaderComponent title="Студенты" :tabs="tabs" @openForm="createStudent" />
    <div class="page-content">
      <StudentCard
          @updateStudents="fetchStudents"
          @editStudent="editStudent"
          v-for="student in students" :key="student.id"
          :student="student"
      />
    </div>
    <PaginatorTable :next="next" :previous="previous" @changePage="fetchStudents" />
    <studentForm :student="selectedStudent" v-if="showForm" @close="closeForm" @save="saveStudent" />
  </div>
</template>

<script>
import axios from "@/plugins/axios";
import StudentCard from "@/components/StudentCard.vue";
import HeaderComponent from "@/components/HeaderComponent.vue";
import StudentForm from "@/components/StudentForm.vue";
import PaginatorTable from "@/components/PaginatorTable.vue";

export default {
  name: 'HomeView',
  components: {PaginatorTable, StudentForm, HeaderComponent, StudentCard},
  data() {
    return {
      students: [],
      showForm: false,
      selectedStudent: null,
      activeTab: 0,
      tabs: [
        { name: 'Карта' },
        { name: 'Таблица' }
      ],
      next: null,
      previous: null,
      currentPage: 1,
    }
  },
  created() {
    this.fetchStudents()
  },
  methods: {
    createStudent() {
      this.selectedStudent = null
      this.showForm = true
    },
    editStudent(student) {
      this.selectedStudent = student
      this.showForm = true
    },
    closeForm() {
      this.showForm = false
      this.selectedStudent = null
    },
    async saveStudent(student) {
      try {
        const studentId = student.get('id');
        if (studentId) {
          const hasNewProfilePhoto = student.has('profile_photo') && student.get('profile_photo') instanceof File;

          if (!hasNewProfilePhoto) {
            student.delete('profile_photo');
          }
          await axios.put(`anket_app/students/${studentId}/`, student, {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          });
        } else {
          await axios.post(`anket_app/students/`, student, {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          });
        }
        await this.fetchStudents();
      } catch (e) {
        alert('Ошибка при создании студента');
      }
      this.closeForm();
    },
    async fetchStudents(url=`anket_app/students/?page=${this.currentPage}`) {
      try {
        const response = await axios.get(url)
        this.students = response.data.results
        this.next = response.data.next;
        this.previous = response.data.previous;
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