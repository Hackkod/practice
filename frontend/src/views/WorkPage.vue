<template>
  <div>
    <HeaderComponent
      title="Работа"
      :tabs="tabs"
      :active-tab="activeTab"
      :type-options="typeOptions"
      @tab-change="setActiveTab"
      @open-form="createWork"
      @update-filters="updateFilters"
    />
    <WorkList
      :works="works"
      @update-works="fetchWorks"
      @update-sort="updateSort"
      :sort-key="sortKey"
      :sort-asc="sortAsc"
    />
    <WorkForm v-if="showForm" @close="closeForm" @save="saveWork" />
    <PaginatorTable
      :total-pages="totalPages"
      :current-page="currentPage"
      @change-page="handleChangePage"
    />
  </div>
</template>

<script>
import axios from "@/plugins/axios";
import WorkList from "@/components/WorkList.vue";
import HeaderComponent from "@/components/HeaderComponent.vue";
import WorkForm from "@/components/WorkForm.vue";
import PaginatorTable from "@/components/PaginatorTable.vue";

export default {
  components: {
    PaginatorTable,
    WorkForm,
    HeaderComponent,
    WorkList,
  },
  data() {
    return {
      works: [],
      showForm: false,
      activeTab: 0,
      tabs: [{ name: "Таблица" }],
      totalPages: 0,
      currentPage: 1,
      filters: {
        searchQuery: "",
        startDate: "",
        endDate: "",
        selectedType: "",
      },
      sortKey: "",
      sortAsc: true,
      typeOptions: [
        { value: "Договор", label: "Договор" },
        { value: "Штаб", label: "Штаб" },
      ],
    };
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
        alert("Ошибка при создании работы");
      }
    },
    async fetchWorks(url = `event_app/works/?page=${this.currentPage}`) {
      try {
        const { searchQuery, startDate, endDate, selectedType } = this.filters;
        const response = await axios.get(url, {
          params: {
            page: this.currentPage,
            search: searchQuery,
            start_date: startDate,
            end_date: endDate,
            type: selectedType,
            ordering: this.sortAsc ? this.sortKey : `-${this.sortKey}`,
          },
        });
        this.works = response.data.results;
        this.totalPages = Math.ceil(response.data.count / 6);
      } catch (e) {
        alert("Ошибка при получении списка работ");
      }
    },
    updateSort(sortKey, sortAsc) {
      this.sortKey = sortKey;
      this.sortAsc = sortAsc;
      this.currentPage = 1;
      this.fetchWorks();
    },
    setActiveTab(index) {
      this.activeTab = index;
    },
    updateFilters(newFilters) {
      this.filters = newFilters;
      this.currentPage = 1;
      this.fetchWorks();
    },
    handleChangePage(page) {
      this.currentPage = page;
      this.fetchWorks();
    },
  },
};
</script>

<style lang="scss" scoped></style>
