<template>
  <div>
    <HeaderComponent title="Стажировки и практики" :tabs="tabs" />
    <study-list :studies="studies" @updateStudies="fetchStudies"/>
  </div>
</template>

<script>
import axios from "@/plugins/axios";
import StudyList from "@/components/StudyList.vue";
import HeaderComponent from "@/components/HeaderComponent.vue";

export default {
  components: {HeaderComponent, StudyList},
  data() {
    return {
      studies: [],
      activeTab: 0,
      tabs: [
        { name: 'Таблица' }
      ],
    }
  },
  created() {
    this.fetchStudies();
  },
  methods: {
    async fetchStudies() {
      try {
        const response = await axios.get('event_app/studies/');
        this.studies = response.data;
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