<template>
  <div class="student-info-container">
    <div class="student-info-main">
      <div class="student-info-img-container">
        <img class="student-info-img"
             :src="this.studentProfilePhoto"
             alt="">
      </div>
      <div class="student-info-name-est">
        <span class="student-name">{{ truncatedName }}</span>
        <span class="student-establishment">{{ truncateEstablishment }}</span>
        <span class="student-course">Курс: {{this.studentCourse}}</span>
      </div>
    </div>
    <div class="student-info-actions">
      <button class="card-edit-btn ">
        <img
            :src="require('@/assets/img/EditIcon.svg')"
            alt="Иконка редактирования"
            width="32"
            height="32">
      </button>
      <button class="card-delete-btn">
        <img
            :src="require('@/assets/img/DeleteIcon.svg')"
            alt="Иконка удаления"
            width="32"
            height="32">
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "StudentCard",
  components: { },
  props: {
    studentName: {
      type: String,
      required: true
    },
    studentSurname: {
      type: String,
      required: true
    },
    studentPatronymic: {
      type: String,
      required: true
    },
    studentCourse: {
      type: Number,
      required: true
    },
    studentEstablishment: {
      type: String,
      required: true
    },
    studentProfilePhoto: {
      type: String,
      required: true
    }
  },
  computed: {
    truncatedName() {
      const fullName =
          this.studentSurname + ' ' +
          this.studentName[0] + '.' +
          this.studentPatronymic[0] + '.'
      return fullName.length > 11 ? fullName.slice(0, 11) + '...' : fullName;
    },
    truncateEstablishment() {
      const establish = this.studentEstablishment
      return establish.length > 14 ? establish.slice(0, 14) + '...' : establish;
    }
  },
}
</script>

<style scoped lang="scss">
  .student-info-container {
    width: 340px;
    height: 190px;
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
    height: 100px;
    width: 100px;
    overflow: hidden;
    margin: 25px 0 0 25px;
  }

  .student-info-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  .student-info-name-est {
    display: flex;
    flex-direction: column;
    margin-left: 25px;
    margin-top: 20px;
  }

  .student-name {
    font-weight: 500;
    font-size: 24px;
    color: #344ca2;
  }

  .student-establishment, .student-course {
    font-weight: 400;
    font-size: 20px;
    color: #bbb;
  }

  .student-info-actions {
    display: flex;
    flex-direction: row;
    justify-content: right;
    margin-top: 8px;
    margin-right: 25px;
    grid-gap: 20px;
  }
</style>