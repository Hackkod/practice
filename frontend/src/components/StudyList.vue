<template>
  <div>
    <table-overlay>
      <thead>
      <tr>
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
        <td>
          <div class="table-btns">
            <button @click="editStudy(study)">
              <img :src="require('@/assets/img/EditIcon.svg')" alt="Иконка редактирования" width="24" height="24">
            </button>
            <button @click="confirmDelete(study)">
              <img :src="require('@/assets/img/DeleteIcon.svg')" alt="Иконка удаления" width="24" height="24">
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

export default {
  name: 'StudyList',
  props: {
    studies: Array,
  },
  components: {
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

</style>
