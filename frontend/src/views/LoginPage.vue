<template>
  <div>
    <form @submit.prevent="handleLogin">
      <div>
        <label class="test" for="username">Username:</label>
        <input type="text" v-model="username" id="username" required />
      </div>
      <div>
        <label for="password">Password:</label>
        <input type="password" v-model="password" id="password" required />
      </div>
      <v-btn type="submit">Login</v-btn>
      <p v-if="error">{{ error }}</p>
    </form>
  </div>
</template>

<script>
import { login } from '@/services/auth';

export default {
  name: 'LoginPage',
  data() {
    return {
      username: '',
      password: '',
      error: ''
    };
  },
  methods: {
    async handleLogin() {
      try {
        const token = await login(this.username, this.password);
        if (token) {
          this.$router.push({ name: 'Students' });
        }
      } catch (error) {
        console.error('Ошибка:', error);
      }
    }
  }
};
</script>

<style lang="scss" scoped>
</style>