<template>
  <modal-overlay @close="close" @submit="save" :readonly="readonly">
    <modal-header>{{ readonly ? 'Просмотр работы' : workId ? 'Редактирование работы' : 'Создание новой работы' }}</modal-header>
    <div class="form-group">
      <label>Заголовок:</label>
      <input v-model="form.name" required :readonly="readonly"/>
    </div>
    <div class="form-group">
      <label>Студент:</label>
      <input v-if="readonly" v-model="students.name" :readonly="readonly">
      <select v-else v-model="form.student" required>
        <option v-for="student in students" :key="student.id" :value="student.id">
          {{ truncatedName(student) }}
        </option>
      </select>
    </div>
    <div class="form-group">
      <label>Наставник:</label>
      <input v-if="readonly" v-model="mentors.name" :readonly="readonly">
      <select v-else v-model="form.mentor" required>
        <option v-for="mentor in mentors" :key="mentor.id" :value="mentor.id">
          {{ truncatedName(mentor) }}
        </option>
      </select>
    </div>
    <div class="form-group">
      <label>Тип:</label>
      <input v-if="readonly" v-model="form.type" :readonly="readonly">
      <select v-else v-model="form.type" required>
        <option value="AGREEMENT">Agreement</option>
        <option value="STAFF">Staff</option>
      </select>
    </div>
    <div class="form-group">
      <label>Позиция:</label>
      <input v-model="form.position" required :readonly="readonly"/>
    </div>
    <div class="form-group">
      <label>Дата начала:</label>
      <input v-model="form.start_date" type="date" required :readonly="readonly"/>
    </div>
    <div class="form-group">
      <label>Дата окончания:</label>
      <input v-model="form.end_date" type="date" required :readonly="readonly"/>
    </div>
    <div class="form-group">
      <label>Описание:</label>
      <textarea v-model="form.description" :readonly="readonly"/>
    </div>
  </modal-overlay>
</template>

<script>
import axios from "@/plugins/axios";

export default {
  name: 'WorkForm',
  props: {
    workId: Number,
    readonly: Boolean
  },
  data() {
    return {
      form: {
        name: '',
        student: null,
        mentor: null,
        type: 'AGREEMENT',
        position: '',
        start_date: null,
        end_date: null,
        description: '',
      },
      students: [],
      mentors: []
    };
  },
  created() {
    if (!this.readonly)
      this.fetchStudents();
    if (!this.readonly)
      this.fetchMentors();
    if (this.workId)
      this.fetchWorkDetails(this.workId);
  },
  watch: {
    work: {
      immediate: true,
      handler(newWork) {
        if (newWork) {
          this.form.name = newWork.name;
          this.form.student = newWork.student_full.id;
          this.form.mentor = newWork.mentor_full.id;
          this.form.type = newWork.type;
          this.form.position = newWork.position;
          this.form.start_date = newWork.start_date;
          this.form.end_date = newWork.end_date;
          this.form.description = newWork.description;
        }
      }
    }
  },
  methods: {
    async fetchWorkDetails(id) {
      try {
        const response = await axios.get(`event_app/works/${id}/`);
        if (this.readonly)
          this.students = response.data.student_full
        if (this.readonly)
          this.mentors = response.data.mentor_full
        this.form = { ...response.data }
      } catch (e) {
        alert('Ошибка при загрузке данных студента');
      }
    },
    async fetchStudents() {
      try {
        const response = await axios.get('anket_app/students/');
        this.students = response.data.results;
        if (!this.workId && this.students.length) {
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
        if (!this.workId && this.mentors.length) {
          this.form.mentor = this.mentors[0].id;
        }
      } catch (e) {
        alert('Ошибка при загрузке списка наставников');
      }
    },
    async save() {
      this.$emit('save', this.form);
    },
    truncatedName(person){
      const fullName =
          person.surname + ' ' +
          person.name[0] + '.' +
          person.patronymic[0] + '.'
      return fullName.length > 13 ? fullName.slice(0, 13) + '..' : fullName;
    },
    close() {
      this.$emit('close');
    }
  },
};
</script>

<style scoped>

</style>
