<template>
      <div class="d-flex mt-auto mb-auto justify-center">
      <v-card class="mr-5" outlined elevation="5" width="400" height="500">
        <div class="triangle layer-1 d-flex text-left">
          <v-card-title class="font-weight-bold"
            >{{ course.title }}<br />{{ course.school }}</v-card-title
          >
        </div>
        <v-card-text class="mb-2">
          <p class="text-left">{{ course.description }}</p>
        </v-card-text>
        <!-- <v-footer class="white"></v-footer> -->
      </v-card>

      <v-card
        outlined
        elevation="5"
        height="500"
        class="text-left"
        max-width="800"
        max-height="500"
      >
        <v-toolbar card>
          <v-toolbar-title class="font-weight-bold"
            >Reviews &amp; Ratings</v-toolbar-title
          >
        </v-toolbar>

        <v-card-text>
          <v-row
            v-for="index in 10"
            :key="index"
            class="justify-space-around border-bottom-black"
          >
            <v-col
              cols="1"
              class="d-flex flex-column justify-center align-center"
            >
              <v-icon color="primary" large>mdi-arrow-up-drop-circle</v-icon>
              <h5 class="align-center">0</h5>
              <v-icon color="primary" large>mdi-arrow-down-drop-circle</v-icon>
            </v-col>
            <v-col
              cols="auto"
              class="d-flex flex-column justify-center align-center"
            >
              <h5>Overall Rating</h5>
              <v-rating
                v-model="rating"
                color="yellow darken-3"
                background-color="grey darken-1"
                half-increments
                hover
                clearable
                dense
              ></v-rating>
            </v-col>
            <v-col cols="4" class="mt-auto mb-auto">
              <h5>Comments</h5>
              <p class="mb-0">
                This is a testing comment. It can be longer as well as short
              </p>
            </v-col>
            <v-col
              cols="4"
              class="d-flex flex-column justify-center align-center"
            >
              <h5>Tags</h5>
              <v-chip-group active-class="primary--text" column>
                <v-chip small color="primary"> hardworking </v-chip>
                <v-chip small color="primary"> test </v-chip
                ><v-chip small color="primary"> stupid </v-chip
                ><v-chip small color="primary"> bad grader </v-chip
                ><v-chip small color="primary"> tough </v-chip
                ><v-chip small color="primary"> hard </v-chip>
              </v-chip-group>
            </v-col>
          </v-row>
        </v-card-text>
        <v-footer color="white" class="box-shadow pa-2">
          <v-row class="justify-space-around pa-1">
            <v-col
              cols="auto"
              class="d-flex flex-column justify-center align-center"
            >
              <h5>Overall Rating</h5>
              <v-rating
                v-model="rating"
                color="yellow darken-3"
                background-color="grey darken-1"
                half-increments
                hover
                clearable
                dense
              ></v-rating>
            </v-col>
            <v-col cols="4" class="mt-auto mb-auto">
              <h5>Comments</h5>
              <v-textarea outlined rows="2" hide-details flat></v-textarea>
            </v-col>
            <v-col cols="4" class="d-flex flex-column justify-center">
              <h5>Add Tags</h5>

              <v-combobox
                multiple
                v-model="select"
                outlined
                hide-details
                chips
                deletable-chips
                append-icon
              >
                <template v-slot:selection="data">
                  <v-chip small color="primary">
                    {{ data.item }}
                  </v-chip>
                </template>
              </v-combobox>
            </v-col>
            <v-col cols="auto d-flex justify-center align-center">
              <v-btn dark small color="primary"> Submit </v-btn>
            </v-col>
          </v-row>
        </v-footer>
      </v-card>
    </div>

</template>

<script>
export default {

}
</script>

<style>

</style>