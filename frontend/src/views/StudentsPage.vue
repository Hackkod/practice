<template>
  <div>
    <HeaderComponent title="Студенты" :tabs="tabs" :activeTab="activeTab" @tabChange="setActiveTab" @openForm="createStudent" />
    <div :class="{'page-content': activeTab === 0}">
      <template v-if="activeTab === 0">
        <StudentCard
            @updateStudents="fetchStudents"
            @editStudent="editStudent"
            v-for="student in students" :key="student.id"
            :student="student"
        />
      </template>
      <template v-else-if="activeTab === 1">
        <StudentList
            :students="students"
            @updateStudents="fetchStudents"
            @editStudent="editStudent"
        />
      </template>
    </div>
    <StudentForm :student="selectedStudent" v-if="showForm" @close="closeForm" @save="saveStudent" />
    <PaginatorTable :next="next" :previous="previous" @changePage="fetchStudents" />
  </div>
</template>

<script>
import axios from "@/plugins/axios";
import StudentCard from "@/components/StudentCard.vue";
import HeaderComponent from "@/components/HeaderComponent.vue";
import StudentForm from "@/components/StudentForm.vue";
import PaginatorTable from "@/components/PaginatorTable.vue";
import StudentList from "@/components/StudentList.vue";

export default {
  name: 'HomeView',
  components: {StudentList, PaginatorTable, StudentForm, HeaderComponent, StudentCard},
  data() {
    return {
      students: [],
      showForm: false,
      selectedStudent: null,
      activeTab: 0,
      itemsPerPage: 12,
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
    async fetchStudents(url=`anket_app/students/?page=${this.currentPage}&page_size=${this.itemsPerPage}`) {
      try {
        const response = await axios.get(url)
        this.students = response.data.results
        this.next = response.data.next;
        this.previous = response.data.previous;
      } catch (e) {
        alert('Ошибка')
      }
    },
    setActiveTab(index) {
      this.activeTab = index;
      this.itemsPerPage = index === 0 ? 12 : 6;
      this.fetchStudents();
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