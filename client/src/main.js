import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import router from './router'
import store from './store'

Vue.config.productionTip = false

require('@/store/subscriber')

store.dispatch('auth/attempt', localStorage.getItem('token')).then(
  new Vue({
    vuetify,
    store,
    router,
    render: h => h(App)
  }).$mount('#app')
)
