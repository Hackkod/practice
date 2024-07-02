<template>
  <div class="page-content">
    <MentorCard
        v-for="mentor in mentors" :key="mentor.id"
        :mentorProfilePhoto="mentor.profile_photo"
        :mentorPosition="mentor.job_position"
        :mentorPatronymic="mentor.patronymic"
        :mentorSurname="mentor.surname"
        :mentorName="mentor.name"
    />
  </div>
</template>

<script>
import MentorCard from "@/components/MentorCard.vue";
import axios from "@/plugins/axios";

export default {
  components: {MentorCard},
  data() {
    return {
      mentors: [],
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
        console.log(this.mentors)
      } catch (e) {
        alert('Ошибка')
      }
    }
  },
}
</script>

<style lang="scss" scoped>
  .page-content {
    margin: 40px 0 0 40px;
    display: flex;
    flex-wrap: wrap;
    gap: 30px;
    justify-content: flex-start;
  }
</style>