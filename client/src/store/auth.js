import axios from 'axios'

export default {
    namespaced: true,
    state: {
        token: null,
        user: null,
        loading: null
    },
    getters: {
        isAuthenticated (state) {
            return state.token !== null
        },
        returnUser (state) {
            return state.user
        },
        loadingStatus (state) {
            if (state.loading != null)
                return state.loading
            else
                return false
        }
    },
    mutations: {
        SET_TOKEN (state, token) {
            state.token = token
        },
        SET_USER (state, user) {
            state.user = user
            state.loading = false
        },
        SET_LOADING_TRUE (state) {
            state.loading = true
        },
        SET_LOADING_FALSE (state) {
            state.loading = false
        }
    },
    actions: {
        async signIn({ commit, dispatch }, credentials) {
            commit('SET_LOADING_TRUE')
            let response = await axios.post('/dj-rest-auth/login/', credentials).catch(error => {console.log(error)})
            return dispatch('attempt', response.data.key)
        },
        async attempt ({ commit, state }, token) {
            if (token) {
                commit('SET_TOKEN', token)  
            }

            if (!state.token) {
                return
            }

            try {
                let response = await axios.get('/dj-rest-auth/user/')
                commit('SET_USER', response.data)
            } catch (e) {
                commit('SET_TOKEN', null)
                commit('SET_USER', null)
            }
        },
        signOut ({ commit }) {
            commit('SET_LOADING_TRUE')
            return axios.post('/dj-rest-auth/logout/').then(() => {
                commit('SET_TOKEN', null)
                commit('SET_USER', null)
            })
        },
        register ({ commit }, data) {
            commit('SET_LOADING_TRUE')
            return axios.post('/dj-rest-auth/registration/', data).then(() => {
                commit('SET_LOADING_FALSE')
            }).catch(() => {
                commit('SET_LOADING_FALSE')
            })
        }
    }
}