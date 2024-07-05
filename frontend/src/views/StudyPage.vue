<template>
  <div>
    <HeaderComponent
        title="Стажировки и практики"
        :tabs="tabs"
        :activeTab="activeTab"
        :typeOptions="typeOptions"
        @tabChange="setActiveTab"
        @openForm="createStudy"
        @updateFilters="updateFilters"
    />
    <studyList
        :studies="studies"
        @updateStudies="fetchStudies"
    />
    <studyForm
        v-if="showForm"
        @close="closeForm"
        @save="saveStudy"
    />
    <PaginatorTable
        :totalPages="totalPages"
        :currentPage="currentPage"
        @changePage="handleChangePage"
    />
  </div>
</template>

<script>
import axios from "@/plugins/axios";
import StudyList from "@/components/StudyList.vue";
import HeaderComponent from "@/components/HeaderComponent.vue";
import PaginatorTable from "@/components/PaginatorTable.vue";
import StudyForm from "@/components/StudyForm.vue";

export default {
  components: {
    StudyForm,
    PaginatorTable,
    HeaderComponent,
    StudyList
  },
  data() {
    return {
      studies: [],
      showForm: false,
      activeTab: 0,
      tabs: [
        { name: 'Таблица' }
      ],
      totalPages: 0,
      currentPage: 1,
      filters: {
        searchQuery: '',
        startDate: '',
        endDate: '',
        selectedType: ''
      },
      typeOptions: [
        { value: 'PRACTICE', label: 'Practice' },
        { value: 'INTERNSHIP', label: 'Internship' }
      ]
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
        const { searchQuery, startDate, endDate, selectedType } = this.filters;
        const response = await axios.get(url, {
          params: {
            page: this.currentPage,
            search: searchQuery,
            start_date: startDate,
            end_date: endDate,
            type: selectedType
          }
        });
        this.studies = response.data.results;
        this.totalPages = Math.ceil(response.data.count / 6);
      } catch (e) {
        alert('Ошибка при получении списка обучений')
      }
    },
    setActiveTab(index) {
      this.activeTab = index;
    },
    updateFilters(newFilters) {
      this.filters = newFilters;
      this.fetchStudies();
    },
    handleChangePage(page) {
      this.currentPage = page;
      this.fetchStudies();
    }
  }
}
</script>

<style lang="scss" scoped>

</style>