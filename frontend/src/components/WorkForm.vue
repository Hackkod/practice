<template>
  <modal-overlay @close="close" @submit="save">
    <modal-header>{{ work ? 'Редактирование работы' : 'Создание новой работы' }}</modal-header>
    <modal-form-group>
      <modal-label>Заголовок:</modal-label>
      <modal-input v-model="form.name" required/>
    </modal-form-group>
    <modal-form-group>
      <modal-label>Студент:</modal-label>
      <modal-select v-model="form.student" required>
        <option v-for="student in students" :key="student.id" :value="student.id">
          {{ student.name }}
        </option>
      </modal-select>
    </modal-form-group>
    <modal-form-group>
      <modal-label>Наставник:</modal-label>
      <modal-select v-model="form.mentor" required>
        <option v-for="mentor in mentors" :key="mentor.id" :value="mentor.id">
          {{ mentor.name }}
        </option>
      </modal-select>
    </modal-form-group>
    <modal-form-group>
      <modal-label>Тип:</modal-label>
      <modal-select v-model="form.type" required>
        <option value="AGREEMENT">Agreement</option>
        <option value="STAFF">Staff</option>
      </modal-select>
    </modal-form-group>
    <modal-form-group>
      <modal-label>Позиция:</modal-label>
      <modal-input v-model="form.position" required/>
    </modal-form-group>
    <modal-form-group>
      <modal-label>Дата начала:</modal-label>
      <modal-input v-model="form.start_date" type="date" required/>
    </modal-form-group>
    <modal-form-group>
      <modal-label>Дата окончания:</modal-label>
      <modal-input v-model="form.end_date" type="date" required/>
    </modal-form-group>
    <modal-form-group>
      <modal-label>Описание:</modal-label>
      <modal-textarea v-model="form.description"/>
    </modal-form-group>
  </modal-overlay>
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
      form: this.work ? { ...this.work } : {
        name: '',
        student: null,
        mentor: null,
        type: 'AGREEMENT',
        position: '',
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
        if (!this.work && this.students.length) {
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
        if (!this.work && this.mentors.length) {
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
