<template>
  <div>
    <table-overlay>
      <thead>
        <tr>
          <th
            @click="sortBy('name')"
            :class="{ sortable: true, sorted: localSortKey === 'name' }"
          >
            Заголовок
            <v-icon v-if="localSortKey === 'name'">
              {{ localSortAsc ? "mdi-chevron-up" : "mdi-chevron-down" }}
            </v-icon>
          </th>
          <th
            @click="sortBy('student__surname')"
            :class="{
              sortable: true,
              sorted: localSortKey === 'student__surname',
            }"
          >
            Студент
            <v-icon v-if="localSortKey === 'student__surname'">
              {{ localSortAsc ? "mdi-chevron-up" : "mdi-chevron-down" }}
            </v-icon>
          </th>
          <th
            @click="sortBy('mentor__surname')"
            :class="{
              sortable: true,
              sorted: localSortKey === 'mentor__surname',
            }"
          >
            Наставник
            <v-icon v-if="localSortKey === 'mentor__surname'">
              {{ localSortAsc ? "mdi-chevron-up" : "mdi-chevron-down" }}
            </v-icon>
          </th>
          <th
            @click="sortBy('type')"
            :class="{
              sortable: true,
              sorted: localSortKey === 'type',
            }"
          >
            Тип
            <v-icon v-if="localSortKey === 'type'">
              {{ localSortAsc ? "mdi-chevron-up" : "mdi-chevron-down" }}
            </v-icon>
          </th>
          <th
            @click="sortBy('start_date')"
            :class="{
              sortable: true,
              sorted: localSortKey === 'start_date',
            }"
          >
            Дата начала/окончания
            <v-icon v-if="localSortKey === 'start_date'">
              {{ localSortAsc ? "mdi-chevron-up" : "mdi-chevron-down" }}
            </v-icon>
          </th>
          <th class="actions-column">Действия</th>
        </tr>
      </thead>
      <tbody>
        <tr
          class="row-content"
          v-for="study in sortedStudies"
          :key="study.id"
          @click="viewStudy(study)"
        >
          <td>{{ study.name }}</td>
          <td>{{ truncatedName(study.student_full) }}</td>
          <td>{{ truncatedName(study.mentor_full) }}</td>
          <td>{{ study.type }}</td>
          <td>{{ study.start_date }} - {{ study.end_date }}</td>
          <td>
            <div class="table-btns">
              <button @click.stop="editStudy(study)">
                <img
                  :src="require('@/assets/img/EditIcon.svg')"
                  alt="Иконка редактирования"
                  width="24"
                  height="24"
                />
              </button>
              <button @click.stop="confirmDelete(study)">
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
    <study-form
      v-if="showForm"
      :study-id="selectedStudy"
      :readonly="readonly"
      @close="closeForm"
      @save="saveStudy"
    />
  </div>
</template>

<script>
import StudyForm from "@/components/StudyForm.vue";
import axios from "@/plugins/axios";
import TableOverlay from "@/components/UI/TableOverlay.vue";

export default {
  name: "StudyList",
  props: {
    // eslint-disable-next-line vue/require-default-prop
    studies: Array,
    // eslint-disable-next-line vue/require-default-prop
    sortKey: String,
    sortAsc: Boolean,
  },
  components: {
    TableOverlay,
    StudyForm,
  },
  emits: ["updateStudies", "update-sort"],
  data() {
    return {
      showForm: false,
      selectedStudy: null,
      readonly: false,
      localSortKey: this.sortKey,
      localSortAsc: this.sortAsc,
    };
  },
  computed: {
    sortedStudies() {
      const sorted = [...this.studies];
      if (this.localSortKey) {
        sorted.sort((a, b) => {
          let line = 1;
          if (!this.localSortAsc) line = -1;
          let a_str, b_str;

          if (this.localSortKey === "start_date") {
            a_str = `${a.start_date}-${a.end_date}`;
            b_str = `${b.start_date}-${b.end_date}`;
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
    editStudy(study) {
      this.selectedStudy = study.id;
      this.showForm = true;
      this.readonly = false;
    },
    closeForm() {
      this.showForm = false;
      this.readonly = false;
      this.selectedStudy = null;
    },
    viewStudy(study) {
      this.selectedStudy = study.id;
      this.readonly = true;
      this.showForm = true;
    },
    async saveStudy(updatedStudy) {
      try {
        await axios.put(`event_app/studies/${updatedStudy.id}/`, updatedStudy);
        this.$emit("updateStudies");
      } catch (e) {
        alert("Ошибка при изменении работы");
      }
      this.closeForm();
    },
    async deleteStudy(study) {
      try {
        await axios.delete(`event_app/studies/${study.id}/`);
        this.$emit("updateStudies");
      } catch (e) {
        alert("Ошибка при удалении работы");
      }
    },
    confirmDelete(study) {
      if (confirm(`Вы уверены, что хотите удалить обучение ${study.name}?`)) {
        this.deleteStudy(study);
      }
    },
    truncatedName(person) {
      const fullName =
        person.surname +
        " " +
        person.name[0] +
        "." +
        person.patronymic[0] +
        ".";
      return fullName.length > 13 ? fullName.slice(0, 13) + ".." : fullName;
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
