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
        <button class="page-add-btn" @click="openForm" />
        <div class="page-func-inputs-show" v-if="showEventFilters">
          <div class="page-filter-label">С:</div>
          <input
              type="date"
              v-model="startDate"
              @change="updateFilters"
              placeholder="Дата начала"
              :class="{'active-input': startDate}"
          >
          <div class="page-filter-label">По:</div>
          <input
              type="date"
              v-model="endDate"
              @change="updateFilters"
              placeholder="Дата окончания"
              :class="{'active-input': endDate}"
          >
          <select
              class="page-select-field"
              v-model="selectedType"
              @change="updateFilters"
              :class="{'active-input': selectedType}"
          >
            <option value="" selected>Все типы</option>
            <option
                v-for="option in typeOptions"
                :key="option.value"
                :value="option.value"
            >
              {{ option.label }}
            </option>
          </select>
        </div>
        <div class="page-func-inputs-show" v-if="showAnketFilters">
          <select
              class="page-select-field"
              v-model="selectedHardSkill"
              @change="updateFilters"
              :class="{'active-input': selectedHardSkill}"
          >
            <option value="" selected>Все навыки</option>
            <option
                v-for="skill in filterOptions.hardSkills"
                :key="skill.id"
                :value="skill.id"
            >
              {{ skill.skill_name }}
            </option>
          </select>
          <div class="page-func-inputs-show" v-if="showCourseFilter">
            <div class="page-filter-label">Курс:</div>
            <input
                type="number"
                max="6"
                min="1"
                v-model="selectedCourse"
                @input="validateCourse"
                @change="updateFilters"
                placeholder="Все курсы"
                :class="{'active-input': selectedCourse, 'page-select-field': true}"
            >
          </div>
        </div>
        <v-icon
            class="clear-filters-btn"
            color="#aaa"
            size="large"
            @click="clearFilters"
        >
          mdi-close
        </v-icon>
        <div class="search-container">
          <input
              class="page-input-filter"
              type="text"
              placeholder="Поиск"
              v-model="searchQuery"
              @keyup.enter="updateFilters"
          >
          <button
              class="search-icon-btn"
              @click="updateFilters"
          />
        </div>
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
    },
    typeOptions: {
      type: Array,
      required: false,
      default: () => []
    },
    showEventFilters: {
      type: Boolean,
      default: true
    },
    showAnketFilters: {
      type: Boolean,
      default: false
    },
    showCourseFilter: {
      type: Boolean,
      default: false
    },
    filterOptions: {
      type: Object,
      default: () => ({
        hardSkills: []
      })
    }
  },
  data() {
    return {
      searchQuery: '',
      startDate: '',
      endDate: '',
      selectedType: '',
      selectedHardSkill: '',
      selectedCourse: ''
    }
  },
  methods: {
    openForm() {
      this.$emit('openForm');
    },
    updateFilters() {
      this.$emit('updateFilters', {
        searchQuery: this.searchQuery,
        startDate: this.startDate,
        endDate: this.endDate,
        selectedType: this.selectedType,
        selectedHardSkill: this.selectedHardSkill,
        selectedCourse: this.selectedCourse
      });
    },
    clearFilters() {
      this.searchQuery = '';
      this.startDate = '';
      this.endDate = '';
      this.selectedType = '';
      this.selectedHardSkill = '';
      this.selectedCourse = '';
      this.updateFilters();
    },
    validateCourse(event) {
      const min = 1
      const max = 6
      let value = event.target.value

      if (value !== '') {
        value = parseInt(value, 10)
        if (value < min) {
          value = min
        } else if (value > max) {
          value = max
        }
      }
      this.selectedCourse = value
    },
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
  background: url("@/assets/img/FilterIcon.svg") no-repeat calc(100% - 15px) center;
  background-size: 27px 27px;
  border: 3px solid #eee;
  border-radius: 10px;
  width: 180px;
  height: 40px;
  font-size: 18px;
  font-weight: 400;
  color: #bbb;
  padding: 0 15px;
}

.page-select-field.active-input {
  color: #32312e;
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
  align-items: center;
  grid-gap: 10px;
  margin: 15px 20px 10px auto;

  .page-func-inputs-show {
    display: flex;
    flex-direction: row;
    align-items: center;
    grid-gap: 10px;

    input {
      background: none;
      width: 140px;
    }

    input::placeholder {
      color: #bbb;
    }

    input.active-input {
      color: #32312e;
    }
  }

  .page-filter-label {
    color: #bbb;
    font-size: 18px;
  }

  input[type="date"] {
    color: #bbb;
    border: 3px solid #eee;
    border-radius: 10px;
    padding: 0 10px;
    height: 40px;
    font-size: 18px;
    font-weight: 400;
    position: relative;
    z-index: 1;
  }

  input[type="date"].active-input {
    color: #32312e;
  }

  input[type="date"]::-webkit-calendar-picker-indicator {
    filter: invert(47%) sepia(0%) saturate(0%) hue-rotate(194deg) brightness(91%) contrast(90%);
    cursor: pointer;
  }

  input[type="date"]:focus {
    outline: none;
    border: 3px solid #bbb;
  }
}

.clear-filters-btn {
  width: 40px;
  height: 40px;
  border: none;
  cursor: pointer;
}

.clear-filters-btn:hover {
  background-color: #f0f0f0;
  border-radius: 8px;
}

.search-container {
  position: relative;
  display: inline-block;
}

.search-icon-btn {
  position: absolute;
  right: 15px;
  top: 50%;
  transform: translateY(-50%);
  background: url("@/assets/img/SearchIcon.svg") no-repeat center center;
  background-size: 27px 27px;
  width: 27px;
  height: 27px;
  border: none;
  cursor: pointer;
}

.search-icon-btn:hover {
  opacity: 0.8;
}
</style>
