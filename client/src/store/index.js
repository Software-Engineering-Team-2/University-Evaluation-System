import Vuex from 'vuex'
import Vue from 'vue'
import auth from './auth'
import search from './search'
import courses from './courses'
import instructor from './instructor'
import axios from 'axios'

axios.defaults.baseURL = 'https://husystem.herokuapp.com/';
// axios.defaults.baseURL = 'http://127.0.0.1:8000/';

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
        auth, search, courses, instructor
    }
})