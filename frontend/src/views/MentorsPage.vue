<template>
  <div>
    <HeaderComponent
      title="Наставники"
      :tabs="tabs"
      :active-tab="activeTab"
      @tab-change="setActiveTab"
      @open-form="createMentor"
      :filter-options="filterOptions"
      :show-event-filters="false"
      :show-anket-filters="true"
      :show-course-filter="false"
      @update-filters="updateFilters"
    />
    <div :class="{ 'page-content': activeTab === 0 }">
      <template v-if="activeTab === 0">
        <MentorCard
          @view-mentor="viewMentor"
          @update-mentors="fetchMentors"
          @edit-mentor="editMentor"
          v-for="mentor in mentors"
          :key="mentor.id"
          :mentor="mentor"
        />
      </template>
      <template v-else-if="activeTab === 1">
        <MentorList
          :mentors="mentors"
          @view-mentor="viewMentor"
          @update-mentors="fetchMentors"
          @edit-mentor="editMentor"
          @update-sort="updateSort"
          :sort-key="sortKey"
          :sort-asc="sortAsc"
        />
      </template>
    </div>
    <PaginatorTable
      :total-pages="totalPages"
      :current-page="currentPage"
      @change-page="handleChangePage"
    />
    <MentorForm
      :mentor-id="selectedMentor"
      :readonly="readonly"
      v-if="showForm"
      @close="closeForm"
      @save="saveMentor"
    />
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
  components: {
    MentorList,
    PaginatorTable,
    MentorForm,
    HeaderComponent,
    MentorCard,
  },
  data() {
    return {
      mentors: [],
      showForm: false,
      readonly: false,
      selectedMentor: null,
      activeTab: 0,
      itemsPerPage: 12,
      tabs: [{ name: "Карта" }, { name: "Таблица" }],
      totalPages: 0,
      currentPage: 1,
      filterOptions: {
        hardSkills: [],
      },
      filters: {
        searchQuery: "",
        selectedHardSkill: null,
      },
      sortKey: "",
      sortAsc: true,
    };
  },
  created() {
    this.fetchHardSkills();
    this.fetchMentors();
  },
  methods: {
    createMentor() {
      this.selectedMentor = null;
      this.showForm = true;
      this.readonly = false;
    },
    editMentor(mentor) {
      this.selectedMentor = mentor.id;
      this.showForm = true;
      this.readonly = false;
    },
    closeForm() {
      this.showForm = false;
      this.selectedMentor = null;
      this.readonly = false;
    },
    viewMentor(mentor) {
      this.selectedMentor = mentor.id;
      this.readonly = true;
      this.showForm = true;
    },
    async saveMentor(mentor) {
      try {
        const mentorId = mentor.get("id");
        if (mentorId) {
          const hasNewProfilePhoto =
            mentor.has("profile_photo") &&
            mentor.get("profile_photo") instanceof File;

          if (!hasNewProfilePhoto) {
            mentor.delete("profile_photo");
          }
          await axios.put(`anket_app/mentors/${mentorId}/`, mentor, {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          });
        } else {
          await axios.post(`anket_app/mentors/`, mentor, {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          });
        }
        await this.fetchMentors();
        this.closeForm();
      } catch (e) {
        alert("Ошибка при создании наставника");
      }
    },
    async fetchMentors(
      url = `anket_app/mentors/?page=${this.currentPage}&page_size=${this.itemsPerPage}`,
    ) {
      try {
        const { searchQuery, selectedHardSkill } = this.filters;
        let params = {
          page: this.currentPage,
          search: searchQuery,
          ordering: this.sortAsc ? this.sortKey : `-${this.sortKey}`,
        };

        if (selectedHardSkill) {
          params.hard_skills_id = selectedHardSkill;
        }

        const response = await axios.get(url, {
          params,
        });
        this.mentors = response.data.results;
        this.totalPages = Math.ceil(response.data.count / this.itemsPerPage);
      } catch (e) {
        alert("Ошибка");
      }
    },
    updateSort(sortKey, sortAsc) {
      this.sortKey = sortKey;
      this.sortAsc = sortAsc;
      this.currentPage = 1;
      this.fetchMentors();
    },
    async fetchHardSkills() {
      try {
        const response = await axios.get("hard_skill_app/hard_skills/");
        this.filterOptions.hardSkills = response.data.results;
      } catch (e) {
        alert("Ошибка при получении списка навыков");
      }
    },
    setActiveTab(index) {
      this.activeTab = index;
      this.itemsPerPage = index === 0 ? 12 : 6;
      this.fetchMentors();
    },
    updateFilters(newFilters) {
      this.filters = newFilters;
      this.currentPage = 1;
      this.fetchMentors();
    },
    handleChangePage(page) {
      this.currentPage = page;
      this.fetchMentors();
    },
  },
};
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
