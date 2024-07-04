<template>
  <div class="page-main-container">
    <div class="page-name-container">
      <span class="page-name">{{ title }}</span>
    </div>
    <div class="page-table-functional-row">
      <div class="page-table-switchers">
        <div
            v-for="(tab, index) in tabs"
            :key="index"
            :class="['tab', { active: activeTab === index }]"
            @click="$emit('tabChange', index)"
        >
          {{ tab.name }}
        </div>
      </div>
      <div class="page-func-inputs">
        <button class="page-add-btn" @click="openForm"></button>
        <select class="page-select-field" name="filter">
          <option value="" disabled selected hidden>Фильтр</option>
          <option value="value1">Значение 1</option>
          <option value="value2">Значение 2</option>
          <option value="value3">Значение 3</option>
        </select>
        <input class="page-input-filter" type="text" placeholder="Поиск">
      </div>
    </div>
    <div class="page-divider" />
  </div>
</template>

<script>
export default {
  name: "HeaderComponent",
  props: {
    title: {
      type: String,
      required: true,
    },
    tabs: {
      type: Array,
      required: true
    },
    activeTab: {
      type: Number,
      required: true
    }
  },
  data() {
    return {

    }
  },
  methods: {
    openForm() {
      this.$emit('openForm');
    }
  }
}
</script>

<style scoped lang="scss">
  .page-main-container {
    width: 100%;
    display: flex;
    flex-direction: column;
    position: relative;
  }

  .page-name-container {
    margin-top: 40px;
    margin-left: 20px;
    font-size: 36px;
    font-weight: 700;
    color: #32312e;
  }

  .page-table-functional-row {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: flex-end;
  }

  .page-table-switchers {
    display: flex;
    flex-direction: row;
    gap: 10px;
    font-weight: 500;
    font-size: 18px;
    color: #bbb;
    margin-top: 20px;
    margin-left: 20px;
    position: relative;
  }

  .tab {
    padding-right: 15px;
    cursor: pointer;
  }

  .tab.active {
    font-weight: bold;
    border-bottom: 4px solid #bdabff;
    z-index: 1;
    position: relative;
  }

  .active {
    color: #32312e;
  }

  .page-divider {
    height: 3px;
    background-color: #bbb;
    position: absolute;
    bottom: 0;
    left: 20px;
    right: 20px;
  }

  .page-input-filter {
    background: url("@/assets/img/SearchIcon.png") no-repeat calc(100% - 15px) center;
    background-size: 27px 27px;
    border: 3px solid #eee;
    border-radius: 10px;
    width: 220px;
    height: 40px;
    font-size: 18px;
    font-weight: 400;
    color: #32312e;
    padding: 0 15px;
  }

  .page-input-filter:focus {
    outline: none;
  }

  .page-input-filter::placeholder {
    color: #bbb;
  }

  .page-select-field {
    background: url("@/assets/img/FilterIcon.png") no-repeat calc(100% - 15px) center;
    background-size: 27px 27px;
    border: 3px solid #eee;
    border-radius: 10px;
    width: 220px;
    height: 40px;
    font-size: 18px;
    font-weight: 400;
    color: #bbb;
    padding: 0 15px;
  }

  .page-select-field:focus {
    outline: none;
  }

  .page-add-btn {
    background-size: cover;
    display: flex;
    width: 40px;
    height: 40px;
    background-image: url("@/assets/img/AddIcon.png");
    background-color: #f0ecff;
    border-radius: 8px;
  }

  .page-func-inputs {
    display: flex;
    flex-direction: row;
    grid-gap: 10px;
    margin: 15px 20px 10px auto;
  }
</style>