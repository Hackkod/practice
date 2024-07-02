<template>
  <div class="work-list">
    <table class="work-table">
      <thead>
      <tr class="table-headers">
        <th>Заголовок</th>
        <th>Студент</th>
        <th>Наставник</th>
        <th>Тип</th>
        <th>Дата начала/окончания</th>
        <th>Действия</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="work in works" :key="work.id">
        <td>{{ work.name }}</td>
        <td>{{ work.student_full.name }}</td>
        <td>{{ work.mentor_full.name }}</td>
        <td>{{ work.type }}</td>
        <td>{{ work.start_date }} - {{ work.end_date }}</td>
        <td class="actions-column">
          <button @click="editWork(work)" class="table-btn ">
            <img :src="require('@/assets/img/EditIcon.svg')" alt="Иконка редактирования" width="20" height="20">
          </button>
          <button @click="confirmDelete(work)" class="table-btn">
            <img :src="require('@/assets/img/DeleteIcon.svg')" alt="Иконка удаления" width="20" height="20">
          </button>
        </td>
      </tr>
      </tbody>
    </table>
    <work-form v-if="showForm" :work="selectedWork" @close="closeForm" @save="saveWork"/>
  </div>
</template>

<script>
import WorkForm from "@/components/WorkForm.vue";
import axios from "@/plugins/axios";

export default {
  name: 'WorkList',
  props: {
    works: Array,
  },
  components: {
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
.work-list {
  background-image: linear-gradient(#faf8ff, #faf8ff);
  background-size: calc(100% - 40px) calc(100% - 60px);
  background-position: center;
}

.work-table {
  backdrop-filter: blur(20px);
  width: 100%;
  padding: 20px;
  border-collapse: separate;
  border-spacing: 0 16px;

  tr {
    background-color: #fff;
    box-shadow: 0 4px 20px 0 #f2f1f3;
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
  }

  tr:hover {
    background-color: #f1f1f1;
  }

  .actions-column {
    display: flex;
    justify-content: space-around;
    max-width: 90px;
  }
}
</style>