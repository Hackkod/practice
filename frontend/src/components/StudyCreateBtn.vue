<template>
  <div>
    <button @click="showForm = true">Создать обучение</button>
    <study-form v-if="showForm" @close="closeForm" @save="saveStudy"/>
  </div>
</template>

<script>
import axios from "@/plugins/axios";
import StudyForm from "@/components/StudyForm.vue";

export default {
  name: "StudyCreateBtn",
  components: {
    StudyForm,
  },
  data() {
    return {
      showForm: false,
    };
  },
  methods: {
    closeForm() {
      this.showForm = false;
    },
    async saveStudy(study) {
      try {
        const response = await axios.post('event_app/studies/', study);
        this.$emit('studyAdded', response.data);
      } catch (e) {
        alert('Ошибка при создании обучения');
      }
      this.closeForm();
    },
  },
};
</script>

<style scoped>

</style>
