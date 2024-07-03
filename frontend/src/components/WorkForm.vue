<template>
  <modal-overlay @close="close" @submit="save">
    <h3>{{ work ? 'Редактирование работы' : 'Создание новой работы' }}</h3>
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
        <option value="AGREEMENT">Agreement</option>
        <option value="STAFF">Staff</option>
      </select>
    </div>
    <div class="form-group">
      <label>Позиция:</label>
      <input v-model="form.position" required>
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
import ModalOverlay from "@/components/UI/ModalOverlay.vue";

export default {
  name: 'WorkForm',
  components: {ModalOverlay},
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
    close() {
      this.$emit('close');
    }
  },
};
</script>

<style scoped>
h3 {
  color: #32312e;
  font-size: 20px;
  margin-bottom: 20px;
  text-align: center;
}

.form-group {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  margin-bottom: 15px;
  font-size: 16px;

  label {
    display: block;
    padding-top: 6px;
    color: #4a4a4a;
  }

  input, select, textarea {
    width: 230px;
    padding: 4px;
    border: 1px solid #ccc;
    border-radius: 10px;
    background: #ffffff;
    color: #32312e;
  }
}
</style>
