<template>
  <div>
    <Navigation />
    <v-row class="ma-0">
      <!-- course info -->
      <v-col cols="4" class="pa-0">
        <v-toolbar card class="triangle pb-4 primary d-flex text-left">
          <v-toolbar-title class="font-weight-bold"
            >{{ course.title }}<br />{{ course.school }}</v-toolbar-title
          >
        </v-toolbar>
        <v-card-text class="mb-2 description">
          <p class="text-left">{{ course.description }}</p>
        </v-card-text>
      </v-col>
      <!-- course info end -->
      <v-divider vertical></v-divider>
      <!-- reviews -->
      <v-col cols="8" class="pa-0">
        <!-- review title -->
        <v-toolbar class="toolbar" card>
          <v-toolbar-title class="font-weight-bold"
            >Reviews &amp; Ratings</v-toolbar-title
          >
        </v-toolbar>
        <!-- reviews all -->
        <v-card-text class="comments">
          <v-row
            v-for="review in courseReviews"
            :key="review.id"
            class="justify-space-around border-bottom-black"
          >
            <v-col
              cols="1"
              class="d-flex flex-column justify-center align-center"
            >
              <v-btn @click="updateVotes(review.id, review.votes, 1)" class="mx-2" icon x-large color="primary">
                <v-icon class="icon-large"> mdi-arrow-up-drop-circle </v-icon>
              </v-btn>
              <h4 class="align-center"> {{ review.votes }} </h4>
              <v-btn @click="updateVotes(review.id, review.votes, -1)" class="mx-2" icon x-large color="primary">
                <v-icon class="icon-large"> mdi-arrow-down-drop-circle </v-icon>
              </v-btn>
            </v-col>
            <v-col
              cols="auto"
              class="d-flex flex-column justify-center align-center"
            >
              <h4>Overall Rating</h4>
              <v-rating
                readonly
                v-model="review.rating"
                color="yellow darken-3"
                background-color="grey darken-1"
                half-increments
                hover
                clearable
                dense
              ></v-rating>
            </v-col>
            <v-col cols="4" class="mt-auto mb-auto">
              <h4>Comments</h4>
              <p class="mb-0 text-left">
                {{ review.comments }}
              </p>
            </v-col>
            <v-col
              cols="4"
              class="d-flex flex-column justify-center align-center"
            >
              <h4>Tags</h4>
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
        <!-- reviews all end -->

        <!-- add review  -->
        <v-row
          no-gutters
          class="box-shadow justify-space-around pa-1 pt-2 pb-2 ma-0"
        >
          <v-col
            cols="auto"
            class="d-flex flex-column justify-center align-center"
          >
            <h5>Overall Rating</h5>
            <v-rating
              v-model="review.rating"
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
            <v-textarea
              v-model="review.comments"
              outlined
              rows="2"
              hide-details
              flat
            ></v-textarea>
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
            <v-btn @click="submitReview" dark small color="primary">
              Submit
            </v-btn>
          </v-col>
        </v-row>
        <!-- add review end -->
      </v-col>
      <!-- reviews end -->
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
      courseReviews: [],
      select: ["add-tags-with", "enter", "tab", "paste"],
      review: {
        courseSemesterID: null,
        rating: null,
        comments: null,
      },
    };
  },
  components: {
    Navigation,
  },
  created() {
    // console.log(this.$route.params)
    this.queryCourse({ id: this.$route.params.id }).then(() => {
      this.getCourseReviews({ courseSemesterID: this.course.id });
    });
  },
  methods: {
    ...mapActions({
      searchResults: "search/courseSearch",
      fetchCourseReviews: "courses/fetchCourseReviews",
      postCourseReviews: "courses/postCourseReviews",
      updateVotesAPI: "courses/updateVotes"
    }),
    async queryCourse(value) {
      await this.searchResults(value).then((response) => {
        this.course = response[0];
        this.review.courseSemesterID = this.course.id;
      });
    },
    getCourseReviews(value) {
      this.fetchCourseReviews(value).then((response) => {
        this.courseReviews = response;
      });
    },
    submitReview() {
      this.postCourseReviews(this.review).then(() => {
        this.courseReviews.push(this.review);
        this.review = {
          courseSemesterID: null,
          rating: null,
          comments: null,
        };
      });
    },
    updateVotes (id, votes, val) {
      this.updateVotesAPI({id: id, votes: votes+val}).then((response) => {
        console.log(response)
      })
    }
  },
};
</script>

<style>
.icon-large {
  font-size: 35px !important;
}
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

.description {
  max-height: 50vh;
}

.comments {
  max-height: calc(100vh - 231px);
  max-height: -moz-calc(100vh - 231px);
  max-height: -webkit-calc(100vh - 231px);
  min-height: calc(100vh - 231px);
  min-height: -moz-calc(100vh - 231px);
  min-height: -webkit-calc(100vh - 231px);
}

.triangle {
  position: relative;
  min-height: calc(50vh - 72px);
  align-items: flex-end;
  color: white !important;
}

.box-shadow {
  -webkit-box-shadow: 0px -4px 3px rgb(0 0 0 / 20%);
  -moz-box-shadow: 0px -4px 3px rgb(0 0 0 / 20%);
  box-shadow: 0px -4px 3px rgb(0 0 0 / 20%);
}

.toolbar {
  margin-left: 1px;
}
</style>