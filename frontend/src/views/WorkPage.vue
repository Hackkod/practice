<template>
  <div>
    <HeaderComponent title="Работа" :tabs="tabs" @openForm="createWork" />
    <work-list :works="works" @updateWorks="fetchWorks"/>
    <work-form v-if="showForm" @close="closeForm" @save="saveWork"/>
  </div>
</template>

<script>
import axios from "@/plugins/axios";
import WorkList from "@/components/WorkList.vue";
import HeaderComponent from "@/components/HeaderComponent.vue";
import WorkForm from "@/components/WorkForm.vue";

export default {
  components: {WorkForm, HeaderComponent, WorkList},
  data() {
    return {
      works: [],
      showForm: false,
      tabs: [
        { name: 'Таблица' }
      ],
    }
  },
  created() {
    this.fetchWorks();
  },
  methods: {
    createWork() {
      this.showForm = true;
    },
    closeForm() {
      this.showForm = false;
    },
    async saveWork(newWork) {
      try {
        await axios.post(`event_app/works/`, newWork);
        await this.fetchWorks();
        this.closeForm();
      } catch (e) {
        alert('Ошибка при создании работы');
      }
    },
    async fetchWorks() {
      try {
        const response = await axios.get('event_app/works/');
        this.works = response.data;
        console.log(this.works)
      } catch (e) {
        alert('Ошибка при получении списка работ')
      }
    },
  }
}
</script>

<style lang="scss" scoped>

</style>