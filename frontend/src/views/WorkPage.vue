<template>
  <form>Записи работы</form>
  <div class="work" v-for="work in works" :key="work.id">
    <div><strong>Заголовок</strong> {{ work.name }}</div>
    <div><strong>Студент</strong> {{ work.student_full.name }}</div>
    <div><strong>Наставник</strong> {{ work.mentor_full.name }}</div>
    <div><strong>Дата начала</strong> {{ work.start_date }}</div>
    <div><strong>Дата конца</strong> {{ work.end_date }}</div>
    <div><strong>Тип</strong> {{ work.type }}</div>
    <div><strong>Описание</strong> {{ work.description }}</div>
  </div>
  <v-btn @click="fetchWorks">Получить записи работы</v-btn>
</template>

<script>
import axios from "@/plugins/axios";
// import WorkList from "@/components/WorkList.vue";

export default {
  // components: {WorkList},
  data() {
    return {
      works: [],
    }
  },
  created() {
    this.fetchWorks();
  },
  methods: {
    async fetchWorks() {
      try {
        const response = await axios.get('event_app/works/');
        this.works = response.data;
      }
      catch (e) {
          alert('Ошибка')
      }
    }
  }
}
</script>

<style lang="scss" scoped>

</style>