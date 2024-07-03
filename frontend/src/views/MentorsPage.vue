<template>
  <div>
    <HeaderComponent title="Наставники" :tabs="tabs" />
    <div class="page-content">
      <MentorCard
          @updateMentors="fetchMentors"
          v-for="mentor in mentors" :key="mentor.id"
          :mentorProfilePhoto="mentor.profile_photo"
          :mentorPosition="mentor.job_position"
          :mentorPatronymic="mentor.patronymic"
          :mentorSurname="mentor.surname"
          :mentorName="mentor.name"
          :mentorID="mentor.id"
      />
    </div>
    <PaginatorTable :next="next" :previous="previous" @changePage="fetchMentors" />
  </div>
</template>

<script>
import MentorCard from "@/components/MentorCard.vue";
import axios from "@/plugins/axios";
import HeaderComponent from "@/components/HeaderComponent.vue";
import PaginatorTable from "@/components/PaginatorTable.vue";

export default {
  components: {PaginatorTable, HeaderComponent, MentorCard},
  data() {
    return {
      mentors: [],
      activeTab: 0,
      tabs: [
        { name: 'Карта' },
        { name: 'Таблица' }
      ],
      next: null,
      previous: null,
      currentPage: 1,
    }
  },
  created() {
    this.fetchMentors()
  },
  methods: {
    async fetchMentors(url = `anket_app/mentors/?page=${this.currentPage}`) {
      try {
        const response = await axios.get(url)
        this.mentors = response.data.results;
        this.next = response.data.next;
        this.previous = response.data.previous;
      } catch (e) {
        alert('Ошибка')
      }
    }
  },
}
</script>

<style lang="scss" scoped>
  .page-content {
    margin: 20px 0 0 20px;
    display: flex;
    flex-wrap: wrap;
    gap: 18px;
    justify-content: flex-start;
  }
</style>