<template>
  <modal-overlay @close="close" @submit="save" :readonly="readonly">
    <modal-header>{{ readonly ? 'Просмотр наставника' : mentorId ? 'Редактирование наставника' : 'Создание нового наставника' }}</modal-header>
    <div class="form-content">
      <div class="first-column">
        <div class="form-group">
          <label>Фамилия:</label>
          <input v-model="form.surname" placeholder="Иванов" required :readonly="readonly">
        </div>
        <div class="form-group">
          <label>Имя:</label>
          <input v-model="form.name" placeholder="Иван" required :readonly="readonly">
        </div>
        <div class="form-group">
          <label>Отчество:</label>
          <input v-model="form.patronymic" placeholder="Иванович" required :readonly="readonly">
        </div>
        <div class="form-group">
          <label>Пол:</label>
          <input v-if="readonly" v-model="form.gender" required :readonly="readonly">
          <select v-else v-model="form.gender" required>
            <option value="M">Male</option>
            <option value="F">Female</option>
          </select>
        </div>
        <div class="form-group">
          <label>Дата рождения:</label>
          <input v-model="form.birth_date" type="date" required :readonly="readonly">
        </div>
        <div class="form-group">
          <label>Должность:</label>
          <input v-model="form.job_position" placeholder="Самый главный" required :readonly="readonly">
        </div>
      </div>
      <div class="second-column">
        <div class="form-group">
          <label>Фотография наставника:</label>
          <div v-if="readonly" class="mentor-info-img-container-main">
            <div class="mentor-info-img-container">
              <img class="mentor-info-img"
                   :src="form.profile_photo"
                   alt="">
            </div>
          </div>
          <input v-else type="file" @change="handleFileChange" name="profile_photo">
        </div>
        <div class="form-group">
          <label>Дополнительная информация:</label>
          <textarea v-model="form.other_info" placeholder="Поборол депрессию в 0 лет" :readonly="readonly"/>
        </div>
        <div class="form-group">
          <label>Софт скиллы:</label>
          <textarea v-model="form.soft_skills" placeholder="Умеет убеждать перерисовывать связи между сущностями" :readonly="readonly"/>
        </div>
        <div class="form-group">
          <label>Хард скиллы:</label>
          <div class="hard-skill-list" v-if="readonly">
            <span v-for="skill in hard_skill_ids" :key="skill.id">
                {{ skill.skill_name }}
            </span>
          </div>
          <select v-else multiple v-model="form.hard_skills_id" required :disabled="readonly">
            <option v-for="hard_skill in hard_skill_ids" :key="hard_skill.id" :value="hard_skill.id">
              {{ hard_skill.skill_name }}
            </option>
          </select>
        </div>
      </div>
    </div>
  </modal-overlay>
</template>

<script>
import ModalOverlay from "@/components/UI/ModalOverlay.vue";
import axios from "@/plugins/axios";

export default {
  name: "MentorForm",
  components: {ModalOverlay},
  props: {
    mentorId: Number,
    readonly: Boolean
  },
  data() {
    return {
      form: {
        name: '',
        surname: '',
        patronymic: '',
        gender: 'M',
        birth_date: null,
        soft_skills: '',
        hard_skills_id: [],
        other_info: '',
        profile_photo: null,
        job_position: ''
      },
      hard_skill_ids: [],
    };
  },
  created() {
    if (!this.readonly)
      this.fetchHardSkillIds()
    if (this.mentorId) {
      this.fetchMentorDetails(this.mentorId);
    }
  },
  methods: {
    async fetchMentorDetails(id) {
      try {
        const response = await axios.get(`anket_app/mentors/${id}/`);
        if (this.readonly)
          this.hard_skill_ids = response.data.hard_skills_ids
        this.form = { ...response.data }
      } catch (e) {
        alert('Ошибка при загрузке данных наставника');
      }
    },
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

<style scoped lang="scss">
.form-content {
  display: flex;
  flex-direction: row;
  grid-gap: 30px;
}

.hard-skill-list {
  display: flex;
  flex-direction: column;
  width: 230px;
  padding: 4px;
  border: 1px solid #ccc;
  border-radius: 10px;
  background: #ffffff;
  color: #32312e;
  outline: none;
}

.mentor-info-img-container {
  height: 160px;
  width: 160px;
  overflow: hidden;
}

.mentor-info-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  align-items: center;
}

.mentor-info-img-container-main {
  display: flex;
  justify-content: left;
  width: 230px;
  outline: none;
}
</style>