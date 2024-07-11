<template>
  <div>
    <table-overlay>
      <thead>
        <tr>
          <th
            @click="sortBy('surname')"
            :class="{ sortable: true, sorted: localSortKey === 'surname' }"
          >
            ФИО
            <v-icon v-if="localSortKey === 'surname'">
              {{ localSortAsc ? "mdi-chevron-up" : "mdi-chevron-down" }}
            </v-icon>
          </th>
          <th
            @click="sortBy('establishment')"
            :class="{
              sortable: true,
              sorted: localSortKey === 'establishment',
            }"
          >
            Учреждение
            <v-icon v-if="localSortKey === 'establishment'">
              {{ localSortAsc ? "mdi-chevron-up" : "mdi-chevron-down" }}
            </v-icon>
          </th>
          <th
            @click="sortBy('start_study_year')"
            :class="{
              sortable: true,
              sorted: localSortKey === 'start_study_year',
            }"
          >
            Начало/Конец обучения
            <v-icon v-if="localSortKey === 'start_study_year'">
              {{ localSortAsc ? "mdi-chevron-up" : "mdi-chevron-down" }}
            </v-icon>
          </th>
          <th
            @click="sortBy('course')"
            :class="{ sortable: true, sorted: localSortKey === 'course' }"
          >
            Курс
            <v-icon v-if="localSortKey === 'course'">
              {{ localSortAsc ? "mdi-chevron-up" : "mdi-chevron-down" }}
            </v-icon>
          </th>
          <th class="actions-column">Действия</th>
        </tr>
      </thead>
      <tbody>
        <tr
          class="row-content"
          v-for="student in sortedStudents"
          :key="student.id"
          @click="this.$emit('viewStudent', student)"
        >
          <td class="td-info">
            <div class="line-info">
              <img :src="student.profile_photo" alt="" class="line-photo" />
              <span>{{ truncatedName(student) }}</span>
            </div>
          </td>
          <td>{{ truncatedEstablishment(student) }}</td>
          <td>{{ student.start_study_year }} - {{ student.end_study_year }}</td>
          <td>{{ student.course }}</td>
          <td>
            <div class="table-btns">
              <button @click.stop="editStudent(student)">
                <img
                  :src="require('@/assets/img/EditIcon.svg')"
                  alt="Иконка редактирования"
                  width="24"
                  height="24"
                />
              </button>
              <button @click.stop="confirmDelete(student)">
                <img
                  :src="require('@/assets/img/DeleteIcon.svg')"
                  alt="Иконка удаления"
                  width="24"
                  height="24"
                />
              </button>
            </div>
          </td>
        </tr>
      </tbody>
    </table-overlay>
    <student-form
      v-if="showForm"
      :student="selectedStudent"
      @close="closeForm"
      @save="saveStudent"
    />
  </div>
</template>

<script>
import axios from "@/plugins/axios";
import StudentForm from "@/components/StudentForm.vue";
import TableOverlay from "@/components/UI/TableOverlay.vue";

export default {
  name: "StudentList",
  props: {
    // eslint-disable-next-line vue/require-default-prop
    students: Array,
    // eslint-disable-next-line vue/require-default-prop
    sortKey: String,
    sortAsc: Boolean,
  },
  components: {
    TableOverlay,
    StudentForm,
  },
  emits: ["editStudent", "updateStudents", "update-sort"],
  data() {
    return {
      showForm: false,
      selectedStudent: null,
      localSortKey: this.sortKey,
      localSortAsc: this.sortAsc,
    };
  },
  computed: {
    sortedStudents() {
      const sorted = [...this.students];
      if (this.localSortKey) {
        sorted.sort((a, b) => {
          let line = 1;
          if (!this.localSortAsc) line = -1;
          let a_str, b_str;

          if (this.localSortKey === "start_study_year") {
            a_str = `${a.start_study_year}-${a.end_study_year}`;
            b_str = `${b.start_study_year}-${b.end_study_year}`;
          } else {
            a_str = a[this.localSortKey];
            b_str = b[this.localSortKey];
          }

          if (a_str < b_str) return -1 * line;
          if (a_str > b_str) return line;
          return 0;
        });
      }
      return sorted;
    },
  },
  methods: {
    editStudent(student) {
      this.$emit("editStudent", student);
    },
    closeForm() {
      this.showForm = false;
    },
    async saveStudent(updatedStudent) {
      try {
        console.log(updatedStudent);
        await axios.put(
          `anket_app/students/${updatedStudent.id}/`,
          updatedStudent,
        );
        this.$emit("updateStudents");
      } catch (e) {
        alert("Ошибка при изменении студента");
      }
      this.closeForm();
    },
    async deleteStudent(student) {
      try {
        await axios.delete(`anket_app/students/${student.id}/`);
        this.$emit("updateStudents");
      } catch (e) {
        alert("Ошибка при удалении студента");
      }
    },
    confirmDelete(student) {
      if (confirm(`Вы уверены, что хотите удалить студента ${student.name}?`)) {
        this.deleteStudent(student);
      }
    },
    truncatedName(student) {
      const fullName =
        student.surname + " " + student.name + " " + student.patronymic;
      return fullName.length > 22 ? fullName.slice(0, 22) + "..." : fullName;
    },
    truncatedEstablishment(student) {
      const establish = student.establishment;
      return establish.length > 22 ? establish.slice(0, 22) + "..." : establish;
    },
    sortBy(key) {
      if (this.localSortKey === key) {
        this.localSortAsc = !this.localSortAsc;
      } else {
        this.localSortKey = key;
        this.localSortAsc = true;
      }
      this.$emit("update-sort", this.localSortKey, this.localSortAsc);
    },
  },
};
</script>

<style lang="scss" scoped>
th {
  cursor: pointer;
  position: relative;
}

th.sortable:hover {
  background-color: #f5f5f6;
}

th.sorted {
  font-weight: bold;
}

th span {
  margin-left: 5px;
  font-size: 0.8em;
}
</style>
