import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '@/components/HelloWorld'
import Dashboard from '@/components/Dashboard'
import courseProfile from '@/components/courseProfile'
import instructorProfile from '@/components/instructorProfile'
import pageNotFound from '@/components/pageNotFound'
import store from '@/store'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login,
    beforeEnter: (to, from, next) => {
      if (store.getters['auth/isAuthenticated']) {
        return next({
          name: 'Dashboard'
        })
      }
      next()
    },
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    beforeEnter: (to, from, next) => {
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
    component: courseProfile,
    beforeEnter: (to, from, next) => {
      if (!store.getters['auth/isAuthenticated']) {
        return next({
          name: 'Login'
        })
      }
      next()
    }, 
  },
  {
    path: '/instructor/:id',
    name: 'Instructor',
    component: instructorProfile,
    beforeEnter: (to, from, next) => {
      if (!store.getters['auth/isAuthenticated']) {
        return next({
          name: 'Login'
        })
      }
      next()
    },
  },
  {
    path: '*',
    component: pageNotFound
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
