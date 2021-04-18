import axios from 'axios'

export default {
    namespaced: true,
    state: {
        // token: null,
        // user: null,
        search_results: null
    },
    getters: {
        // isAuthenticated (state) {
        //     return state.token !== null
        // },
        // returnUser (state) {
        //     return state.user
        // }
    },
    mutations: {
        // SET_TOKEN (state, token) {
        //     state.token = token
        // },
        // SET_USER (state, user) {
        //     state.user = user
        // }
    },
    actions: {
        async search (_, request) {
            let response = await axios.get("http://127.0.0.1:8000/get-courses", {params: request}).catch(error => {
                console.log(error)
            })
            return response.data
        }
        // async signIn({ dispatch }, credentials) {
        //     let response = await axios.post('http://127.0.0.1:8000/dj-rest-auth/login/', credentials).catch(error => {console.log(error)})
        //     return dispatch('attempt', response.data.key)
        // },
        // async attempt ({ commit, state }, token) {
        //     if (token) {
        //         commit('SET_TOKEN', token)  
        //     }

        //     if (!state.token) {
        //         return
        //     }

        //     try {
        //         let response = await axios.get('http://127.0.0.1:8000/dj-rest-auth/user/')
        //         commit('SET_USER', response.data)
        //     } catch (e) {
        //         commit('SET_TOKEN', null)
        //         commit('SET_USER', null)
        //     }
        // },
        // signOut ({ commit }) {
        //     return axios.post('http://127.0.0.1:8000/dj-rest-auth/logout/').then(() => {
        //         commit('SET_TOKEN', null)
        //         commit('SET_USER', null)
        //     })
        // },
        // register (_, data) {
        //     console.log(data)
        //     return axios.post('http://127.0.0.1:8000/dj-rest-auth/registration/', data).catch((e) => {
        //         console.log(e)
        //     })  
        // }
    }
}