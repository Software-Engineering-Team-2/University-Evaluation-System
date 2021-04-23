import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '@/components/HelloWorld'
import Dashboard from '@/components/Dashboard'
import courseProfile from '@/components/courseProfile'
import instructorProfile from '@/components/instructorProfile'
import store from '@/store'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    beforeEnter: (to, from, next) => {
      console.log(store.getters['auth/isAuthenticated'])
      if (!store.getters['auth/isAuthenticated']) {
        return next({
          name: 'Login'
        })
      }
      next()
    },
  },
  {
    path: '/course/:id',
    name: 'Course',
    component: courseProfile
  },
  {
    path: '/instructor/:id',
    name: 'Instructor',
    component: instructorProfile
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
