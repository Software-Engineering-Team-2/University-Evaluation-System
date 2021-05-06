<template>
  <div id="app">
    <v-app>
      <pageLoader />
      <router-view :key="$route.path"/>
    </v-app>
  </div>
</template>

<script>
import pageLoader from './components/pageLoader'
export default {
  components: {
    pageLoader
  }
}
</script>

<style lang="scss">
.v-application--wrap {
  min-height: 100%!important;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  min-width: 100vh;
  min-height: 100vh;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
html {
  overflow-x: scroll !important;
  height: 100%;
}

body {
  height: 100%;
}

/* Hide scrollbar for Chrome, Safari and Opera */
html::-webkit-scrollbar {
  display: none;
}

/* Hide scrollbar for IE, Edge and Firefox */
html {
  -ms-overflow-style: none;  /* IE and Edge */
  scrollbar-width: none;  /* Firefox */
}
</style>

