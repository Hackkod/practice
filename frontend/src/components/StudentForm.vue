<template>
  <modal-overlay @close="close" @submit="save">
    <modal-header>{{ student ? 'Редактирование студента' : 'Создание нового студента' }}</modal-header>
    <div class="form-content">
      <div class="first-column">
        <div class="form-group">
          <label>Фамилия:</label>
          <input v-model="form.surname" required>
        </div>
        <div class="form-group">
          <label>Имя:</label>
          <input v-model="form.name" required>
        </div>
        <div class="form-group">
          <label>Отчество:</label>
          <input v-model="form.patronymic" required>
        </div>
        <div class="form-group">
          <label>Пол:</label>
          <select v-model="form.gender" required>
            <option value="M">Male</option>
            <option value="F">Female</option>
          </select>
        </div>
        <div class="form-group">
          <label>Дата рождения:</label>
          <input v-model="form.birth_date" type="date" required>
        </div>
        <div class="form-group">
          <label>Софт скиллы:</label>
          <textarea v-model="form.soft_skills"></textarea>
        </div>
        <div class="form-group">
          <label>Хард скиллы:</label>
          <select multiple v-model="form.hard_skills_id" required>
            <option v-for="hard_skill in hard_skill_ids" :key="hard_skill.id" :value="hard_skill.id">
              {{ hard_skill.skill_name }}
            </option>
          </select>
        </div>
      </div>
      <div class="second-column">
        <div class="form-group">
          <label>Дополнительная информация:</label>
          <textarea v-model="form.other_info"></textarea>
        </div>
        <div class="form-group">
          <label>Фотография студента:</label>
          <input type="file" @change="handleFileChange" name="profile_photo">
        </div>
        <div class="form-group">
          <label>Учебное учреждение:</label>
          <input v-model="form.establishment" required>
        </div>
        <div class="form-group">
          <label>Дата начала обучения:</label>
          <input v-model="form.start_study_year" type="number" required>
        </div>
        <div class="form-group">
          <label>Дата окончания обучения:</label>
          <input v-model="form.end_study_year" type="number" required>
        </div>
      </div>
    </div>
  </modal-overlay>
</template>

<script>
import ModalOverlay from "@/components/UI/ModalOverlay.vue";
import axios from "@/plugins/axios";

export default {
  name: "StudentForm",
  components: {ModalOverlay},
  props: {
    student: Object,
  },
  data() {
    return {
      form: this.student ? { ...this.student } : {
        name: '',
        surname: '',
        patronymic: '',
        gender: 'M',
        birth_date: null,
        soft_skills: '',
        hard_skills_id: [],
        other_info: '',
        profile_photo: null,
        establishment: '',
        start_study_year: null,
        end_study_year: null
      },
      hard_skill_ids: [],
    };
  },
  created() {
    this.fetchHardSkillIds()
  },
  methods: {
    async fetchHardSkillIds() {
      try {
        const response = await axios.get('hard_skill_app/hard_skills/');
        this.hard_skill_ids = response.data.results;
      } catch (e) {
        alert('Ошибка при загрузке списка хард скиллов');
      }
    },
    handleFileChange(event) {
      this.form.profile_photo = event.target.files[0];
    },
    async save() {
      const formData = new FormData();
      Object.keys(this.form).forEach(key => {
        const value = this.form[key];
        if (Array.isArray(value)) {
          if (value.length > 0) {
            value.forEach(item => {
              formData.append(key, item);
            });
          }
        } else if (value !== null && key !== 'profile_photo') {
          formData.append(key, value);
        }
      });
      if (this.form.profile_photo) {
        formData.append('profile_photo', this.form.profile_photo);
      }
      this.$emit('save', formData);
    },
    close() {
      this.$emit('close');
    }
  }
}
</script>

<style lang="scss" scoped>
.form-content {
  display: flex;
  flex-direction: row;
  grid-gap: 30px;
}
</style>