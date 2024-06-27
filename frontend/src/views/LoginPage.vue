<template>
  <div>
    <h1>Login</h1>
    <form @submit.prevent="handleLogin">
      <input v-model="username" type="text" placeholder="Username" />
      <input v-model="password" type="password" placeholder="Password" />
      <button type="submit">Login</button>
    </form>
    <p v-if="error">{{ error }}</p>
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
          this.$router.push({name: 'Home'});
        }
      } catch (error) {
        this.error = 'Invalid username or password';
        console.error('Error details:', error);
      }
    }
  }
};
</script>
