<template>
  <modal-overlay @close="close" @submit="save" :readonly="readonly">
    <modal-header>
      {{
        readonly
          ? "Просмотр работы"
          : workId
            ? "Редактирование работы"
            : "Создание новой работы"
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
        <v-select
          v-else
          class="form-input student-select"
          label="Студент*"
          :item-title="truncatedName"
          item-value="id"
          density="compact"
          variant="outlined"
          v-model="form.student"
          :items="students"
          :rules="[rules.required]"
        ></v-select>
        <v-text-field
          v-if="readonly"
          class="form-input mentor"
          label="Наставник"
          variant="outlined"
          density="compact"
          v-model="mentor_full_name"
          :readonly="readonly"
        ></v-text-field>
        <v-select
          v-else
          class="form-input mentor"
          label="Наставник*"
          :item-title="truncatedName"
          item-value="id"
          density="compact"
          variant="outlined"
          v-model="form.mentor"
          :items="mentors"
          :rules="[rules.required]"
        ></v-select>
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
          class="form-input position"
          label="Позиция*"
          placeholder="Младший разработчик"
          variant="outlined"
          density="compact"
          maxlength="25"
          v-model="form.position"
          :readonly="readonly"
          :rules="[rules.required]"
        ></v-text-field>
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

export default {
  name: "WorkForm",
  props: {
    // eslint-disable-next-line vue/require-default-prop
    workId: Number,
    readonly: Boolean,
  },
  emits: ["close", "save"],
  data() {
    return {
      form: {
        name: "",
        student: null,
        mentor: null,
        type: null,
        position: "",
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
          name: "Договор",
          value: "Договор",
        },
        {
          name: "Штаб",
          value: "Штаб",
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
    workId: {
      immediate: true,
      handler(newWorkId) {
        if (newWorkId) {
          this.fetchWorkDetails(newWorkId);
        }
      },
    },
  },
  methods: {
    fetchWorkDetails(id) {
      axios
        .get(`event_app/works/${id}/`)
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
    fetchStudents() {
      axios
        .get("anket_app/students/")
        .then((response) => {
          this.students = response.data.results;
          if (!this.workId && this.students.length) {
            this.form.student = this.students[0].id;
          }
        })
        .catch(() => {
          alert("Ошибка при загрузке списка студентов");
        });
    },
    fetchMentors() {
      axios
        .get("anket_app/mentors/")
        .then((response) => {
          this.mentors = response.data.results;
          if (!this.workId && this.mentors.length) {
            this.form.mentor = this.mentors[0].id;
          }
        })
        .catch(() => {
          alert("Ошибка при загрузке списка наставников");
        });
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
