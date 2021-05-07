<template>
  <div>
    <Navigation />
    <v-row class="dash" align="center" justify="center">
      <v-col cols="6" align="center" justify="center">
        <v-avatar size="150">
          <v-icon size="150"> mdi-account-circle </v-icon>
        </v-avatar>
        <h1>Welcome, {{ user.first_name + " " + user.last_name }}</h1>
        <p>Please use the search bar to search for instructors or courses. You can post your reviews, and view already posted reviews about a particular course/instructor</p>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import Navigation from "@/components/Navigation";

export default {
  components: {
    Navigation,
  },
  methods: {
    ...mapActions({
      signOutAction: "auth/signOut",
    }),
    signOut() {
      this.signOutAction().then(() => {
        this.$router.replace("/");
      });
    },
  },
  computed: {
    ...mapGetters({
      isAuthenticated: "auth/isAuthenticated",
      user: "auth/returnUser",
    }),
  },
};
</script>

<style>
.dash {
  height: calc(100vh - 64px);
}
</style>