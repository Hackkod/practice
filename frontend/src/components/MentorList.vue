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
      <tr v-for="mentor in mentors" :key="mentor.id">
        <td class="mentor-info">
          <img :src="mentor.profile_photo" alt=" " class="mentor-photo">
          <span>{{ truncatedName(mentor) }}</span>
        </td>
        <td>{{ mentor.gender }}</td>
        <td>{{ mentor.job_position }}</td>
        <td>{{ mentor.birth_date }}</td>
        <td>
          <div class="table-btns">
            <button @click="editMentor(mentor)">
              <img :src="require('@/assets/img/EditIcon.svg')" alt="Иконка редактирования" width="24" height="24">
            </button>
            <button @click="confirmDelete(mentor)">
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
      // try {
      //   const studentId = updatedStudent.get('id');
      //
      //   if (studentId) {
      //     const hasNewProfilePhoto = updatedStudent.has('profile_photo') && updatedStudent.get('profile_photo') instanceof File;
      //
      //     if (!hasNewProfilePhoto) {
      //       updatedStudent.delete('profile_photo');
      //     }
      //     await axios.put(`anket_app/students/${studentId}/`, updatedStudent, {
      //       headers: {
      //         'Content-Type': 'multipart/form-data'
      //       }
      //     });
      //   } else {
      //     await axios.post(`anket_app/students/`, updatedStudent, {
      //       headers: {
      //         'Content-Type': 'multipart/form-data'
      //       }
      //     });
      //   }
      //   this.$emit('updateStudents');
      // } catch (e) {
      //   alert('Ошибка при изменении студента');
      // }
      // this.closeForm();
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
.mentor-info {
  display: flex;
  align-items: center;
}

.mentor-photo {
  width: 40px;
  height: 40px;
  margin-right: 10px;
  border-radius: 50%;
  object-fit: cover;
}
</style>
