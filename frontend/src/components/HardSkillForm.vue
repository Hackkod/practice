<template>
  <modal-overlay @close="close" @submit="save">
    <modal-header>Добавление нового Хард скилла</modal-header>
    <div class="form-content">
      <div class="form-group">
        <label for="skill_name">Название навыка:</label>
        <input type="text" id="skill_name" v-model="form.skill_name" />
      </div>
    </div>
  </modal-overlay>
</template>

<script>
import ModalOverlay from "@/components/UI/ModalOverlay.vue";
import axios from "@/plugins/axios";
import ModalHeader from "@/components/UI/ModalHeader.vue";

export default {
  name: "HardSkillForm",
  components: {ModalHeader, ModalOverlay },
  data() {
    return {
      form: {
        skill_name: '',
      }
    };
  },
  methods: {
    async save() {
      try {
        await axios.post('hard_skill_app/hard_skills/', this.form);
        this.$emit('refreshHardSkills');
        this.close();
      } catch (e) {
        alert('Ошибка при добавлении hard skill');
      }
    },
    close() {
      this.$emit('close');
    }
  }
};
</script>

<style scoped>
.form-content {
  padding: 20px;
}
.form-group {
  margin-bottom: 15px;
}
</style>
