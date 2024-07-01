<template>
  <study-create-btn @studyAdded="addStudyToList"/>
  <study-list :studies="studies"/>
</template>

<script>
import axios from "@/plugins/axios";
import StudyList from "@/components/StudyList.vue";
import StudyCreateBtn from "@/components/StudyCreateBtn.vue";

export default {
  components: {StudyCreateBtn, StudyList},
  data() {
    return {
      studies: [],
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