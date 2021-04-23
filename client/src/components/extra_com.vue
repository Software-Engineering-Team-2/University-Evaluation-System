<template>
  <div class="hw-100 display-f">
    <Navigation />
    <v-divider></v-divider>
    <v-row class="ma-0">
      <v-col cols="4" class="pa-0">
        <div class="triangle primary d-flex text-left">
          <v-card-title class="font-weight-bold"
            >{{ course.title }}<br />{{ course.school }}</v-card-title
          >
        </div>
        <v-card-text class="mb-2 description">
          <p class="text-left">{{ course.description }}</p>
        </v-card-text>
      </v-col>
      <v-col cols="8" class="purple">
      <v-toolbar card>
          <v-toolbar-title class="font-weight-bold"
            >Reviews &amp; Ratings</v-toolbar-title
          >
        </v-toolbar>

        <v-card-text class="comments">
          <v-row
            v-for="index in 4"
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
      </v-col>
    </v-row>
  </div>
</template>

<script>
import Navigation from "@/components/Navigation";
import { mapActions } from "vuex";

export default {
  data() {
    return {
      course: null,
      select: ["add-tags-with", "enter", "tab", "paste"],
      testing:
        "This is a comment for testing if the functionality is working fine.",
    };
  },
  components: {
    Navigation,
  },
  created() {
    // console.log(this.$route.params)
    this.queryCourse({ id: this.$route.params.id });
  },
  methods: {
    ...mapActions({
      searchResults: "search/search",
    }),
    queryCourse(value) {
      this.searchResults(value).then((response) => {
        this.course = response[0];
      });
    },
  },
};
</script>

<style scoped>
.hw-100 {
  height: 100%;
  width: 100%;
}
.display-f {
  display: flex;
  flex-direction: column;
}
.border-bottom-black {
  border-bottom: thin solid rgba(0, 0, 0, 0.12);
}
.theme--light.v-btn.v-btn--disabled:not(.v-btn--flat):not(.v-btn--text):not(.v-btn-outlined) {
  color: white !important;
  background-color: #4c1c58 !important;
  border-color: #4c1c58 !important;
}
.v-card {
  display: flex !important;
  flex-direction: column;
}

.v-card__text {
  flex-grow: 1;
  overflow: auto;
}

.box-shadow {
  box-shadow: 0px -3px 5px 0px rgb(0 0 0 / 20%),
    0px 4px 5px 0px rgb(0 0 0 / 14%), 0px 1px 10px 0px rgb(0 0 0 / 12%) !important;
}

.skewed {
  position: absolute;
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 0;
  transform: skewY(6deg);
  transform-origin: top right;
}

.triangle {
  position: relative;
  min-height: 50%;
  align-items: flex-end;
  color: white;
}

.description {
  max-height: 50%;
}

.comments {
  max-height: 10%;
}

/* .triangle::before {
  content: '';
  position: absolute;
  bottom: 0;
  width: 0;
  height: 0;
  border-style: solid;
  border-width: 50px 50px 0 50px;
  border-color: rgba(119, 32, 85, 1) transparent transparent transparent;
  left: 50%;
  transform: translateX(-50%) translateY(100%);
} */
</style>