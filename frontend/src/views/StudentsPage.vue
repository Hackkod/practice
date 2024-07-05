<template>
  <div>
    <HeaderComponent
        title="Студенты"
        :tabs="tabs"
        :activeTab="activeTab"
        @tabChange="setActiveTab"
        @openForm="createStudent"
       :filterOptions="filterOptions"
       :showEventFilters="false"
       :showAnketFilters="true"
       :showCourseFilter="true"
       @updateFilters="updateFilters"
    />
    <div :class="{'page-content': activeTab === 0}">
      <template v-if="activeTab === 0">
        <StudentCard
          @viewStudent="viewStudent"
          @updateStudents="fetchStudents"
          @editStudent="editStudent"
          v-for="student in students" :key="student.id"
          :student="student"
        />
      </template>
      <template v-else-if="activeTab === 1">
        <StudentList
          :students="students"
          @viewStudent="viewStudent"
          @updateStudents="fetchStudents"
          @editStudent="editStudent"
        />
      </template>
    </div>
    <StudentForm
        :studentId="selectedStudent"
        :readonly="readonly"
        v-if="showForm"
        @close="closeForm"
        @save="saveStudent"
    />
    <PaginatorTable
        :next="next"
        :previous="previous"
        @changePage="fetchStudents"
    />
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
  components: {
    StudentList,
    PaginatorTable,
    StudentForm,
    HeaderComponent,
    StudentCard
  },
  data() {
    return {
      students: [],
      showForm: false,
      readonly: false,
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
      filterOptions: {
        hardSkills: []
      },
      filters: {
        searchQuery: '',
        selectedHardSkill: null,
        selectedCourse: null
      }
    }
  },
  created() {
    this.fetchHardSkills();
    this.fetchStudents()
  },
  methods: {
    createStudent() {
      this.selectedStudent = null
      this.showForm = true
      this.readonly = false
    },
    editStudent(student) {
      this.selectedStudent = student.id
      this.showForm = true
      this.readonly = false
    },
    closeForm() {
      this.showForm = false
      this.selectedStudent = null
      this.readonly = false
    },
    viewStudent(student) {
      this.selectedStudent = student.id
      this.readonly = true
      this.showForm = true
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
        const { searchQuery, selectedHardSkill, selectedCourse } = this.filters;
        let params = {
          search: searchQuery,
          course: selectedCourse
        };

        if (selectedHardSkill) {
          params.hard_skills_id = selectedHardSkill;
        }

        const response = await axios.get(url, {
          params
        });
        this.students = response.data.results
        this.next = response.data.next;
        this.previous = response.data.previous;
      } catch (e) {
        alert('Ошибка')
      }
    },
    async fetchHardSkills() {
      try {
        const response = await axios.get('hard_skill_app/hard_skills/');
        this.filterOptions.hardSkills = response.data.results;
      } catch (e) {
        alert('Ошибка при получении списка навыков');
      }
    },
    setActiveTab(index) {
      this.activeTab = index;
      this.itemsPerPage = index === 0 ? 12 : 6;
      this.fetchStudents();
    },
    updateFilters(newFilters) {
      this.filters = newFilters;
      this.fetchStudents();
    }
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