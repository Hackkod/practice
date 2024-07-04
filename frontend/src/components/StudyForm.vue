<template>
  <modal-overlay @close="close" @submit="save" :readonly="readonly">
    <modal-header>{{ readonly ? 'Просмотр обучения' : studyId ? 'Редактирование обучения' : 'Создание нового обучения' }}</modal-header>
    <div class="form-group">
      <label>Заголовок:</label>
      <input v-model="form.name" required :readonly="readonly">
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
        <option value="PRACTICE">Practice</option>
        <option value="INTERNSHIP">Internship</option>
      </select>
    </div>
    <div class="form-group">
      <label>Дата начала:</label>
      <input v-model="form.start_date" type="date" required :readonly="readonly">
    </div>
    <div class="form-group">
      <label>Дата окончания:</label>
      <input v-model="form.end_date" type="date" required :readonly="readonly">
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
  name: 'StudyForm',
  props: {
    studyId: Number,
    readonly: Boolean
  },
  data() {
    return {
      form: {
        name: '',
        student: null,
        mentor: null,
        type: 'PRACTICE',
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
    if (this.studyId)
      this.fetchStudyDetails(this.studyId);
  },
  watch: {
    study: {
      immediate: true,
      handler(newStudy) {
        if (newStudy) {
          this.form.name = newStudy.name;
          this.form.student = newStudy.student_full.id;
          this.form.mentor = newStudy.mentor_full.id;
          this.form.type = newStudy.type;
          this.form.start_date = newStudy.start_date;
          this.form.end_date = newStudy.end_date;
          this.form.description = newStudy.description;
        }
      }
    }
  },
  methods: {
    async fetchStudyDetails(id) {
      try {
        const response = await axios.get(`event_app/studies/${id}/`);
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
        if (!this.studyId && this.students.length) {
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
        if (!this.studyId && this.mentors.length) {
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