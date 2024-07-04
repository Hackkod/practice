<template>
  <div>
    <HeaderComponent title="Стажировки и практики" :tabs="tabs" :activeTab="activeTab" @tabChange="setActiveTab" @openForm="createStudy" />
    <studyList :studies="studies" @updateStudies="fetchStudies"/>
    <studyForm v-if="showForm" @close="closeForm" @save="saveStudy"/>
    <PaginatorTable :next="next" :previous="previous" @changePage="fetchStudies" />
  </div>
</template>

<script>
import axios from "@/plugins/axios";
import StudyList from "@/components/StudyList.vue";
import HeaderComponent from "@/components/HeaderComponent.vue";
import PaginatorTable from "@/components/PaginatorTable.vue";
import StudyForm from "@/components/StudyForm.vue";

export default {
  components: {StudyForm, PaginatorTable, HeaderComponent, StudyList},
  data() {
    return {
      studies: [],
      showForm: false,
      activeTab: 0,
      tabs: [
        { name: 'Таблица' }
      ],
      next: null,
      previous: null,
      currentPage: 1,
    }
  },
  created() {
    this.fetchStudies();
  },
  methods: {
    createStudy() {
      this.showForm = true;
    },
    closeForm() {
      this.showForm = false;
    },
    async saveStudy(newStudy) {
      try {
        await axios.post(`event_app/studies/`, newStudy);
        await this.fetchStudies();
        this.closeForm();
      } catch (e) {
        alert('Ошибка при создании обучения');
      }
    },
    async fetchStudies(url = `event_app/studies/?page=${this.currentPage}`) {
      try {
        const response = await axios.get(url);
        this.studies = response.data.results;
        this.next = response.data.next;
        this.previous = response.data.previous;
      } catch (e) {
        alert('Ошибка при получении списка обучений')
      }
    },
    setActiveTab(index) {
      this.activeTab = index;
    },
    addStudyToList(study) {
      this.studies.push(study);
    }
  }
}
</script>

<style lang="scss" scoped>

</style>