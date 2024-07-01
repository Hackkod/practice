import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/LoginPage.vue'
import Students from '../views/StudentsPage.vue'
import Mentors from '../views/MentorsPage.vue'
import Studies from '../views/StudyPage.vue'
import Works from '../views/WorkPage.vue'
import { getToken } from "@/services/auth";
import MainLayout from "@/views/MainLayout.vue";

const routes = [
  // {
  //   path: '/',
  //   redirect: '/login',
  // },
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
          pageName: 'Студенты',
          activeIndex: 0,
          tabs: [
            { name: 'Карта' },
            { name: 'Таблица' }
          ],
        }
      },
      {
        path: '/mentors',
        name: 'Mentors',
        component: Mentors,
        meta: {
          requiresAuth: true,
          pageName: 'Наставники',
          activeIndex: 1,
          tabs: [
            { name: 'Карта' },
            { name: 'Таблица' }
          ],
        }
      },
      {
        path: '/studies',
        name: 'Studies',
        component: Studies,
        meta: {
          requiresAuth: true,
          pageName: 'Стажировки и практики',
          activeIndex: 2,
          tabs: [
            { name: 'Таблица' }
          ],
        }
      },
      {
        path: '/works',
        name: 'Works',
        component: Works,
        meta: {
          requiresAuth: true,
          pageName: 'Работа',
          activeIndex: 3,
          tabs: [
            { name: 'Таблица' }
          ],
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
