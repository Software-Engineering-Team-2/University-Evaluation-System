<template>
  <v-container fluid fill-height class="layer-1">
    <v-row align="center" justify="center">
      <v-col align="center" justify="center">
        <v-card outlined elevation="5" shaped max-width="400" class="pa-9">
          <v-img contain height="100" src="@/assets/hu-logo.png"></v-img>
          <v-col
            ><v-tabs fixed-tabs class="mt-4" v-model="tab">
              <v-tab> Login </v-tab>
              <v-tab> SignUp </v-tab>
            </v-tabs>
          </v-col>
          <v-tabs-items v-model="tab">
            <v-tab-item>
              <v-form v-model="valid">
                <v-col>
                  <v-text-field
                    v-model="email"
                    :rules="nameRules"
                    label="Email"
                    required
                    type="email"
                  ></v-text-field>

                  <v-text-field
                    v-model="password1"
                    :rules="nameRules"
                    label="Password"
                    required
                    type="password"
                  ></v-text-field>
                  <v-select
                    v-model="login_as"
                    :items="login_as_items"
                    label="Login as"
                  ></v-select>
                  <div>
                    <v-btn
                      @click="submit"
                      color="primary"
                      class="mt-4 mb-4 mr-3"
                    >
                      Login
                    </v-btn>
                  </div>
                  <div>
                    <p><a>Forgot Password?</a></p>
                  </div>
                </v-col>
              </v-form>
            </v-tab-item>
            <v-tab-item>
              <v-form v-model="valid">
                <v-col>
                  <v-text-field
                    v-model="firstname"
                    :rules="nameRules"
                    label="Firstname"
                    required
                    type="text"
                  ></v-text-field>
                  <v-text-field
                    v-model="lastname"
                    :rules="nameRules"
                    label="Lastname"
                    required
                    type="text"
                  ></v-text-field>
                  <v-text-field
                    v-model="username"
                    :rules="nameRules"
                    label="Username"
                    required
                    type="text"
                  ></v-text-field>
                  <v-text-field
                    v-model="email"
                    :rules="nameRules"
                    label="Email"
                    required
                    type="email"
                  ></v-text-field>

                  <v-text-field
                    v-model="password1"
                    :rules="nameRules"
                    label="Password"
                    required
                    type="password"
                  ></v-text-field>
                  <v-text-field
                    v-model="password2"
                    :rules="nameRules"
                    label="Confirm Password"
                    required
                    type="password"
                  ></v-text-field>
                  <div>
                    <v-btn color="primary" class="mt-4 mb-4" @click="register">
                      Sign-Up
                    </v-btn>
                  </div>
                </v-col>
              </v-form>
            </v-tab-item>
          </v-tabs-items>
          <div>
            <a>
              <v-icon color="primary"> mdi-email </v-icon>
              <span class="icon-link"> Contact Us </span>
            </a>
          </div>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapActions } from "vuex";
import { mapGetters } from "vuex";

export default {
  name: "HelloWorld",

  data: () => ({
    tab: null,
    login_as_items: ["Student", "Instructor"],
    email: "",
    password1: "",
    password2: "",
    username: "",
    login_as: "",
    firstname: "",
    lastname: "",
  }),

  methods: {
    ...mapActions({
      signIn: "auth/signIn",
      registerAction: "auth/register",
    }),
    submit() {
      this.signIn({
        email: this.email,
        password: this.password1,
        verified: "False",
      }).then(() => {
        this.$router.replace({
          name: "Dashboard",
        });
      });
    },
    register() {
      this.registerAction({
        first_name: this.firstname,
        last_name: this.lastname,
        email: this.email,
        password1: this.password1,
        password2: this.password2,
        username: this.username,
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
.layer-1 {
  background: -moz-linear-gradient(
    45deg,
    rgba(227, 42, 74, 1) 0%,
    rgba(119, 32, 85, 1) 54%,
    rgba(76, 28, 88, 1) 100%
  );
  background: -webkit-linear-gradient(
    45deg,
    rgba(227, 42, 74, 1) 0%,
    rgba(119, 32, 85, 1) 54%,
    rgba(76, 28, 88, 1) 100%
  );
  background: -o-linear-gradient(
    45deg,
    rgba(227, 42, 74, 1) 0%,
    rgba(119, 32, 85, 1) 54%,
    rgba(76, 28, 88, 1) 100%
  );
  background: -ms-linear-gradient(
    45deg,
    rgba(227, 42, 74, 1) 0%,
    rgba(119, 32, 85, 1) 54%,
    rgba(76, 28, 88, 1) 100%
  );
  background: linear-gradient(
    45deg,
    rgba(227, 42, 74, 1) 0%,
    rgba(119, 32, 85, 1) 54%,
    rgba(76, 28, 88, 1) 100%
  );
}
.icon-link {
  vertical-align: middle;
}
</style>