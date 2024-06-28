<template>
  <div>
    <div>Записи работы</div>
    <div class="work" v-for="work in works" :key="work.id">
      <div><strong>Заголовок</strong> {{ work.name }}</div>
      <div><strong>Студент</strong> {{ work.student_full.name }}</div>
      <div><strong>Наставник</strong> {{ work.mentor_full.name }}</div>
      <div><strong>Дата начала</strong> {{ work.start_date }}</div>
      <div><strong>Дата конца</strong> {{ work.end_date }}</div>
      <div><strong>Тип</strong> {{ work.type }}</div>
      <div><strong>Описание</strong> {{ work.description }}</div>
      <button @click="editWork(work)">Редактировать</button>
      <button @click="confirmDelete(work)">Удалить</button>
    </div>
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
    async saveWork(work) {
      try {
        await axios.put(`event_app/works/${work.id}/`, work);
      } catch (e) {
        alert('Ошибка при изменении работы')
      }
      this.closeForm()
    },
    async deleteWork(work) {
      try {
        await axios.delete(`event_app/works/${work.id}/`);
      } catch (e) {
        alert('Ошибка при удалении работы')
      }
    },
    confirmDelete(work) {
      if (confirm(`Вы уверены, что хотите удалить ${work.name}?`)) {
        this.deleteWork(work);
      }
    },
  }
}
</script>

<style lang="scss" scoped>

</style>