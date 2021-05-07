<template>
  <div class="layer-1 notfound">
    <v-container fluid fill-height class="layer-1">
      <v-row align="center" justify="center">
        <v-col align="center" justify="center">
          <v-card outlined elevation="5" shaped max-width="400" class="pa-9">
            <v-col
              >
            <v-img contain height="200" src="@/assets/404.png"></v-img>
            <router-link to="/"><h4 class="mt-4">Click here to go to Login page.</h4></router-link>
            </v-col>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {};
</script>

<style>
.notfound {
  min-height: 100vh;
}
</style>