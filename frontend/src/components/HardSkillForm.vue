<template>
  <modal-overlay @close="close" @submit="save">
    <modal-header>Добавление хард скилла</modal-header>
    <div class="form-content">
      <div class="form-group">
        <v-text-field
          class="form-input skill_name"
          label="Название навыка"
          placeholder="python"
          variant="outlined"
          density="compact"
          v-model="form.skill_name"
        >
        </v-text-field>
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
  components: { ModalHeader, ModalOverlay },
  emits: ["refreshHardSkills", "close"],
  data() {
    return {
      form: {
        skill_name: "",
      },
    };
  },
  methods: {
    async save() {
      try {
        await axios.post("hard_skill_app/hard_skills/", this.form);
        this.$emit("refreshHardSkills");
        this.close();
      } catch (e) {
        alert("Ошибка при добавлении hard skill");
      }
    },
    close() {
      this.$emit("close");
    },
  },
};
</script>

<style scoped></style>
