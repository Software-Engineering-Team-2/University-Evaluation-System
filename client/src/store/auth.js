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
            let response = await axios.post('/dj-rest-auth/login/', credentials).catch(error => {
                commit('SET_LOADING_FALSE')
                return error.response
            })
            return dispatch('attempt', response.data)
        },
        async attempt ({ commit, state }, token) {
            if (token['key']) {
                commit('SET_TOKEN', token['key'])  
            }

            if (!state.token) {
                return token
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
            return axios.post('/dj-rest-auth/registration/', data).then((response) => {
                commit('SET_LOADING_FALSE')
                return response
            }).catch(error => {
                commit('SET_LOADING_FALSE')
                return error.response
            })
        }
    }
}