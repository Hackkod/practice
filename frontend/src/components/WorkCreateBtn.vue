<template>
  <div>
    <button @click="showForm = true">Создать работу</button>
    <work-form v-if="showForm" @close="closeForm" @save="saveWork"/>
  </div>
</template>

<script>
import axios from "@/plugins/axios";
import WorkForm from "@/components/WorkForm.vue";

export default {
  name: "WorkCreateBtn",
  components: {
    WorkForm,
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
    async saveWork(work) {
      try {
        const response = await axios.post('event_app/works/', work);
        this.$emit('workAdded', response.data);
      } catch (e) {
        alert('Ошибка при создании работы');
      }
      this.closeForm();
    },
  },
};
</script>

<style scoped>

</style>
