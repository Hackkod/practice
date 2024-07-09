<template>
  <modal-overlay @close="close" @submit="save" :readonly="readonly">
    <modal-header>
      {{
        readonly
          ? "Просмотр наставника"
          : mentorId
            ? "Редактирование наставника"
            : "Создание нового наставника"
      }}
    </modal-header>
    <div class="form-content">
      <div class="first-column">
        <v-text-field
            class="form-input surname"
            label="Фамилия*"
            placeholder="Иванов"
            variant="outlined"
            density="compact"
            v-model="form.surname"
            maxlength="25"
            :readonly="readonly"
            :rules="[rules.required, rules.min2ch]"
        ></v-text-field>
        <v-text-field
            class="form-input name"
            label="Имя*"
            placeholder="Иван"
            variant="outlined"
            density="compact"
            v-model="form.name"
            maxlength="25"
            :readonly="readonly"
            :rules="[rules.required, rules.min2ch]"
        ></v-text-field>
        <v-text-field
            class="form-input patronymic"
            label="Отчество*"
            placeholder="Иванович"
            variant="outlined"
            density="compact"
            v-model="form.patronymic"
            maxlength="25"
            :readonly="readonly"
            :rules="[rules.required, rules.min2ch]"
        ></v-text-field>
        <v-text-field
            v-if="readonly"
            class="form-input gender"
            label="Пол"
            variant="outlined"
            density="compact"
            v-model="form.gender"
            :readonly="readonly"
        ></v-text-field>
        <v-select
            v-else
            class="form-input gender-select"
            label="Пол*"
            item-title="name"
            item-value="value"
            density="compact"
            variant="outlined"
            v-model="form.gender"
            :items="genders"
            :rules="[rules.required]"
        ></v-select>
        <v-text-field
            class="form-input birth_date"
            label="Дата рождения*"
            variant="outlined"
            density="compact"
            type="date"
            v-model="form.birth_date"
            :readonly="readonly"
            :rules="[rules.required, rules.birthDate]"
        ></v-text-field>
        <v-text-field
            class="form-input job_position"
            label="Должность*"
            placeholder="Младший разработчик"
            variant="outlined"
            density="compact"
            maxlength="50"
            v-model="form.job_position"
            :readonly="readonly"
            :rules="[rules.required]"
        ></v-text-field>
      </div>
      <div :class="secondColumnClass(readonly)">
        <v-img
          v-if="readonly"
          class="profile_photo"
          aspect-ratio="1/1"
          cover
          :width="180"
          :src="form.profile_photo"
        ></v-img>
        <v-file-input
          v-else
          class="form-input profile_photo-select"
          label="Фотография наставника"
          variant="outlined"
          density="compact"
          counter
          show-size
          clearable
          @change="handleFileChange"
        >
          <template #selection>
            {{ truncFile }}
          </template>
        </v-file-input>
        <v-textarea
          class="form-input other_info"
          label="Дополнительная информация"
          variant="outlined"
          density="compact"
          rows="2"
          no-resize
          v-model="form.other_info"
          :readonly="readonly"
        ></v-textarea>
        <v-textarea
            class="form-input soft_skills"
            label="Софт скиллы*"
            variant="outlined"
            density="compact"
            rows="2"
            no-resize
            v-model="form.soft_skills"
            :readonly="readonly"
            :rules="[rules.required]"
        ></v-textarea>
        <v-select
            v-if="!readonly"
            class="form-input hard_skills"
            label="Хард скиллы*"
            item-title="skill_name"
            item-value="id"
            density="compact"
            variant="outlined"
            multiple
            v-model="form.hard_skills_id"
            :items="hard_skill_ids"
            :rules="[rules.notEmptyArr]"
        >
          <template #selection="{ item, index }">
            <v-chip v-if="index < 1">
              <span>{{ item.title }}</span>
            </v-chip>
            <span
              v-if="index === 1"
              class="text-grey text-caption align-self-center"
            >
              (+{{ form.hard_skills_id.length - 1 }} others)
            </span>
          </template>
          <template #append>
           <span class="append-icon">
             <v-icon color="#96989f" @click.prevent="openAddHardSkillForm" size="large">mdi-plus</v-icon>
           </span>
          </template>
        </v-select>
      </div>
    </div>
    <div class="hard-skills-chips" v-if="readonly">
      <v-chip
        class="skill-chip"
        v-for="skill in hard_skill_ids"
        :key="skill.id"
      >
        <span>{{ skill.skill_name }}</span>
      </v-chip>
    </div>
  </modal-overlay>
  <hard-skill-form
    v-if="showAddHardSkillForm"
    @close="closeAddHardSkillForm"
    @refresh-hard-skills="fetchHardSkillIds"
  />
</template>

