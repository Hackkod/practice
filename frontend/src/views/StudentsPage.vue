<template>
  <div>
    <button @click="handleLogout">Logout</button>
  </div>
</template>

<script>
import { logout } from '@/services/auth'

export default {
  name: 'HomeView',
  components: { },
  methods: {
    handleLogout() {
      logout();
      this.$router.push({name: 'Login'})
    }
  }
}
</script>
