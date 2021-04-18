<template>
  <div>
    <Navigation />
    <h1> {{ user }} </h1>
    <v-btn @click="signOut">Sign Out</v-btn>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import Navigation from '@/components/Navigation'

export default {
  components: {
    Navigation
  },
  methods: {
    ...mapActions({
      signOutAction: 'auth/signOut'
    }),
    signOut () {
      this.signOutAction().then(() => {
        this.$router.replace('/')
      })
    }
  },
  computed: {
    ...mapGetters({
      isAuthenticated: 'auth/isAuthenticated',
      user: 'auth/returnUser'
    })
  }
}
</script>

<style>

</style>