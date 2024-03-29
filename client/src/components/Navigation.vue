<template>
  <div>
    <v-app-bar class="layer-1" dark>
      <v-app-bar-nav-icon
        class="hidden-sm-and-up"
        @click.stop="drawer = !drawer"
      ></v-app-bar-nav-icon>
      <img height="50" src="@/assets/hu-logo.png" class="mr-3" />

      <v-spacer></v-spacer>

      <v-combobox
        solo
        light
        hide-details
        clearable
        no-filter
        :search-input.sync="searchString"
        v-model="selected"
        :items="items"
        append-icon="mdi-magnify"
        label="Search"
        class="notranslate"
      >
        <template v-slot:no-data>
          <p class="ml-3 mt-3">Please enter search query.</p>
        </template>
        <template v-slot:item="{ item }">
          <!-- HTML that describe how select should render items when the select is open -->
          <v-list-item
            link
            v-if="item.school"
            :to="{
              name: 'Course',
              params: { id: item.id },
            }"
            >{{ item.text }} {{ item.school ? " - "+item.school : "" }}</v-list-item
          >
          <v-list-item
            link
            v-else
            :to="{
              name: 'Instructor',
              params: { id: item.id },
            }"
            >{{ item.text }} {{ item.school ? " - "+item.school : "" }}</v-list-item
          >
        </template>
      </v-combobox>
      <v-spacer></v-spacer>

      <v-menu class="display-block" v-if="user">
        <template v-slot:activator="{ attrs, on }">
          <v-btn class="white--text" v-bind="attrs" v-on="on" plain>
            {{ user.first_name + " " + user.last_name }}
            <v-icon class="ml-1">mdi-account-circle</v-icon>
          </v-btn>
        </template>

        <v-list>
          <v-list-item link>
            <v-list-item-title @click="signOut"
              ><v-icon>mdi-logout</v-icon>
              <span class="vertical-align-middle"
                >Logout</span
              ></v-list-item-title
            >
          </v-list-item>
        </v-list>
      </v-menu>
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" absolute bottom temporary>
      <v-list nav dense>
        <v-list-item-group
          v-model="group"
          active-class="deep-purple--text text--accent-4"
        >
          <v-list-item>
            <v-list-item-title>Foo</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-title>Bar</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-title>Fizz</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-title>Buzz</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
  data() {
    return {
      drawer: false,
      group: null,
      searchString: null,
      selected: null,
      items: [],
    };
  },
  computed: {
    ...mapGetters({
      isAuthenticated: "auth/isAuthenticated",
      user: "auth/returnUser",
    }),
  },
  methods: {
    ...mapActions({
      signOutAction: "auth/signOut",
      searchCourse: "search/courseSearch",
      searchInstructor: "search/instructorSearch",
    }),
    signOut() {
      this.signOutAction().then(() => {
        this.$router.replace("/");
      });
    },
    async searchResults(value1, value2) {
      let courses = await this.searchCourse(value1);
      let instructors = await this.searchInstructor(value2);
      return [courses, instructors];
    },
  },
  watch: {
    group() {
      this.drawer = false;
    },
    searchString() {
      if (this.searchString) {
        this.searchResults(
          {
            title: this.searchString ? this.searchString : "",
          },
          {
            name: this.searchString ? this.searchString : "",
          }
        ).then((response) => {
          this.items = [];
          if (response[0].length != 0) {
            this.items.push({ header: "Courses" });
            response[0].forEach((element) => {
              this.items.push({
                text: element.title,
                value: element.title,
                school: element.school,
                id: element.id
              });
            });
          }
          if (response[1].length != 0) {
            this.items.push({ header: "Instructors" });
            response[1].forEach((element) => {
              this.items.push({
                text: element.name,
                value: element.name,
                id: element.id
              });
            });
          }
        });
      } else {
        this.items = [];
      }
    },
  },
};
</script>

<style>
.display-block {
  display: block;
}
.vertical-align-middle {
  vertical-align: middle;
}
.notranslate {
  transform: none !important;
}
</style>