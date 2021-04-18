import Vuex from 'vuex'
import Vue from 'vue'
import auth from './auth'
import search from './search'

Vue.use(Vuex)
Vue.config.devtools = true

export default new Vuex.Store({
    state: {
        //
    },
    mutations: {
        //
    },
    actions: {
        //
    },
    modules: {
        auth, search
    }
})