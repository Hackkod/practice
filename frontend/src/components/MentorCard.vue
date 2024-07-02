<template>
  <div class="mentor-info-container">
    <div class="mentor-info-main">
      <div class="mentor-info-img-container">
        <img class="mentor-info-img"
             :src="this.mentorProfilePhoto"
             alt="">
      </div>
      <div class="mentor-info-name-pos">
        <span class="mentor-name">{{ truncatedName }}</span>
        <span class="mentor-position">{{ truncatedPosition }}</span>
      </div>
    </div>
    <div class="mentor-info-actions">
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
  name: "MentorCard",
  components: { },
  props: {
    mentorName: {
      type: String,
      required: true
    },
    mentorSurname: {
      type: String,
      required: true
    },
    mentorPatronymic: {
      type: String,
      required: true
    },
    mentorPosition: {
      type: String,
      required: true
    },
    mentorProfilePhoto: {
      type: String,
      required: true
    }
  },
  computed: {
    truncatedName() {
      const fullName =
          this.mentorSurname + ' ' +
          this.mentorName[0] + '.' +
          this.mentorPatronymic[0] + '.'
      return fullName.length > 11 ? fullName.slice(0, 11) + '...' : fullName;
    },
    truncatedPosition() {
      const pos = this.mentorPosition
      return pos.length > 14 ? pos.slice(0, 14) + '...' : pos;
    }
  },
}
</script>

<style scoped lang="scss">
.mentor-info-container {
  width: 340px;
  height: 190px;
  border-radius: 10px;
  box-shadow: 0 4px 20px 0 #f2f1f3;
  background: #fff;
}

.mentor-info-main {
  display: flex;
  flex-direction: row;
  align-items: center;
}

.mentor-info-img-container {
  border-radius: 50%;
  height: 100px;
  width: 100px;
  overflow: hidden;
  margin: 25px 0 0 25px;
}

.mentor-info-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.mentor-info-name-pos {
  display: flex;
  flex-direction: column;
  margin-left: 25px;
  margin-top: 20px;
}

.mentor-name {
  font-weight: 500;
  font-size: 24px;
  color: #344ca2;
}

.mentor-position {
  font-weight: 400;
  font-size: 20px;
  color: #bbb;
}

.mentor-info-actions {
  display: flex;
  flex-direction: row;
  justify-content: right;
  margin-top: 8px;
  margin-right: 25px;
  grid-gap: 20px;
}
</style>