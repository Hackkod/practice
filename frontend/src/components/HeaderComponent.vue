<template>
  <div class="page-main-container">
    <div class="page-name-container">
      <span class="page-name">{{ pageName }}</span>
    </div>
    <div class="page-table-functional-row">
      <div class="page-table-switchers">
        <div
            v-for="(tab, index) in tabs"
            :key="index"
            :class="['tab', { active: activeTab === index }]"
            @click="activeTab = index"
        >
          {{ tab.name }}
        </div>
      </div>
      <div class="page-func-inputs">
        <button class="page-add-btn"></button>
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
    pageName: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      students: [],
      activeTab: 0,
      tabs: [
        {name: 'Карта'},
        {name: 'Таблица'}
      ]
    }
  },
}
</script>

<style lang="scss" scoped>
.page-main-container {
  width: 100%;
  display: flex;
  flex-direction: column;
}

.page-name-container {
  margin-top: 70px;
  margin-left: 40px;
  font-size: 48px;
  font-weight: 700;
  color: #32312e;
}

.page-table-switchers {
  display: flex;
  flex-direction: row;
  grid-gap: 20px;
  font-weight: 500;
  font-size: 24px;
  color: #bbb;
  margin-top: 40px;
  margin-left: 40px;
}

.active {
  color: #32312e;
}

.tab {
  padding-right: 20px;
  cursor: pointer;
}

.tab.active {
  font-weight: bold;
  border-bottom: 4px solid #bdabff;
}

.page-divider {
  width: 94.8%;
  height: 3px;
  background-color: #bbb;
  align-self: center;
}

.page-table-functional-row {
  display: flex;
  flex-direction: row;
}

.page-input-filter {
  background: url("@/assets/img/SearchIcon.png") no-repeat calc(100% - 15px) center;
  border: 3px solid #eee;
  border-radius: 10px;
  width: 320px;
  height: 45px;
  font-size: 24px;
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
  border: 3px solid #eee;
  border-radius: 10px;
  width: 320px;
  height: 45px;
  font-size: 24px;
  font-weight: 400;
  color: #bbb;
  padding: 0 15px;
}

.page-select-field:focus {
  outline: none;
}

.page-add-btn {
  width: 45px;
  height: 45px;
  background-image: url("@/assets/img/AddIcon.png");
  background-color: #f0ecff;
  border-radius: 8px;
}

.page-func-inputs {
  display: flex;
  flex-direction: row;
  grid-gap: 15px;
  margin-top: 15px;
  margin-left: auto;
  margin-right: 40px;
}
</style>