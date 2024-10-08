<template>
  <modal-overlay @close="close" @submit="save" :readonly="readonly">
    <modal-header>
      {{
        readonly
          ? "Просмотр студента"
          : studentId
            ? "Редактирование студента"
            : "Создание нового студента"
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
          maxlength="25"
          v-model="form.surname"
          :readonly="readonly"
          :rules="[rules.required, rules.min2ch]"
        ></v-text-field>
        <v-text-field
          class="form-input name"
          label="Имя*"
          placeholder="Иван"
          variant="outlined"
          density="compact"
          maxlength="25"
          v-model="form.name"
          :readonly="readonly"
          :rules="[rules.required, rules.min2ch]"
        ></v-text-field>
        <v-text-field
          class="form-input patronymic"
          label="Отчество*"
          placeholder="Иванович"
          variant="outlined"
          density="compact"
          maxlength="25"
          v-model="form.patronymic"
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
          class="form-input establishment"
          label="Учебное учреждение*"
          placeholder="ЧувГУ"
          variant="outlined"
          density="compact"
          maxlength="25"
          v-model="form.establishment"
          :readonly="readonly"
          :rules="[rules.required]"
        ></v-text-field>
        <v-text-field
          class="form-input start_study_year"
          label="Начало обучения*"
          placeholder="2021"
          variant="outlined"
          density="compact"
          v-model="form.start_study_year"
          type="number"
          :readonly="readonly"
          :rules="[rules.required, rules.yearValid]"
        ></v-text-field>
        <v-text-field
          class="form-input end_study_year"
          label="Конец обучения*"
          placeholder="2025"
          variant="outlined"
          density="compact"
          v-model="form.end_study_year"
          type="number"
          :readonly="readonly"
          :rules="[
            rules.required,
            rules.yearValid,
            rules.endYearValid,
            rules.studyTerm,
          ]"
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
          label="Фотография студента"
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
            <v-chip v-if="index < 1" style="max-width: 78px">
              <span>{{ item.title }}</span>
            </v-chip>
            <span
              v-if="index === 1"
              class="text-grey text-caption align-self-center"
            >
              (+{{ form.hard_skills_id.length - 1 }})
            </span>
          </template>
          <template #prepend-item>
            <v-list-item title="Выбрать все" @click="toggle">
              <template #prepend>
                <v-checkbox-btn
                  :indeterminate="SomeHardSkill && !AllHardSkill"
                  :model-value="AllHardSkill"
                ></v-checkbox-btn>
              </template>
            </v-list-item>
            <v-divider class="mt-2"></v-divider>
          </template>
          <template #append>
            <span class="append-icon">
              <v-icon
                color="grey"
                @click.prevent="openAddHardSkillForm"
                size="large"
                >mdi-plus</v-icon
              >
            </span>
            <span class="append-icon">
              <v-icon color="grey" @click.prevent="removeHardSkill" size="large"
                >mdi-delete</v-icon
              >
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
  <HardSkillForm
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
  name: "StudentForm",
  components: { HardSkillForm, ModalOverlay },
  props: {
    // eslint-disable-next-line vue/require-default-prop
    studentId: Number,
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
        establishment: "",
        start_study_year: null,
        end_study_year: null,
      },
      hard_skill_ids: [],
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
      showAddHardSkillForm: false,
      rules: {
        required: (value) => !!value || "Обязательно.",
        min2ch: (value) =>
          (value && value.length >= 2) || "Не менее 2 символов.",
        notEmptyArr: (value) =>
          (Array.isArray(value) && value.length > 0) || "Обязательно.",
        birthDate: (value) => {
          const currentDate = new Date();
          const birthDate = new Date(value);
          if (birthDate > currentDate) {
            return `Не позже текущей даты.`;
          }
          const minAge = 14;
          let age = currentDate.getFullYear() - birthDate.getFullYear();
          const monthDiff = currentDate.getMonth() - birthDate.getMonth();
          const dayDiff = currentDate.getDate() - birthDate.getDate();

          if (monthDiff < 0 || (monthDiff === 0 && dayDiff < 0)) {
            age--;
          }
          return age >= minAge || `Не менее 14 лет.`;
        },
        yearValid: (value) =>
          value.toString().length === 4 || "Некорректный год.",
        endYearValid: (value) =>
          value >= this.form.start_study_year || "Год окончания раньше начала.",
        studyTerm: (value) =>
          (value - this.form.start_study_year >= 4 &&
            value - this.form.start_study_year <= 6) ||
          "Некорректный срок.",
      },
    };
  },
  created() {
    if (!this.readonly) this.fetchHardSkillIds();
    if (this.studentId) this.fetchStudentDetails(this.studentId);
  },
  computed: {
    truncFile() {
      if (this.form.profile_photo && this.form.profile_photo.name) {
        const fullName = this.form.profile_photo.name;
        return fullName.length > 8 ? fullName.slice(0, 8) + "..." : fullName;
      }
      return "";
    },
    SomeHardSkill() {
      return this.hard_skill_ids.length > 0;
    },
    AllHardSkill() {
      return this.hard_skill_ids.length === this.form.hard_skills_id.length;
    },
  },
  methods: {
    secondColumnClass(readonly) {
      return readonly ? "second-column-readonly" : "second-column";
    },
    async fetchStudentDetails(id) {
      try {
        const response = await axios.get(`anket_app/students/${id}/`);
        this.form = { ...response.data };
        if (this.readonly) this.hard_skill_ids = response.data.hard_skills_ids;
        else
          this.form.hard_skills_id = response.data.hard_skills_ids.map(
            (skill) => skill.id,
          );
      } catch (e) {
        alert("Ошибка при загрузке данных студента");
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
      console.log(this.form);
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
    async removeHardSkill() {
      try {
        for (const id of this.form.hard_skills_id) {
          await axios.delete(`hard_skill_app/hard_skills/${id}/`);
        }
        await this.fetchHardSkillIds();
        this.form.hard_skills_id = [];
      } catch (e) {
        alert("Ошибка при удалении хард скиллов");
      }
    },
    toggle() {
      if (this.AllHardSkill) {
        this.form.hard_skills_id = [];
      } else {
        this.form.hard_skills_id = this.hard_skill_ids.map((skill) => skill.id);
      }
    },
  },
};
</script>

<style lang="scss" scoped>
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
  min-width: 250px;
  max-width: 250px;
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
  margin-bottom: 223px;
}

.append-icon {
  display: inline-block;
  vertical-align: middle;
}
</style>
