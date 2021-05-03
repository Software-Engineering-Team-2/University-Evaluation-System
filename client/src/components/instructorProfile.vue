<template>
  <div>
    <Navigation />
    <v-row class="ma-0">
      <!-- instructor info -->
      <v-col cols="4" class="pa-0">
        <v-toolbar class="profile pb-4 primary d-flex justify-center">
          <v-avatar size="150" class="margin-neg">
            <v-img
              class="outlined"
              src="https://cdn.vuetifyjs.com/images/profiles/marcus.jpg"
            ></v-img>
          </v-avatar>
        </v-toolbar>
        <v-toolbar-title class="font-weight-bold mt-16" v-if="instructor"
          >{{ instructor.name }}<br />{{ instructor.email }}</v-toolbar-title
        >
        <v-card-text class="mb-2 description-instructor" v-if="instructor">
          <p class="text-left">{{ instructor.description }}</p>
        </v-card-text>
      </v-col>
      <!-- instructor info end -->
      <v-divider vertical></v-divider>
      <!-- reviews -->
      <v-col cols="8" class="pa-0">
        <!-- review title -->
        <v-toolbar class="toolbar">
          <v-toolbar-title class="font-weight-bold"
            >Reviews &amp; Ratings</v-toolbar-title
          >
        </v-toolbar>
        <!-- reviews all -->
        <v-card-text class="comments">
          <v-row
            v-for="review in instructorReviews"
            :key="review.id"
            class="justify-space-around border-bottom-black"
          >
            <v-col
              cols="1"
              class="d-flex flex-column justify-center align-center"
            >
              <v-btn
                @click="updateVotes(review.id, 'up')"
                class="mx-2"
                icon
                x-large
                :color="review.voted == 'up' ? '#dd294a' : 'primary'"
              >
                <v-icon class="icon-large"> mdi-arrow-up-drop-circle </v-icon>
              </v-btn>
              <h4 class="align-center">{{ review.und_score }}</h4>
              <v-btn
                @click="updateVotes(review.id)"
                class="mx-2"
                icon
                x-large
                :color="review.voted == 'down' ? '#dd294a' : 'primary'"
              >
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

function compare(a, b) {
  if (a.und_score < b.und_score) {
    return 1;
  }
  if (a.und_score > b.und_score) {
    return -1;
  }
  return 0;
}

export default {
  data() {
    return {
      instructor: null,
      instructorReviews: [],
      select: ["add-tags-with", "enter", "tab", "paste"],
      review: {
        instructorID: null,
        rating: null,
        comments: null,
      },
    };
  },
  components: {
    Navigation,
  },
  created() {
    this.queryInstructor({ id: this.$route.params.id }).then(() => {
      this.getInstructorReviews({ instructorID: this.instructor.id });
    });
  },
  methods: {
    ...mapActions({
      searchResults: "search/instructorSearch",
      fetchInstructorReviews: "instructor/fetchInstructorReviews",
      postInstructorReviews: "instructor/postInstructorReviews",
      updateVotesAPI: "instructor/updateVotes",
      getInstructorReviewVotes: "instructor/getInstructorReviewVotes"
    }),
    async queryInstructor(value) {
      await this.searchResults(value).then((response) => {
        this.instructor = response[0];
        this.review.instructorID = this.instructor.id;
      });
    },
    getInstructorReviews(value) {
      this.fetchInstructorReviews(value).then((response) => {
        response.forEach(element => {
          this.getInstructorReviewVotes({instructorReviewId: element.id}).then((r) => {
            if (r.score === 1)
              this.$set(element, 'voted', 'up')
            else
              this.$set(element, 'voted', 'down')
          })
        })
        return response
      }).then((data) => {
        console.log(data)
        this.instructorReviews = data
        this.instructorReviews.sort( compare )
      });
    },
    submitReview() {
      this.postInstructorReviews(this.review).then(() => {
        this.instructorReviews.push(this.review);
        this.review = {
          instructorID: null,
          rating: null,
          comments: null,
        };
      });
    },
    updateVotes(id, type="down") {
      this.updateVotesAPI({ id: id, type: type }).then(() => {
        this.getInstructorReviews({ instructorID: this.instructor.id });
      });
    }
  },
};
</script>

<style>
.description-instructor {
  max-height: calc(60vh - 124px);
}

.profile {
  position: relative;
  min-height: calc(40vh - 72px);
  align-items: flex-end;
  color: white !important;
}

.margin-neg {
  position: absolute;
  left: 50%;
  transform: translateX(-50%) translateY(50%);
  bottom: 0px;
}
</style>