<template>
  <div class="hw-100 display-f">
    <Navigation />
    <v-card
      outlined
      elevation="5"
      min-height="400"
      max-width="400"
      class="pa-9 mt-auto mb-auto"
    >
      <div></div>
      <v-avatar color="primary" size="200"
        ><v-icon dark size="150"> mdi-account-circle </v-icon></v-avatar
      >
    </v-card>
  </div>
</template>

<script>
import Navigation from "@/components/Navigation";

export default {
  components: {
    Navigation,
  },
};
</script>

<style>
.hw-100 {
  height: 100%;
  width: 100%;
}
.display-f {
  display: flex;
  flex-direction: column;
}
</style>