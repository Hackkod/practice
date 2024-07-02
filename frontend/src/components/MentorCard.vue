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
            width="26"
            height="26">
      </button>
      <button class="card-delete-btn">
        <img
            @click="confirmDelete(mentorID)"
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
    },
    mentorID: {
      type: Number,
      required: true
    },
  },
  methods: {
    async deleteMentor(id) {
      try {
        await axios.delete(`anket_app/mentors/${id}/`)
        this.$emit('updateMentors');
      } catch (e) {
        alert('Ошибка при удалении наставника')
      }
    },
    confirmDelete(id) {
      if (confirm(`Вы уверены, что хотите удалить наставника ${this.mentorSurname + ' ' + this.mentorName}?`)) {
        this.deleteMentor(id);
      }
    }
  },
  computed: {
    truncatedName() {
      const fullName =
          this.mentorSurname + ' ' +
          this.mentorName[0] + '.' +
          this.mentorPatronymic[0] + '.'
      return fullName.length > 10 ? fullName.slice(0, 10) + '..' : fullName;
    },
    truncatedPosition() {
      const pos = this.mentorPosition
      return pos.length > 14 ? pos.slice(0, 14) + '..' : pos;
    }
  },
}
</script>

<style scoped lang="scss">
  .mentor-info-container {
    width: 285px;
    height: 150px;
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
    height: 80px;
    width: 80px;
    overflow: hidden;
    margin: 20px 0 0 20px;
  }

  .mentor-info-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  .mentor-info-name-pos {
    display: flex;
    flex-direction: column;
    margin-left: 20px;
    margin-top: 20px;
  }

  .mentor-name {
    font-weight: 500;
    font-size: 22px;
    color: #344ca2;
  }

  .mentor-position {
    font-weight: 400;
    font-size: 18px;
    color: #bbb;
  }

  .mentor-info-actions {
    display: flex;
    flex-direction: row;
    justify-content: right;
    margin-top: 5px;
    margin-right: 20px;
    grid-gap: 20px;
  }
</style>