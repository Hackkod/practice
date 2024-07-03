<template>
  <modal-overlay @close="close" @submit="save">
    <modal-header>{{ study ? 'Редактирование обучения' : 'Создание нового обучения' }}</modal-header>
    <div class="form-group">
      <label>Заголовок:</label>
      <input v-model="form.name" required>
    </div>
    <div class="form-group">
      <label>Студент:</label>
      <select v-model="form.student" required>
        <option v-for="student in students" :key="student.id" :value="student.id">
          {{ student.name }}
        </option>
      </select>
    </div>
    <div class="form-group">
      <label>Наставник:</label>
      <select v-model="form.mentor" required>
        <option v-for="mentor in mentors" :key="mentor.id" :value="mentor.id">
          {{ mentor.name }}
        </option>
      </select>
    </div>
    <div class="form-group">
      <label>Тип:</label>
      <select v-model="form.type" required>
        <option value="PRACTICE">Practice</option>
        <option value="INTERNSHIP">Internship</option>
      </select>
    </div>
    <div class="form-group">
      <label>Дата начала:</label>
      <input v-model="form.start_date" type="date" required>
    </div>
    <div class="form-group">
      <label>Дата окончания:</label>
      <input v-model="form.end_date" type="date" required>
    </div>
    <div class="form-group">
      <label>Описание:</label>
      <textarea v-model="form.description"></textarea>
    </div>
  </modal-overlay>
</template>

<script>
import axios from "@/plugins/axios";

export default {
  name: 'StudyForm',
  props: {
    study: Object,
  },
  data() {
    return {
      form: this.study ? { ...this.study } : {
        name: '',
        student: null,
        mentor: null,
        type: 'PRACTICE',
        start_date: '',
        end_date: '',
        description: '',
      },
      students: [],
      mentors: []
    };
  },
  created() {
    this.fetchStudents();
    this.fetchMentors();
  },
  methods: {
    async fetchStudents() {
      try {
        const response = await axios.get('anket_app/students/');
        this.students = response.data.results;
        if (!this.study && this.students.length) {
          this.form.student = this.students[0].id;
        }
      } catch (e) {
        alert('Ошибка при загрузке списка студентов');
      }
    },
    async fetchMentors() {
      try {
        const response = await axios.get('anket_app/mentors/');
        this.mentors = response.data.results;
        if (!this.study && this.mentors.length) {
          this.form.mentor = this.mentors[0].id;
        }
      } catch (e) {
        alert('Ошибка при загрузке списка наставников');
      }
    },
    async save() {
      this.$emit('save', this.form);
    },
    close() {
      this.$emit('close');
    }
  },
};
</script>

<style scoped>

</style>