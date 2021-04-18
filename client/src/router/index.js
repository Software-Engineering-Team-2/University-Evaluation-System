import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '@/components/HelloWorld'
import Dashboard from '@/components/Dashboard'
import Course_Profile from '@/components/Course_Profile'
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
    path: '/course',
    name: 'Course',
    component: Course_Profile
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
