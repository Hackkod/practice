<template>
  <div>
    <HeaderComponent title="Работа" :tabs="tabs" @openForm="createWork" />
    <WorkList :works="works" @updateWorks="fetchWorks"/>
    <WorkForm v-if="showForm" @close="closeForm" @save="saveWork"/>
    <PaginatorTable :next="next" :previous="previous" @changePage="fetchWorks" />
  </div>
</template>

<script>
import axios from "@/plugins/axios";
import WorkList from "@/components/WorkList.vue";
import HeaderComponent from "@/components/HeaderComponent.vue";
import WorkForm from "@/components/WorkForm.vue";
import PaginatorTable from "@/components/PaginatorTable.vue";

export default {
  components: {PaginatorTable, WorkForm, HeaderComponent, WorkList},
  data() {
    return {
      works: [],
      showForm: false,
      tabs: [
        { name: 'Таблица' }
      ],
      next: null,
      previous: null,
      currentPage: 1,
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
    async fetchWorks(url = `event_app/works/?page=${this.currentPage}`) {
      try {
        const response = await axios.get(url);
        this.works = response.data.results;
        this.next = response.data.next;
        this.previous = response.data.previous;
      } catch (e) {
        alert('Ошибка при получении списка работ')
      }
    },
    // async nextPage(){
    //   if (this.next) {
    //     this.currentPage += 1;
    //     await this.fetchWorks(this.next);
    //   }
    // },
    // async previousPage(){
    //   if (this.previous) {
    //     this.currentPage -= 1;
    //     await this.fetchWorks(this.previous);
    //   }
    // },
  }
}
</script>

<style lang="scss" scoped>

</style>