<template>
  <div>
    <div class="left-side">
      <div class="left-side-navbar">
        <div class="left-side-account">
          <div class="left-side-profile-img-container">
            <img class="left-side-profile-img"
                 src="https://icdn.lenta.ru/images/2024/03/15/12/20240315121325156/square_1280_2b052867d958834bd4788b91709d3fe4.jpg"
                 alt="">
          </div>
          <div class="left-side-profile-info-container">
            <span class="left-side-profile-name">Хасбулла</span>
            <span class="left-side-profile-position">Администратор</span>
          </div>
          <div class="left-side-profile-menu-container">
            <ul class="menu">
              <li v-for="(item, index) in menuItems" :key="index">
                <div
                    class="nav-item"
                    :class="{ active: activeIndex === index }"
                    @click="setActive(index)">
                  <v-icon>{{ item.icon }}</v-icon>
                  <a>{{ item.name }}</a>
                </div>
              </li>
            </ul>
          </div>
        </div>
        <div class="left-side-divider" />
        <div class="left-side-exit-container">
          <v-icon>mdi-exit-to-app</v-icon>
          <button class="left-side-exit-btn" @click="handleLogout">Выйти</button>
        </div>
      </div>
      <div class="left-side-navbar-border" />
    </div>
  </div>
</template>

<script>
import { logout } from '@/services/auth'
import axios from "@/plugins/axios";

export default {
  name: 'LeftSideBar',
  components: { },
  data() {
    return {
      students: [],
      activeIndex: 0,
      menuItems: [
        { name: 'Студенты', icon: 'mdi-school', route: '/students' },
        { name: 'Наставники', icon: 'mdi-account-details', route: '/mentors' },
        { name: 'Стажировки и практики', icon: 'mdi-account-tie', route: '/studies' },
        { name: 'Работа', icon: 'mdi-badge-account-horizontal', route: '/works' }
      ],
    }
  },
  created() {
    this.fetchStudents()
  },
  methods: {
    async fetchStudents() {
      try {
        const response = await axios.get('anket_app/students/')
        this.students = response.data
      } catch (e) {
        alert('Ошибка')
      }
    },
    setActive(index) {
      this.activeIndex = index;
      const selectedRoute = this.menuItems[index].route;
      this.$router.push({ path: selectedRoute });
    },
    handleLogout() {
      logout();
      this.$router.push({name: 'Login'})
    }
  }
}
</script>

<style lang="scss" scoped>
.left-side {
  display: flex;
  flex-direction: row;
  height: 100vh;
}

.left-side-navbar {
  width: 368px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.left-side-navbar-border {
  width: 2px;
  background-color: #e9e3ff;
  filter: blur(4px);
}

.left-side-account {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.left-side-profile-img-container {
  margin-top: 70px;
  border-radius: 50%;
  height: 100px;
  width: 100px;
  overflow: hidden;
}

.left-side-profile-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.left-side-profile-info-container {
  margin-top: 16px;
  display: flex;
  flex-direction: column;
  align-items: center;
  font-weight: 500;
}

.left-side-profile-name {
  font-size: 24px;
  color: #32312e;
}

.left-side-profile-position {
  margin-top: 5px;
  font-size: 20px;
  color: #bbb;
}

.left-side-profile-menu-container {
  margin-top: 60px;
}

.menu {
  list-style-type: none;
}

li {
  margin-bottom: 20px
}

.nav-item {
  display: flex;
  flex-direction: row;
  align-items: center;
  align-content: space-between;
  width: 280px;
  font-size: 24px;
  font-weight: 400;
  color: #bbb;
  padding: 20px 30px 20px 30px;
  border-radius: 10px;
  cursor: pointer;
}

.active {
  color: #32312e;
  background-color: #e9e3ff;
  font-size: 24px;
  font-weight: 500;
  transition: background-color 0.5s;
}

a {
  margin-left: 25px;
}

.left-side-divider {
  width: 270px;
  height: 3px;
  background-color: #bbb;
  margin-top: 70px;
  padding: 1.5px;
}

.left-side-exit-container {
  display: flex;
  flex-direction: row;
  align-items: center;
  width: 230px;
  margin-top: 40px;
  font-size: 24px;
  color: #bbb;
  font-weight: 400;
  margin-bottom: 40px;
}

.left-side-exit-btn {
  font-weight: 400;
  margin-left: 25px;
}
</style>
