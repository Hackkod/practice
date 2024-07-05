<template>
  <div>
    <table-overlay>
      <thead>
      <tr>
        <th>ФИО</th>
        <th>Учреждение</th>
        <th>Начало/Конец обучения</th>
        <th>Курс</th>
        <th class="actions-column">Действия</th>
      </tr>
      </thead>
      <tbody>
      <tr
          class="row-content"
          v-for="student in students"
          :key="student.id"
          @click="this.$emit('viewStudent', student)"
      >
        <td class="td-info">
          <div class="line-info">
            <img :src="student.profile_photo" alt="" class="line-photo">
            <span>{{ truncatedName(student) }}</span>
          </div>
        </td>
        <td>{{ truncatedEstablishment(student) }}</td>
        <td>{{ student.start_study_year }} - {{student.end_study_year}}</td>
        <td>{{ student.course }}</td>
        <td>
          <div class="table-btns">
            <button @click.stop="editStudent(student)">
              <img :src="require('@/assets/img/EditIcon.svg')" alt="Иконка редактирования" width="24" height="24">
            </button>
            <button @click.stop="confirmDelete(student)">
              <img :src="require('@/assets/img/DeleteIcon.svg')" alt="Иконка удаления" width="24" height="24">
            </button>
          </div>
        </td>
      </tr>
      </tbody>
    </table-overlay>
    <student-form v-if="showForm" :student="selectedStudent" @close="closeForm" @save="saveStudent"/>
  </div>
</template>

<script>
import axios from "@/plugins/axios";
import StudentForm from "@/components/StudentForm.vue";

export default {
  name: 'StudentList',
  props: {
    students: Array,
  },
  components: {
    StudentForm

  },
  data() {
    return {
      showForm: false,
      selectedStudent: null,
    }
  },
  methods: {
    editStudent(student) {
      this.$emit('editStudent', student);
    },
    closeForm() {
      this.showForm = false;
    },
    async saveStudent(updatedStudent) {
      try {
        console.log(updatedStudent)
        await axios.put(`anket_app/students/${updatedStudent.id}/`, updatedStudent);
        this.$emit('updateStudents');
      } catch (e) {
        alert('Ошибка при изменении студента');
      }
      this.closeForm();
    },
    async deleteStudent(student) {
      try {
        await axios.delete(`anket_app/students/${student.id}/`);
        this.$emit('updateStudents');
      } catch (e) {
        alert('Ошибка при удалении студента')
      }
    },
    confirmDelete(student) {
      if (confirm(`Вы уверены, что хотите удалить студента ${student.name}?`)) {
        this.deleteStudent(student);
      }
    },
    truncatedName(student){
      const fullName =
          student.surname + ' ' +
          student.name + ' ' +
          student.patronymic
      return fullName.length > 22 ? fullName.slice(0, 22) + '...' : fullName;
    },
    truncatedEstablishment(student){
      const establish = student.establishment
      return establish.length > 22 ? establish.slice(0, 22) + '...' : establish;
    },
  }
}
</script>

<style lang="scss" scoped>

</style>
