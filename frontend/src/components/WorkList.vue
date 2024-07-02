<template>
  <div>
    <table-overlay>
        <thead>
        <tr class="table-headers">
          <th>Заголовок</th>
          <th>Студент</th>
          <th>Наставник</th>
          <th>Тип</th>
          <th>Дата начала/окончания</th>
          <th class="actions-column">Действия</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="work in works" :key="work.id">
          <td>{{ work.name }}</td>
          <td>{{ work.student_full.name }}</td>
          <td>{{ work.mentor_full.name }}</td>
          <td>{{ work.type }}</td>
          <td>{{ work.start_date }} - {{ work.end_date }}</td>
          <td>
            <div class="actions-btns">
              <button @click="editWork(work)" class="table-btn ">
                <img :src="require('@/assets/img/EditIcon.svg')" alt="Иконка редактирования" width="30" height="30">
              </button>
              <button @click="confirmDelete(work)" class="table-btn">
                <img :src="require('@/assets/img/DeleteIcon.svg')" alt="Иконка удаления" width="30" height="30">
              </button>
            </div>
          </td>
        </tr>
        </tbody>
    </table-overlay>
    <work-form v-if="showForm" :work="selectedWork" @close="closeForm" @save="saveWork"/>
  </div>
</template>

<script>
import WorkForm from "@/components/WorkForm.vue";
import axios from "@/plugins/axios";
import TableOverlay from "@/components/UI/TableOverlay.vue";

export default {
  name: 'WorkList',
  props: {
    works: Array,
  },
  components: {
    TableOverlay,
    WorkForm,
  },
  data() {
    return {
      showForm: false,
      selectedWork: null,
    }
  },
  methods: {
    editWork(work) {
      this.selectedWork = work;
      this.showForm = true;
    },
    closeForm() {
      this.showForm = false;
    },
    async saveWork(updatedWork) {
      try {
        await axios.put(`event_app/works/${updatedWork.id}/`, updatedWork);
        this.$emit('updateWorks');
      } catch (e) {
        alert('Ошибка при изменении работы');
      }
      this.closeForm();
    },
    async deleteWork(work) {
      try {
        await axios.delete(`event_app/works/${work.id}/`);
        this.$emit('updateWorks');
      } catch (e) {
        alert('Ошибка при удалении работы')
      }
    },
    confirmDelete(work) {
      if (confirm(`Вы уверены, что хотите удалить работу ${work.name}?`)) {
        this.deleteWork(work);
      }
    },
  }
}
</script>

<style lang="scss" scoped>
tr {
  background-color: #fff;
  box-shadow: 0 4px 20px 0 #f2f1f3;
  font-size: 20px;
}

.table-headers {
  background-color: #f9f9f9;
}

th, td {
  color: #32312e;
  padding: 12px 8px;
  text-align: left;
  border: none;
  white-space: nowrap;
}

th:first-child, td:first-child {
  border-radius: 20px 0 0 20px;
  padding-left: 20px;
}
th:last-child, td:last-child {
  border-radius: 0 20px 20px 0;
}

th {
  background-color: #f9f9f9;
  font-size: 24px;
}

tr:hover {
  background-color: #faf8ff;
}

.actions-btns {
  display: flex;
  grid-gap: 40px;
}
</style>
