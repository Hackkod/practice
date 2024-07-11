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
            @click="sortBy('gender')"
            :class="{ sortable: true, sorted: localSortKey === 'gender' }"
          >
            Пол
            <v-icon v-if="localSortKey === 'gender'">
              {{ localSortAsc ? "mdi-chevron-up" : "mdi-chevron-down" }}
            </v-icon>
          </th>
          <th
            @click="sortBy('job_position')"
            :class="{ sortable: true, sorted: localSortKey === 'job_position' }"
          >
            Должность
            <v-icon v-if="localSortKey === 'job_position'">
              {{ localSortAsc ? "mdi-chevron-up" : "mdi-chevron-down" }}
            </v-icon>
          </th>
          <th
            @click="sortBy('birth_date')"
            :class="{ sortable: true, sorted: localSortKey === 'birth_date' }"
          >
            Дата рождения
            <v-icon v-if="localSortKey === 'birth_date'">
              {{ localSortAsc ? "mdi-chevron-up" : "mdi-chevron-down" }}
            </v-icon>
          </th>
          <th class="actions-column">Действия</th>
        </tr>
      </thead>
      <tbody>
        <tr
          class="row-content"
          v-for="mentor in sortedMentors"
          :key="mentor.id"
          @click="this.$emit('viewMentor', mentor)"
        >
          <td class="td-info">
            <div class="line-info">
              <img :src="mentor.profile_photo" alt="" class="line-photo" />
              <span>{{ truncatedName(mentor) }}</span>
            </div>
          </td>
          <td>{{ mentor.gender }}</td>
          <td>{{ mentor.job_position }}</td>
          <td>{{ mentor.birth_date }}</td>
          <td>
            <div class="table-btns">
              <button @click.stop="editMentor(mentor)">
                <img
                  :src="require('@/assets/img/EditIcon.svg')"
                  alt="Иконка редактирования"
                  width="24"
                  height="24"
                />
              </button>
              <button @click.stop="confirmDelete(mentor)">
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
    <mentor-form
      v-if="showForm"
      :student="selectedMentor"
      @close="closeForm"
      @save="saveMentor"
    />
  </div>
</template>

<script>
import axios from "@/plugins/axios";
import MentorForm from "@/components/MentorForm.vue";
import TableOverlay from "@/components/UI/TableOverlay.vue";

export default {
  name: "MentorList",
  props: {
    // eslint-disable-next-line vue/require-default-prop
    mentors: Array,
    // eslint-disable-next-line vue/require-default-prop
    sortKey: String,
    sortAsc: Boolean,
  },
  components: {
    TableOverlay,
    MentorForm,
  },
  emits: ["editMentor", "updateMentors", "update-sort"],
  data() {
    return {
      showForm: false,
      selectedMentor: null,
      localSortKey: this.sortKey,
      localSortAsc: this.sortAsc,
    };
  },
  computed: {
    sortedMentors() {
      const sorted = [...this.mentors];
      if (this.localSortKey) {
        sorted.sort((a, b) => {
          let line = 1;
          if (!this.localSortAsc) line = -1;
          let a_str, b_str;

          a_str = a[this.localSortKey];
          b_str = b[this.localSortKey];

          if (a_str < b_str) return -1 * line;
          if (a_str > b_str) return line;
          return 0;
        });
      }
      return sorted;
    },
  },
  methods: {
    editMentor(mentor) {
      this.$emit("editMentor", mentor);
    },
    closeForm() {
      this.showForm = false;
    },
    async saveMentor(updatedMentor) {
      try {
        await axios.put(
          `anket_app/mentors/${updatedMentor.id}/`,
          updatedMentor,
        );
        this.$emit("updateMentors");
      } catch (e) {
        alert("Ошибка при изменении наставника");
      }
      this.closeForm();
    },
    async deleteMentor(mentor) {
      try {
        await axios.delete(`anket_app/mentors/${mentor.id}/`);
        this.$emit("updateMentors");
      } catch (e) {
        alert("Ошибка при удалении наставника");
      }
    },
    confirmDelete(mentor) {
      if (confirm(`Вы уверены, что хотите удалить студента ${mentor.name}?`)) {
        this.deleteMentor(mentor);
      }
    },
    truncatedName(mentor) {
      const fullName =
        mentor.surname + " " + mentor.name + " " + mentor.patronymic;
      return fullName.length > 26 ? fullName.slice(0, 26) + "..." : fullName;
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
