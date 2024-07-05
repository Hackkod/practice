<template>
  <div>
    <table-overlay>
      <thead>
      <tr>
        <th>ФИО</th>
        <th>Пол</th>
        <th>Должность</th>
        <th>Дата рождения</th>
        <th class="actions-column">Действия</th>
      </tr>
      </thead>
      <tbody>
      <tr
          class="row-content"
          v-for="mentor in mentors"
          :key="mentor.id"
          @click="this.$emit('viewMentor', mentor)"
      >
        <td class="td-info">
          <div class="line-info">
            <img :src="mentor.profile_photo" alt="" class="line-photo">
            <span>{{ truncatedName(mentor) }}</span>
          </div>
        </td>
        <td>{{ mentor.gender }}</td>
        <td>{{ mentor.job_position }}</td>
        <td>{{ mentor.birth_date }}</td>
        <td>
          <div class="table-btns">
            <button @click.stop="editMentor(mentor)">
              <img :src="require('@/assets/img/EditIcon.svg')" alt="Иконка редактирования" width="24" height="24">
            </button>
            <button @click.stop="confirmDelete(mentor)">
              <img :src="require('@/assets/img/DeleteIcon.svg')" alt="Иконка удаления" width="24" height="24">
            </button>
          </div>
        </td>
      </tr>
      </tbody>
    </table-overlay>
    <mentor-form v-if="showForm" :student="selectedMentor" @close="closeForm" @save="saveMentor"/>
  </div>
</template>

<script>
import axios from "@/plugins/axios";
import MentorForm from "@/components/MentorForm.vue";

export default {
  name: 'MentorList',
  props: {
    mentors: Array,
  },
  components: {
    MentorForm,
  },
  data() {
    return {
      showForm: false,
      selectedMentor: null,
    }
  },
  methods: {
    editMentor(mentor) {
      this.$emit('editMentor', mentor);
    },
    closeForm() {
      this.showForm = false;
    },
    async saveMentor(updatedMentor) {
      try {
        await axios.put(`anket_app/mentors/${updatedMentor.id}/`, updatedMentor);
        this.$emit('updateMentors');
      } catch (e) {
        alert('Ошибка при изменении наставника');
      }
      this.closeForm();
    },
    async deleteMentor(mentor) {
      try {
        await axios.delete(`anket_app/mentors/${mentor.id}/`);
        this.$emit('updateMentors');
      } catch (e) {
        alert('Ошибка при удалении наставника')
      }
    },
    confirmDelete(mentor) {
      if (confirm(`Вы уверены, что хотите удалить студента ${mentor.name}?`)) {
        this.deleteMentor(mentor);
      }
    },
    truncatedName(mentor){
      const fullName =
          mentor.surname + ' ' +
          mentor.name + ' ' +
          mentor.patronymic
      return fullName.length > 26 ? fullName.slice(0, 26) + '...' : fullName;
    },
  }
}
</script>

<style lang="scss" scoped>

</style>
