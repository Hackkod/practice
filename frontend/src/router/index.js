import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomePage.vue'
import Login from '../views/LoginPage.vue'
import { getToken } from "@/services/auth";

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView,
    meta: {requiresAuth: true}
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
    meta: {requiresAuth: false}
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!getToken()) {
      next({ name: 'Login' });
    } else {
      next();
    }
  } else {
    next();
  }
})

export default router
