import axios from 'axios'

export default {
    namespaced: true,
    state: {
        token: null,
        user: null,
        loading: null,
        userLoading: null
    },
    getters: {
        isAuthenticated (state) {
            return state.token !== null
        },
        returnUser (state) {
            return state.user
        },
        loadingStatus (state) {
            if (state.loading != null || state.userLoading != null)
                return state.loading || state.userLoading
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
            state.userLoading = false
        },
        SET_LOADING_TRUE (state) {
            state.loading = true
        },
        SET_LOADING_FALSE (state) {
            state.loading = false
        },
        SET_USER_LOADING_TRUE (state) {
            state.userLoading = true
        },
        SET_USER_LOADING_FALSE (state) {
            state.userLoading = false
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
            commit('SET_USER_LOADING_TRUE')
            if (token['key']) {
                commit('SET_TOKEN', token['key'])  
            }

            if (!state.token) {
                commit('SET_LOADING_FALSE')
                commit('SET_USER_LOADING_FALSE')
                return token
            }

            try {
                let response = await axios.get('/dj-rest-auth/user/')
                commit('SET_USER', response.data)
                commit('SET_LOADING_FALSE')
            } catch (e) {
                commit('SET_TOKEN', null)
                commit('SET_USER', null)
                commit('SET_LOADING_FALSE')
            }
        },
        signOut ({ commit }) {
            commit('SET_LOADING_TRUE')
            return axios.post('/dj-rest-auth/logout/').then(() => {
                commit('SET_TOKEN', null)
                commit('SET_USER', null)
                commit('SET_LOADING_FALSE')
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