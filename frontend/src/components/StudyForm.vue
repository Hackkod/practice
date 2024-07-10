<template>
  <modal-overlay @close="close" @submit="save" :readonly="readonly">
    <modal-header>
      {{
        readonly
          ? "Просмотр обучения"
          : studyId
            ? "Редактирование обучения"
            : "Создание нового обучения"
      }}
    </modal-header>
    <div class="form-content">
      <div class="first-column">
        <v-text-field
          class="form-input name"
          label="Заголовок*"
          placeholder="#1111"
          variant="outlined"
          density="compact"
          maxlength="25"
          v-model="form.name"
          :readonly="readonly"
          :rules="[rules.required]"
        ></v-text-field>
        <v-text-field
          v-if="readonly"
          class="form-input student"
          label="Студент"
          variant="outlined"
          density="compact"
          v-model="student_full_name"
          :readonly="readonly"
        ></v-text-field>
        <v-autocomplete
            v-else
            class="form-input student-select"
            clearable
            label="Студент*"
            :item-title="truncatedName"
            item-value="id"
            density="compact"
            variant="outlined"
            v-model="form.student"
            :items="students"
            :rules="[rules.required]"
            @update:search="(search) => fetchStudents(search)"
        ></v-autocomplete>
        <v-text-field
          v-if="readonly"
          class="form-input mentor"
          label="Наставник"
          variant="outlined"
          density="compact"
          v-model="mentor_full_name"
          :readonly="readonly"
        ></v-text-field>
        <v-autocomplete
            v-else
            class="form-input mentor"
            clearable
            label="Наставник*"
            :item-title="truncatedName"
            item-value="id"
            density="compact"
            variant="outlined"
            v-model="form.mentor"
            :items="mentors"
            :rules="[rules.required]"
            @update:search="(search) => fetchMentors(search)"
        ></v-autocomplete>
        <v-text-field
          v-if="readonly"
          class="form-input type"
          label="Тип"
          variant="outlined"
          density="compact"
          v-model="form.type"
          :readonly="readonly"
        ></v-text-field>
        <v-select
          v-else
          class="form-input type"
          label="Тип*"
          item-title="name"
          item-value="value"
          density="compact"
          variant="outlined"
          v-model="form.type"
          :items="types"
          :rules="[rules.required]"
        ></v-select>
      </div>
      <div class="second-column">
        <v-text-field
          class="form-input start_date"
          label="Дата начала*"
          variant="outlined"
          density="compact"
          type="date"
          v-model="form.start_date"
          :readonly="readonly"
          :rules="[rules.required]"
        ></v-text-field>
        <v-text-field
          class="form-input end_date"
          label="Дата окончания*"
          variant="outlined"
          density="compact"
          type="date"
          v-model="form.end_date"
          :readonly="readonly"
          :rules="[rules.required, rules.endDateValid]"
        ></v-text-field>
        <v-textarea
          class="form-input description"
          label="Описание"
          variant="outlined"
          density="compact"
          rows="2"
          no-resize
          v-model="form.description"
          :readonly="readonly"
        ></v-textarea>
      </div>
    </div>
  </modal-overlay>
</template>

<script>
import axios from "@/plugins/axios";
import { debounce } from "lodash";

export default {
  name: "StudyForm",
  props: {
    // eslint-disable-next-line vue/require-default-prop
    studyId: Number,
    readonly: Boolean,
  },
  emits: ["save", "close"],
  data() {
    return {
      form: {
        name: "",
        student: null,
        mentor: null,
        type: null,
        start_date: null,
        end_date: null,
        description: "",
      },
      student_full_name: "",
      mentor_full_name: "",
      students: [],
      mentors: [],
      types: [
        {
          name: "Практика",
          value: "Практика",
        },
        {
          name: "Стажировка",
          value: "Стажировка",
        },
      ],
      rules: {
        required: (value) => !!value || "Обязательно.",
        endDateValid: (value) =>
          value >= this.form.start_date || "Дата окончания раньше начала.",
      },
    };
  },
  created() {
    if (!this.readonly) this.fetchStudents();
    if (!this.readonly) this.fetchMentors();
  },
  watch: {
    studyId: {
      immediate: true,
      handler(newStudyId) {
        if (newStudyId) {
          this.fetchStudyDetails(newStudyId);
        }
      },
    },
  },
  methods: {
    fetchStudyDetails(id) {
      axios
        .get(`event_app/studies/${id}/`)
        .then((response) => {
          const data = response.data;

          if (this.readonly) {
            this.student_full_name = this.truncatedName(
              data.student_full || {},
            );
            this.mentor_full_name = this.truncatedName(data.mentor_full || {});
          }

          this.form = { ...data };
          this.form.student = data.student_full ? data.student_full.id : null;
          this.form.mentor = data.mentor_full ? data.mentor_full.id : null;
        })
        .catch(() => {
          alert("Ошибка при загрузке данных студента");
        });
    },
    fetchStudents: debounce(async function (search = "") {
      try {
        if (this.form.student) {
          const studentData = await this.fetchStudentById(this.form.student);
          this.students = [studentData];
        } else {
          const response = await axios.get("anket_app/students/", {
            params: { search: search, page_size: 10 },
          });
          this.students = response.data.results;
        }
      } catch {
        alert("Ошибка при загрузке списка студентов");
      }
    }, 300),
    fetchMentors: debounce(async function (search = "") {
      try {
        if (this.form.mentor) {
          const mentorData = await this.fetchMentorById(this.form.mentor);
          this.mentors = [mentorData];
        } else {
          const response = await axios.get("anket_app/mentors/", {
            params: { search: search, page_size: 10 },
          });
          this.mentors = response.data.results;
        }
      } catch {
        alert("Ошибка при загрузке списка наставников");
      }
    }, 300),
    async fetchStudentById(id) {
      const response = await axios.get(`anket_app/students/${id}/`);
      return response.data;
    },
    async fetchMentorById(id) {
      const response = await axios.get(`anket_app/mentors/${id}/`);
      return response.data;
    },
    async save() {
      this.$emit("save", this.form);
    },
    truncatedName(person) {
      if (person.surname && person.name && person.patronymic) {
        return (
          person.surname +
          " " +
          person.name[0] +
          "." +
          person.patronymic[0] +
          "."
        );
      } else {
        return "";
      }
    },
    close() {
      this.$emit("close");
    },
  },
};
</script>

<style scoped>
.form-input {
  min-width: 225px;
  max-height: 86px;
}

.form-content {
  display: flex;
  flex-direction: row;
  grid-gap: 30px;
}
</style>
