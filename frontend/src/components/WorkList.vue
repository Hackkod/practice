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
          v-for="work in sortedWorks"
          :key="work.id"
          @click="viewWork(work)"
        >
          <td>{{ work.name }}</td>
          <td>{{ truncatedName(work.student_full) }}</td>
          <td>{{ truncatedName(work.mentor_full) }}</td>
          <td>{{ work.type }}</td>
          <td>{{ work.start_date }} - {{ work.end_date }}</td>
          <td>
            <div class="table-btns">
              <button @click.stop="editWork(work)">
                <img
                  :src="require('@/assets/img/EditIcon.svg')"
                  alt="Иконка редактирования"
                  width="24"
                  height="24"
                />
              </button>
              <button @click.stop="confirmDelete(work)">
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
    <work-form
      v-if="showForm"
      :work-id="selectedWork"
      :readonly="readonly"
      @close="closeForm"
      @save="saveWork"
    />
  </div>
</template>

<script>
import WorkForm from "@/components/WorkForm.vue";
import axios from "@/plugins/axios";
import TableOverlay from "@/components/UI/TableOverlay.vue";

export default {
  name: "WorkList",
  props: {
    // eslint-disable-next-line vue/require-default-prop
    works: Array,
    // eslint-disable-next-line vue/require-default-prop
    sortKey: String,
    sortAsc: Boolean,
  },
  components: {
    TableOverlay,
    WorkForm,
  },
  emits: ["updateWorks", 'update-sort'],
  data() {
    return {
      showForm: false,
      selectedWork: null,
      readonly: false,
      localSortKey: this.sortKey,
      localSortAsc: this.sortAsc,
    };
  },
  computed: {
    sortedWorks() {
      const sorted = [...this.works];
      if (this.localSortKey) {
        sorted.sort((a, b) => {
          let line = 1;
          if (!this.localSortAsc) line = -1;
          let a_str, b_str;

          if (this.localSortKey === "start_date") {
            a_str = `${a.start_date}-${a.end_date}`;
            b_str = `${b.start_date}-${b.date}`;
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
    editWork(work) {
      this.selectedWork = work.id;
      this.showForm = true;
      this.readonly = false;
    },
    closeForm() {
      this.showForm = false;
      this.readonly = false;
      this.selectedWork = null;
    },
    viewWork(work) {
      this.selectedWork = work.id;
      this.readonly = true;
      this.showForm = true;
    },
    async saveWork(updatedWork) {
      try {
        await axios.put(`event_app/works/${updatedWork.id}/`, updatedWork);
        this.$emit("updateWorks");
      } catch (e) {
        alert("Ошибка при изменении работы");
      }
      this.closeForm();
    },
    async deleteWork(work) {
      try {
        await axios.delete(`event_app/works/${work.id}/`);
        this.$emit("updateWorks");
      } catch (e) {
        alert("Ошибка при удалении работы");
      }
    },
    confirmDelete(work) {
      if (confirm(`Вы уверены, что хотите удалить работу ${work.name}?`)) {
        this.deleteWork(work);
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
