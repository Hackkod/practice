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
      <tr v-for="study in studies" :key="study.id">
        <td>{{ study.name }}</td>
        <td>{{ study.student_full.name }}</td>
        <td>{{ study.mentor_full.name }}</td>
        <td>{{ study.type }}</td>
        <td>{{ study.start_date }} - {{ study.end_date }}</td>
        <td class="actions-column">
          <div class="actions-btns">
            <button @click="editStudy(study)" class="table-btn ">
              <img :src="require('@/assets/img/EditIcon.svg')" alt="Иконка редактирования" width="30" height="30">
            </button>
            <button @click="confirmDelete(study)" class="table-btn">
              <img :src="require('@/assets/img/DeleteIcon.svg')" alt="Иконка удаления" width="30" height="30">
            </button>
          </div>
        </td>
      </tr>
      </tbody>
    </table-overlay>
    <study-form v-if="showForm" :study="selectedStudy" @close="closeForm" @save="saveStudy"/>
  </div>
</template>

<script>
import StudyForm from "@/components/StudyForm.vue";
import axios from "@/plugins/axios";
import TableOverlay from "@/components/UI/TableOverlay.vue";

export default {
  name: 'StudyList',
  props: {
    studies: Array,
  },
  components: {
    TableOverlay,
    StudyForm,
  },
  data() {
    return {
      showForm: false,
      selectedStudy: null,
    }
  },
  methods: {
    editStudy(study) {
      this.selectedStudy = study;
      this.showForm = true;
    },
    closeForm() {
      this.showForm = false;
    },
    async saveStudy(updatedStudy) {
      try {
        await axios.put(`event_app/studies/${updatedStudy.id}/`, updatedStudy);
        this.$emit('updateStudies');
      } catch (e) {
        alert('Ошибка при изменении работы');
      }
      this.closeForm();
    },
    async deleteStudy(study) {
      try {
        await axios.delete(`event_app/studies/${study.id}/`);
        this.$emit('updateStudies');
      } catch (e) {
        alert('Ошибка при удалении работы')
      }
    },
    confirmDelete(study) {
      if (confirm(`Вы уверены, что хотите удалить обучение ${study.name}?`)) {
        this.deleteStudy(study);
      }
    },
  }
}
</script>

<style lang="scss" scoped>
tr {
  background-color: #fff;
  box-shadow: 0 4px 20px 0 #f2f1f3;
  font-size: 16px;
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
  font-size: 18px;
}

tr:hover {
  background-color: #faf8ff;
}

.actions-btns {
  display: flex;
  grid-gap: 35px;
}

button {
  display: flex;
  align-items: center;
}
</style>
