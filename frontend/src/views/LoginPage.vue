<template>
  <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>

  <div class="wrapper">
    <div class="form-container">
      <div class="col col-1">
        <div class="image-layer">
          <img :src="require('@/assets/img/Floor.png')" class="form-image-floor" alt="floor">
          <img :src="require('@/assets/img/Cabinet.png')" class="form-image cabinet" alt="cabinet">
          <img :src="require('@/assets/img/Plants.png')" class="form-image plants" alt="plants">
          <img :src="require('@/assets/img/Folder.png')" class="form-image folder" alt="folder">
          <img :src="require('@/assets/img/Resumes.png')" class="form-image resumes" alt="resumes">
        </div>
      </div>

      <div class="col col-2">
        <div class="login-form">
          <div class="form-title">
            <span>Авторизация</span>
          </div>
          <div class="form-inputs">
            <div class="input-box">
              <input v-model="username" type="text" class="input-field" placeholder="Имя пользователя" required>
              <i class="bx bx-user icon"></i>
            </div>
            <div class="input-box">
              <input v-model="password" type="password" class="input-field" placeholder="Пароль" required>
              <i class="bx bx-lock-alt icon"></i>
            </div>
            <div class="input-box">
              <button @click="handleLogin()" class="input-submit">
                <span>Войти</span>
                <i class="bx bx-right-arrow-alt"></i>
              </button>
            </div>
          </div>
          <p v-if="error" class="error-message">{{ error }}</p>
        </div>
      </div>
    </div>
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

<style scoped>
.wrapper{
  background-color: #8EC5FC;
  background-image: linear-gradient(62deg, #8EC5FC 0%, #E0C3FC 100%);
  background-position: center;
  background-size: cover;
  background-attachment: fixed;
  background-repeat: no-repeat;

  align-items: center;
  justify-content: center;
  display: flex;

  min-height: 100vh;
  padding: 0 20px;
}

.form-container{
  display: flex;
  width: 1000px;
  height: 600px;
  border: 3px solid rgba(255, 255, 255, 0.3);
  border-radius: 10px;
  backdrop-filter: blur(20px);
  background: linear-gradient(180deg, rgba(227, 222, 229, 0.2) 0%, rgba(255, 255, 255, 0.2) 100%);
  overflow: hidden;
}

.col-1{
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  width: 55%;
  background: rgba(255, 255, 255, 0.3);
  backdrop-filter: blur(30px);
  border-radius: 0 30% 30% 0;
}

.image-layer{
  position: relative;
}

.form-image-floor{
  width: 100%;
  position: relative;
  top: 20%;
  animation: scale-up 3s ease-in-out alternate infinite;
}

.form-image{
  position: absolute;
  left: 0;
  /*width: 200px;*/
}

.cabinet {
  bottom: 65%;
  left: 80%;
  /*transform: translateX(-35%);*/
}

.plants {
  bottom: 50%;
  left: 83%;
  /*transform: translateX(-15%);*/
}

.folder {
  bottom: 15%;
  left: 14%;
}

.resumes {
  /*width: 50%;*/
  bottom: 0;
  left: 25%;
}

.plants{
  animation: scale-down 3s ease-in-out alternate infinite;
}

.folder{
  animation: scale-down 3s ease-in-out alternate infinite;
}

.resumes{
  animation: up-down 3s ease-in-out alternate infinite;
}

.cabinet{
  animation: left-right 3s ease-in-out alternate infinite;
}

@keyframes left-right{
  to{
    transform: translateX(10px);
  }
}

@keyframes up-down {
  to{
    transform: translateY(10px);
  }
}

@keyframes scale-down {
  to{
    transform: scale(0.95);
  }
}

@keyframes scale-up {
  to{
    transform: scale(1.05);
  }
}

.col-2{
  position: relative;
  width: 45%;
  /*padding: 20px;*/
  padding: 70px 20px 20px 20px;
  overflow: hidden;
}

.login-form{
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  padding: 0 4vw;
}

.form-title{
  /*margin: 40px 0;*/
  margin: 10px 0 70px 0;
  color: #fff;
  font-size: 32px;
  font-weight: 500;
}

.form-inputs{
  width: 100%;
}

.input-box{
  position: relative;
}

.input-field{
  width: 100%;
  height: 55px;
  padding: 0 15px;
  margin: 10px 0;
  color: #fff;
  backdrop-filter: blur(20px);
  box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.2);
  background: rgba(255, 255, 255, 0.2);
  border: none;
  border-radius: 10px;
  outline: none;
}

::placeholder{
  color: #fff;
  font-size: 16px;
  font-weight: 500;
}

.input-box .icon{
  position: absolute;
  top: 50%;
  right: 15px;
  transform: translateY(-50%);
  color: #ffffff;
}

.input-submit{
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  width: 100%;
  height: 55px;
  padding: 0 15px;
  margin: 20px 0;
  color: #fff;
  background: #bdabff;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  transition: .3s;
}

.input-submit:hover{
  gap: 15px;
}

.error-message {
  color: red;
  margin-top: 0;
}

@media (max-width: 892px){
  .form-container{
    width: 400px;
  }

  .col-1{
    display: none;
  }

  .col-2{
    width: 100%;
  }
}
</style>