<template>
  <div class="left-side">
    <div class="left-side-navbar">
      <div class="left-side-account">
        <div class="left-side-profile-img-container">
          <img
            v-if="user !== null"
            class="left-side-profile-img"
            :src="user.photo"
            alt=""
          >
        </div>
        <div class="left-side-profile-info-container">
          <span class="left-side-profile-name" v-if="user !== null">{{ user.username }}</span>
          <span class="left-side-profile-name" v-else>Пользователь</span>
          <span class="left-side-profile-position">Администратор</span>
        </div>
        <div class="left-side-profile-menu-container">
          <ul class="menu">
            <li v-for="(item, index) in menuItems" :key="index">
              <div
                  class="nav-item"
                  :class="{ active: activeIndexPage === index }"
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
</template>

<script>
import { logout } from '@/services/auth'
import axios from "@/plugins/axios";

export default {
  name: 'LeftSideBar',
  components: { },
  data() {
    return {
      user: null,
      activeIndexPage: this.$route.meta.activeIndex || 0,
      menuItems: [
        { name: 'Студенты', icon: 'mdi-school', route: '/students' },
        { name: 'Наставники', icon: 'mdi-account-details', route: '/mentors' },
        { name: 'Стажировки и практики', icon: 'mdi-account-tie', route: '/studies' },
        { name: 'Работа', icon: 'mdi-badge-account-horizontal', route: '/works' }
      ],
    }
  },
  created() {
    this.fetchCurrentUser()
  },
  methods: {
    async fetchCurrentUser() {
      try {
        const response = await axios.get('user_app/current_user/')
        this.user = response.data
      } catch (e) {
        alert('Ошибка')
      }
    },
    setActive(index) {
      this.activeIndexPage = index;
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
    width: 280px;
    display: flex;
    flex-direction: column;
    align-items: center;
    overflow-y: auto;
  }

  .left-side-navbar-border {
    border: 2px solid #e9e3ff;
    filter: blur(6px);
  }

  .left-side-account {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .left-side-profile-img-container {
    margin-top: 20%;
    border-radius: 50%;
    height: 80px;
    width: 80px;
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
    font-size: 16px;
    color: #bbb;
  }

  .left-side-profile-menu-container {
    margin-top: 40px;
    width: 100%;
  }

  .menu {
    list-style-type: none;
    padding: 0;
    margin: 0;
    width: 100%;
  }

  li {
    margin-bottom: 15px;
    width: 100%;
  }

  .nav-item {
    display: flex;
    flex-direction: row;
    align-items: center;
    width: 220px;
    font-size: 18px;
    font-weight: 400;
    color: #bbb;
    padding: 15px 20px;
    border-radius: 10px;
    cursor: pointer;
  }

  .nav-item a {
    margin-left: 15px;
  }

  .nav-item.active {
    color: #32312e;
    background-color: #e9e3ff;
    font-size: 18px;
    font-weight: 500;
    transition: background-color 0.5s;
  }

  .left-side-divider {
    width: calc(100% - 40px);
    height: 3px;
    background-color: #bbb;
    margin-top: auto;
    padding: 1.5px;
  }

  .left-side-exit-container {
    display: flex;
    flex-direction: row;
    align-items: center;
    width: 200px;
    margin-top: 20px;
    font-size: 18px;
    color: #bbb;
    font-weight: 400;
    margin-bottom: 30px;
  }

  .left-side-exit-btn {
    font-weight: 400;
    margin-left: 15px;
  }

  @media (max-width: 1024px) {
    .left-side-navbar {
      width: 220px;
    }

    .left-side-profile-img-container {
      height: 60px;
      width: 60px;
    }

    .left-side-profile-name {
      font-size: 20px;
    }

    .left-side-profile-position {
      font-size: 14px;
    }

    .nav-item {
      width: 180px;
      font-size: 16px;
    }

    .nav-item.active {
      width: 180px;
      font-size: 16px;
    }

    .left-side-divider {
      width: calc(100% - 20px);
      margin-top: 30px;
    }

    .left-side-exit-container {
      padding: 0 28px;
    }
  }

  @media (max-width: 768px) {
    .left-side-navbar {
      width: 200px;
    }

    .left-side-profile-img-container {
      height: 50px;
      width: 50px;
    }

    .left-side-profile-name {
      font-size: 18px;
    }

    .left-side-profile-position {
      font-size: 12px;
    }

    .nav-item {
      width: 160px;
      font-size: 14px;
      padding: 10px 15px;
    }

    .nav-item.active {
      width: 160px;
      font-size: 14px;
      padding: 10px 15px;
    }

    .left-side-divider {
      width: calc(100% - 20px);
      margin-top: 20px;
    }

    .left-side-exit-container {
      width: 180px;
      font-size: 14px;
      padding: 0 23px;
    }
  }

  @media (max-width: 480px) {
    .left-side-navbar {
      width: 180px;
    }

    .left-side-profile-img-container {
      height: 40px;
      width: 40px;
    }

    .left-side-profile-name {
      font-size: 16px;
    }

    .left-side-profile-position {
      font-size: 10px;
    }

    .nav-item {
      width: 140px;
      font-size: 12px;
      padding: 8px 10px;
    }

    .nav-item.active {
      width: 140px;
      font-size: 12px;
      padding: 8px 10px;
    }

    .left-side-divider {
      width: calc(100% - 10px);
      margin-top: 15px;
    }

    .left-side-exit-container {
      width: 160px;
      font-size: 12px;
      padding: 0 18px;
    }
  }
</style>
