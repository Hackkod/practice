<template>
  <div class="work-form">
    <h3>{{ work ? 'Редактирование работы' : 'Создание новой работы' }}</h3>
    <form @submit.prevent="save">
      <div>
        <label>Заголовок:</label>
        <input v-model="form.name" required>
      </div>
      <div>
        <label>Студент:</label>
        <select v-model="form.student" required>
          <option v-for="student in students" :key="student.id" :value="student.id">
            {{ student.name }}
          </option>
        </select>
      </div>
      <div>
        <label>Наставник:</label>
        <select v-model="form.mentor" required>
          <option v-for="mentor in mentors" :key="mentor.id" :value="mentor.id">
            {{ mentor.name }}
          </option>
        </select>
      </div>
      <div>
        <label>Дата начала:</label>
        <input v-model="form.start_date" type="date" required>
      </div>
      <div>
        <label>Дата конца:</label>
        <input v-model="form.end_date" type="date" required>
      </div>
      <div>
        <label>Тип:</label>
        <select v-model="form.type" required>
          <option value="AGREEMENT">Agreement</option>
          <option value="STAFF">Staff</option>
        </select>
      </div>
      <div>
        <label>Позиция:</label>
        <textarea v-model="form.position"></textarea>
      </div>
      <div>
        <label>Описание:</label>
        <textarea v-model="form.description"></textarea>
      </div>
      <button type="submit">Сохранить</button>
      <button type="button" @click="$emit('close')">Отмена</button>
    </form>
  </div>
</template>

<script>
import axios from "@/plugins/axios";

export default {
  name: 'WorkForm',
  props: {
    work: Object,
  },
  data() {
    return {
      students: [],
      mentors: [],
      form: this.work ? { ...this.work } : {
        name: '',
        student: null,
        mentor: null,
        start_date: '',
        end_date: '',
        type: 'AGREEMENT',
        description: '',
      },
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
        this.students = response.data;
      } catch (e) {
        alert('Ошибка при загрузке списка студентов');
      }
    },
    async fetchMentors() {
      try {
        const response = await axios.get('anket_app/mentors/');
        this.mentors = response.data;
      } catch (e) {
        alert('Ошибка при загрузке списка наставников');
      }
    },
    async save() {
      this.$emit('save', this.form);
    },
  },
};
</script>

<style scoped>
.work-form {
  border: 1px solid #ccc;
  padding: 20px;
  margin: 20px 0;
}
</style>
