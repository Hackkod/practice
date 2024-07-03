<template>
  <div>
    <HeaderComponent title="Стажировки и практики" :tabs="tabs" />
    <study-list :studies="studies" @updateStudies="fetchStudies"/>
    <PaginatorTable :next="next" :previous="previous" @changePage="fetchStudies" />
  </div>
</template>

<script>
import axios from "@/plugins/axios";
import StudyList from "@/components/StudyList.vue";
import HeaderComponent from "@/components/HeaderComponent.vue";
import PaginatorTable from "@/components/PaginatorTable.vue";

export default {
  components: {PaginatorTable, HeaderComponent, StudyList},
  data() {
    return {
      studies: [],
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
    addStudyToList(study) {
      this.studies.push(study);
    }
  }
}
</script>

<style lang="scss" scoped>

</style>