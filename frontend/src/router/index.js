import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/LoginPage.vue'
import Students from '../views/StudentsPage.vue'
import Mentors from '../views/MentorsPage.vue'
import Studies from '../views/StudyPage.vue'
import Works from '../views/WorkPage.vue'
import { getToken } from "@/services/auth";
import MainLayout from "@/views/MainLayout.vue";

const routes = [
  {
    path: '/',
    redirect: '/login',
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
    meta: { requiresAuth: false }
  },
  {
    path: '/',
    component: MainLayout,
    meta: { requiresAuth: true },
    children: [
      {
        path: '/students',
        name: 'Students',
        component: Students,
        meta: {
          requiresAuth: true,
          activeIndex: 0,
        }
      },
      {
        path: '/mentors',
        name: 'Mentors',
        component: Mentors,
        meta: {
          requiresAuth: true,
          activeIndex: 1,
        }
      },
      {
        path: '/studies',
        name: 'Studies',
        component: Studies,
        meta: {
          requiresAuth: true,
          activeIndex: 2,
        }
      },
      {
        path: '/works',
        name: 'Works',
        component: Works,
        meta: {
          requiresAuth: true,
          activeIndex: 3,
        }
      },
    ]
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth) && !getToken()) {
      next({ name: 'Login' });
  } else {
    next();
  }
})

export default router
