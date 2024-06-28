<template>
  <div>
    <div>Записи работы</div>
    <div class="study" v-for="study in studies" :key="study.id">
      <div><strong>Заголовок</strong> {{ study.name }}</div>
      <div><strong>Студент</strong> {{ study.student_full.name }}</div>
      <div><strong>Наставник</strong> {{ study.mentor_full.name }}</div>
      <div><strong>Тип</strong> {{ study.type }}</div>
      <div><strong>Дата начала</strong> {{ study.start_date }}</div>
      <div><strong>Дата окончания</strong> {{ study.end_date }}</div>
      <div><strong>Описание</strong> {{ study.description }}</div>
      <button @click="editStudy(study)">Редактировать</button>
      <button @click="confirmDelete(study)">Удалить</button>
    </div>
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
    async saveStudy(study) {
      try {
        await axios.put(`event_app/studies/${study.id}/`, study);
      } catch (e) {
        alert('Ошибка при изменении обучения')
      }
      this.closeForm()
    },
    async deleteStudy(study) {
      try {
        await axios.delete(`event_app/studies/${study.id}/`);
      } catch (e) {
        alert('Ошибка при удалении обучения')
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