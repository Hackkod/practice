<template>
  <div>
    <HeaderComponent title="Наставники" :tabs="tabs" :activeTab="activeTab" @tabChange="setActiveTab" @openForm="createMentor" />
    <div :class="{'page-content': activeTab === 0}">
      <template v-if="activeTab === 0">
        <MentorCard
            @updateMentors="fetchMentors"
            @editMentor="editMentor"
            v-for="mentor in mentors" :key="mentor.id"
            :mentor="mentor"
        />
      </template>
      <template v-else-if="activeTab === 1">
        <MentorList
            :mentors="mentors"
            @updateMentors="fetchMentors"
            @editMentor="editMentor"
        />
      </template>
    </div>
    <PaginatorTable :next="next" :previous="previous" @changePage="fetchMentors" />
    <MentorForm :mentor="selectedMentor" v-if="showForm" @close="closeForm" @save="saveMentor" />
  </div>
</template>

<script>
import MentorCard from "@/components/MentorCard.vue";
import axios from "@/plugins/axios";
import HeaderComponent from "@/components/HeaderComponent.vue";
import MentorForm from "@/components/MentorForm.vue";
import PaginatorTable from "@/components/PaginatorTable.vue";
import MentorList from "@/components/MentorList.vue";

export default {
  components: {MentorList, PaginatorTable, MentorForm, HeaderComponent, MentorCard},
  data() {
    return {
      mentors: [],
      showForm: false,
      selectedMentor: null,
      activeTab: 0,
      itemsPerPage: 12,
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
    createMentor() {
      this.selectedMentor = null
      this.showForm = true
    },
    editMentor(mentor) {
      this.selectedMentor = mentor
      this.showForm = true
    },
    closeForm() {
      this.showForm = false
      this.selectedMentor = null
    },
    async saveMentor(mentor) {
      try {
        const mentorId = mentor.get('id');
        if (mentorId) {
          const hasNewProfilePhoto = mentor.has('profile_photo') && mentor.get('profile_photo') instanceof File;

          if (!hasNewProfilePhoto) {
            mentor.delete('profile_photo');
          }
          await axios.put(`anket_app/mentors/${mentorId}/`, mentor, {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          });
        } else {
          await axios.post(`anket_app/mentors/`, mentor, {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          });
        }
        await this.fetchMentors();
      } catch (e) {
        alert('Ошибка при создании наставника');
      }
      this.closeForm();
    },
    async fetchMentors(url=`anket_app/mentors/?page=${this.currentPage}&page_size=${this.itemsPerPage}`) {
      try {
        const response = await axios.get(url)
        this.mentors = response.data.results
        this.next = response.data.next
        this.previous = response.data.previous
      } catch (e) {
        alert('Ошибка')
      }
    },
    setActiveTab(index) {
      this.activeTab = index;
      this.itemsPerPage = index === 0 ? 12 : 6;
      this.fetchMentors();
    },
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