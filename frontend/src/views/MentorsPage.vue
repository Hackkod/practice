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
  </div>
</template>

<script>
import MentorCard from "@/components/MentorCard.vue";
import axios from "@/plugins/axios";
import HeaderComponent from "@/components/HeaderComponent.vue";

export default {
  components: {HeaderComponent, MentorCard},
  data() {
    return {
      mentors: [],
      activeTab: 0,
      tabs: [
        { name: 'Карта' },
        { name: 'Таблица' }
      ],
    }
  },
  created() {
    this.fetchMentors()
  },
  methods: {
    async fetchMentors() {
      try {
        const response = await axios.get('anket_app/mentors/')
        this.mentors = response.data
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