<template>
  <div class="student-info-container">
    <div class="student-info-main">
      <div class="student-info-img-container">
        <img class="student-info-img"
             :src="student.profile_photo"
             alt="">
      </div>
      <div class="student-info-name-est">
        <span class="student-name">{{ truncatedName }}</span>
        <span class="student-establishment">{{ truncateEstablishment }}</span>
        <span class="student-course">Курс: {{student.course}}</span>
      </div>
    </div>
    <div class="student-info-actions">
      <button class="card-edit-btn" @click="editStudent(student)" >
        <img
            :src="require('@/assets/img/EditIcon.svg')"
            alt="Иконка редактирования"
            width="26"
            height="26">
      </button>
      <button class="card-delete-btn" @click="confirmDelete(student.id)" >
        <img
            :src="require('@/assets/img/DeleteIcon.svg')"
            alt="Иконка удаления"
            width="26"
            height="26">
      </button>
    </div>
  </div>
</template>

<script>
import axios from "@/plugins/axios";

export default {
  name: "StudentCard",
  components: { },
  data() {
    return {
      selectedStudent: null,
    }
  },
  props: {
    student: {
      type: Object,
      required: true
    }
  },
  methods: {
    editStudent(student) {
      this.$emit('editStudent', student);
    },
    async deleteStudent(id) {
      try {
        await axios.delete(`anket_app/students/${id}/`)
        this.$emit('updateStudents');
      } catch (e) {
        alert('Ошибка при удалении студента')
      }
    },
    confirmDelete(id) {
      if (confirm(`Вы уверены, что хотите удалить студента ${this.student.surname + ' ' + this.student.name}?`)) {
        this.deleteStudent(id);
      }
    }
  },
  computed: {
    truncatedName() {
      const fullName =
          this.student.surname + ' ' +
          this.student.name[0] + '.' +
          this.student.patronymic[0] + '.'
      return fullName.length > 11 ? fullName.slice(0, 11) + '...' : fullName;
    },
    truncateEstablishment() {
      const establish = this.student.establishment
      return establish.length > 12 ? establish.slice(0, 12) + '...' : establish;
    }
  },
}
</script>

<style scoped lang="scss">
.student-info-container {
  width: 285px;
  height: 150px;
  border-radius: 10px;
  box-shadow: 0 4px 20px 0 #f2f1f3;
  background: #fff;
}

.student-info-main {
  display: flex;
  flex-direction: row;
  align-items: center;
}

.student-info-img-container {
  border-radius: 50%;
  height: 80px;
  width: 80px;
  overflow: hidden;
  margin: 20px 0 0 20px;
}

.student-info-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.student-info-name-est {
  display: flex;
  flex-direction: column;
  margin-left: 20px;
  margin-top: 20px;
}

.student-name {
  font-weight: 500;
  font-size: 20px;
  color: #344ca2;
}

.student-establishment, .student-course {
  font-weight: 400;
  font-size: 16px;
  color: #bbb;
}

.student-info-actions {
  display: flex;
  flex-direction: row;
  justify-content: right;
  margin-top: 5px;
  margin-right: 20px;
  grid-gap: 20px;
}
</style>