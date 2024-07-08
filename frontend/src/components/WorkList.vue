<template>
  <div>
    <table-overlay>
      <thead>
      <tr>
        <th>Заголовок</th>
        <th>Студент</th>
        <th>Наставник</th>
        <th>Тип</th>
        <th>Дата начала/окончания</th>
        <th class="actions-column">Действия</th>
      </tr>
      </thead>
      <tbody>
      <tr
          class="row-content"
          v-for="work in works"
          :key="work.id"
          @click="viewWork(work)">
        <td>{{ work.name }}</td>
        <td>{{ truncatedName(work.student_full) }}</td>
        <td>{{ truncatedName(work.mentor_full) }}</td>
        <td>{{ work.type }}</td>
        <td>{{ work.start_date }} - {{ work.end_date }}</td>
        <td>
          <div class="table-btns">
            <button @click.stop="editWork(work)">
              <img
                  :src="require('@/assets/img/EditIcon.svg')"
                  alt="Иконка редактирования"
                  width="24"
                  height="24"
              />
            </button>
            <button @click.stop="confirmDelete(work)">
              <img
                  :src="require('@/assets/img/DeleteIcon.svg')"
                  alt="Иконка удаления"
                  width="24"
                  height="24"
              />
            </button>
          </div>
        </td>
      </tr>
      </tbody>
    </table-overlay>
    <work-form
        v-if="showForm"
        :workId="selectedWork"
        :readonly="readonly"
        @close="closeForm"
        @save="saveWork"
    />
  </div>
</template>

<script>
import WorkForm from "@/components/WorkForm.vue";
import axios from "@/plugins/axios";

export default {
  name: 'WorkList',
  props: {
    works: Array,
  },
  components: {
    WorkForm,
  },
  data() {
    return {
      showForm: false,
      selectedWork: null,
      readonly: false,
    }
  },
  methods: {
    editWork(work) {
      this.selectedWork = work.id;
      this.showForm = true;
      this.readonly = false
    },
    closeForm() {
      this.showForm = false;
      this.readonly = false
      this.selectedWork = null
    },
    viewWork(work) {
      this.selectedWork = work.id
      this.readonly = true
      this.showForm = true
    },
    async saveWork(updatedWork) {
      try {
        await axios.put(`event_app/works/${updatedWork.id}/`, updatedWork);
        this.$emit('updateWorks');
      } catch (e) {
        alert('Ошибка при изменении работы');
      }
      this.closeForm();
    },
    async deleteWork(work) {
      try {
        await axios.delete(`event_app/works/${work.id}/`);
        this.$emit('updateWorks');
      } catch (e) {
        alert('Ошибка при удалении работы')
      }
    },
    confirmDelete(work) {
      if (confirm(`Вы уверены, что хотите удалить работу ${work.name}?`)) {
        this.deleteWork(work);
      }
    },
    truncatedName(person){
      const fullName =
          person.surname + ' ' +
          person.name[0] + '.' +
          person.patronymic[0] + '.'
      return fullName.length > 13 ? fullName.slice(0, 13) + '..' : fullName;
    },
  }
}
</script>

<style lang="scss" scoped>

</style>
