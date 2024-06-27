<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <button @click="handleLogout">Logout</button>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import { logout } from '@/services/auth'

export default {
  name: 'HomeView',
  components: {
    HelloWorld
  },
  methods: {
    handleLogout() {
      logout();
      this.$router.push({name: 'Login'})
    }
  }
}
</script>
