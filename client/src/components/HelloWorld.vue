<template>
  <v-container fluid fill-height class="layer-1">
    <v-row align="center" justify="center">
      <v-col align="center" justify="center">
        <v-alert
          v-model="verifySuccess"
          color="primary"
          border="left"
          elevation="2"
          colored-border
          type="success"
          dense
          max-width="600"
        >
          Your email is now verified. Please wait for admin to approve your
          email.
        </v-alert>
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
              <v-form ref="login" v-model="valid">
                <v-col>
                  <v-text-field
                    v-model="email"
                    :rules="emailRules"
                    label="Email"
                    required
                    type="email"
                  ></v-text-field>

                  <v-text-field
                    v-model="password1"
                    label="Password"
                    required
                    :type="show1 ? 'text' : 'password'"
                    :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                    @click:append="show1 = !show1"
                    :rules="[(v) => !!v || 'Password is required']"
                  ></v-text-field>
                  <v-select
                    v-model="login_as"
                    :items="login_as_items"
                    label="Login as"
                    :rules="[(v) => !!v || 'Please select one option']"
                  ></v-select>
                  <v-alert
                    v-model="alert"
                    color="primary"
                    border="left"
                    elevation="2"
                    colored-border
                    type="error"
                    v-for="error in errors"
                    :key="error"
                    dense
                  >
                    {{ error }}
                  </v-alert>
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
              <v-form ref="signup" v-model="valid">
                <v-col>
                  <v-text-field
                    v-model="firstname"
                    label="Firstname"
                    required
                    :rules="[(v) => !!v || 'Firstname is required']"
                    type="text"
                  ></v-text-field>
                  <v-text-field
                    v-model="lastname"
                    label="Lastname"
                    required
                    type="text"
                    :rules="[(v) => !!v || 'Lastname is required']"
                  ></v-text-field>
                  <v-text-field
                    v-model="username"
                    label="Username"
                    required
                    type="text"
                    :rules="[(v) => !!v || 'Username is required']"
                  ></v-text-field>
                  <v-text-field
                    v-model="email"
                    :rules="emailRules"
                    label="Email"
                    required
                    type="email"
                  ></v-text-field>

                  <v-text-field
                    v-model="password1"
                    label="Password"
                    required
                    :rules="[(v) => !!v || 'Password is required']"
                    :type="show2 ? 'text' : 'password'"
                    :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
                    @click:append="show2 = !show2"
                  ></v-text-field>
                  <v-text-field
                    v-model="password2"
                    :rules="[
                      (v) => !!v || 'Confirm Password is required',
                      (v) => v === password1 || 'Passwords don\'t match',
                    ]"
                    label="Confirm Password"
                    required
                    :type="show2 ? 'text' : 'password'"
                    :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
                    @click:append="show2 = !show2"
                  ></v-text-field>
                  <v-alert
                    v-model="alert"
                    color="primary"
                    border="left"
                    elevation="2"
                    colored-border
                    :type="success ? 'success' : 'error'"
                    v-for="error in errors"
                    :key="error"
                    dense
                  >
                    {{ error }}
                  </v-alert>
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
    show1: false,
    show2: false,
    tab: null,
    login_as_items: ["Student", "Instructor"],
    email: "",
    password1: "",
    password2: "",
    username: "",
    login_as: "",
    firstname: "",
    lastname: "",
    valid: true,
    errors: [],
    success: null,
    emailRules: [
      (v) => !!v || "E-mail is required",
      (v) => /.+@.+\.habib.edu.pk/.test(v) || "E-mail must be a valid HU email",
    ],
  }),

  methods: {
    ...mapActions({
      signIn: "auth/signIn",
      registerAction: "auth/register",
    }),
    submit() {
      if (this.$refs.login.validate()) {
        this.signIn({
          email: this.email,
          password: this.password1,
          verified: "False",
        }).then((r) => {
          if (r) {
            this.errors = [];
            for (let i in r) {
              this.errors.push(r[i][0]);
            }
          } else {
            this.$router.replace({
              name: "Dashboard",
            });
          }
        });
      }
    },
    register() {
      if (this.$refs.signup.validate()) {
        this.registerAction({
          first_name: this.firstname,
          last_name: this.lastname,
          email: this.email,
          password1: this.password1,
          password2: this.password2,
          username: this.username,
        }).then((r) => {
          if (r) {
            this.errors = [];
            if (r["status"] === 400) {
              for (let i in r["data"]) {
                this.errors.push(r["data"][i][0]);
              }
            } else {
              this.success = true;
              for (let i in r["data"]) {
                this.errors.push(r["data"][i]);
              }
            }
          }
        });
      }
    },
  },
  computed: {
    ...mapGetters({
      isAuthenticated: "auth/isAuthenticated",
      user: "auth/returnUser",
    }),
    verifySuccess () {
      return this.$route.query['success'] != undefined
    }
  },
  watch: {
    tab() {
      this.errors = [];
    },
  },
  mounted () {
    console.log(this.$route.query['success'])
  }
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