<script>
import ModalOverlay from "@/components/UI/ModalOverlay.vue";
import axios from "@/plugins/axios";
import HardSkillForm from "@/components/HardSkillForm.vue";

export default {
  name: "MentorForm",
  components: { HardSkillForm, ModalOverlay },
  props: {
    // eslint-disable-next-line vue/require-default-prop
    mentorId: Number,
    readonly: Boolean,
  },
  emits: ["save", "close"],
  data() {
    return {
      form: {
        name: "",
        surname: "",
        patronymic: "",
        gender: null,
        birth_date: null,
        soft_skills: "",
        hard_skills_id: [],
        other_info: "",
        profile_photo: null,
        job_position: "",
      },
      genders: [
        {
          name: "Мужской",
          value: "Мужской",
        },
        {
          name: "Женский",
          value: "Женский",
        },
      ],
      hard_skill_ids: [],
      showAddHardSkillForm: false,
      rules: {
        required: value => !!value || 'Обязательно.',
        min2ch: value => (value && value.length >= 2) || 'Не менее 2 символов.',
        notEmptyArr: value => Array.isArray(value) && value.length > 0 || 'Обязательно.',
        birthDate: value => {
          const currentDate = new Date()
          const birthDate = new Date(value)
          if (birthDate > currentDate) {
            return `Не позже текущей даты.`
          }
          const minAge = 14
          let age = currentDate.getFullYear() - birthDate.getFullYear()
          const monthDiff = currentDate.getMonth() - birthDate.getMonth()
          const dayDiff = currentDate.getDate() - birthDate.getDate()

          if (monthDiff < 0 || (monthDiff === 0 && dayDiff < 0)) {
            age--
          }
          return age >= minAge || `Не менее 14 лет.`
        },
      },
    }
  },
  created() {
    if (!this.readonly) this.fetchHardSkillIds();
    if (this.mentorId) {
      this.fetchMentorDetails(this.mentorId);
    }
  },
  computed: {
    truncFile() {
      if (this.form.profile_photo && this.form.profile_photo.name) {
        const fullName = this.form.profile_photo.name;
        return fullName.length > 8 ? fullName.slice(0, 8) + "..." : fullName;
      }
      return "";
    },
  },
  methods: {
    secondColumnClass(readonly) {
      return readonly ? "second-column-readonly" : "second-column";
    },
    async fetchMentorDetails(id) {
      try {
        const response = await axios.get(`anket_app/mentors/${id}/`);
        this.form = { ...response.data };
        if (this.readonly) this.hard_skill_ids = response.data.hard_skills_ids;
        else
          this.form.hard_skills_id = response.data.hard_skills_ids.map(
            (skill) => skill.id,
          );
      } catch (e) {
        alert("Ошибка при загрузке данных наставника");
      }
    },
    async fetchHardSkillIds() {
      try {
        const response = await axios.get("hard_skill_app/hard_skills/");
        this.hard_skill_ids = response.data.results;
      } catch (e) {
        alert("Ошибка при загрузке списка хард скиллов");
      }
    },
    handleFileChange(event) {
      this.form.profile_photo = event.target.files[0];
    },
    async save() {
      const formData = new FormData();
      Object.keys(this.form).forEach((key) => {
        const value = this.form[key];
        if (Array.isArray(value)) {
          if (value.length > 0) {
            value.forEach((item) => {
              formData.append(key, item);
            });
          }
        } else if (value !== null && key !== "profile_photo") {
          formData.append(key, value);
        }
      });
      if (this.form.profile_photo) {
        formData.append("profile_photo", this.form.profile_photo);
      }
      this.$emit("save", formData);
    },
    close() {
      this.$emit("close");
    },
    openAddHardSkillForm() {
      this.showAddHardSkillForm = true;
    },
    closeAddHardSkillForm() {
      this.showAddHardSkillForm = false;
    },
  },
};
</script>

<style scoped lang="scss">
.form-content {
  display: flex;
  flex-direction: row;
  grid-gap: 30px;
}

.second-column-readonly {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.form-input {
  min-width: 225px;
  max-height: 86px;
}

.profile_photo {
  margin-bottom: 20px;
  border-radius: 50%;
  max-height: 180px;
}

.hard-skills-chips {
  max-width: 480px;
  max-height: 100px;
  overflow-y: auto;
}

.skill-chip {
  margin: 0 5px 3px 0;
}

.third-column {
  margin-left: -20px;
  display: flex;
  align-items: flex-end;
  margin-bottom: 99px;
}

.add-button {
  background-size: cover;
  display: flex;
  width: 40px;
  height: 40px;
  background-image: url("@/assets/img/AddIcon.png");
  background-color: #f0ecff;
  border-radius: 8px;
}

.append-icon {
  display: inline-block;
  vertical-align: middle;
}
</style>
