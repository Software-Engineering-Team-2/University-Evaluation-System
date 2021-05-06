<template>
  <div class="page-loader layer-2" v-if="!isloaded || loading">
    <div class="cube"></div>
    <div class="cube"></div>
    <div class="cube"></div>
    <div class="cube"></div>
    <div class="cube"></div>
  </div> 
</template>

<script>
import { mapGetters } from 'vuex'

  export default {
    data: () => {
      return {
        isloaded: false
      }
    },
    mounted() {
      document.onreadystatechange = () => {
        if (document.readyState == "complete") { 
          this.isloaded = true;
        } 
      }
    },
    computed: {
      ...mapGetters({
          loading: 'auth/loadingStatus'
        })
    }
  }
</script>

<style lang="scss" scoped>
//    $colors: #8CC271, #69BEEB, #F5AA39, #E9643B;
  
  .page-loader {
    display: flex;
    justify-content: center;
    align-items: center;
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 999;
  }

  .layer-2 {
    background: -moz-linear-gradient(
        45deg,
        rgba(227, 42, 74, 0.9) 0%,
        rgba(119, 32, 85, 0.9) 54%,
        rgba(76, 28, 88, 0.9) 100%
    );
    background: -webkit-linear-gradient(
        45deg,
        rgba(227, 42, 74, 0.9) 0%,
        rgba(119, 32, 85, 0.9) 54%,
        rgba(76, 28, 88, 0.9) 100%
    );
    background: -o-linear-gradient(
        45deg,
        rgba(227, 42, 74, 0.9) 0%,
        rgba(119, 32, 85, 0.9) 54%,
        rgba(76, 28, 88, 0.9) 100%
    );
    background: -ms-linear-gradient(
        45deg,
        rgba(227, 42, 74, 0.9) 0%,
        rgba(119, 32, 85, 0.9) 54%,
        rgba(76, 28, 88, 0.9) 100%
    );
    background: linear-gradient(
        45deg,
        rgba(227, 42, 74, 0.9) 0%,
        rgba(119, 32, 85, 0.9) 54%,
        rgba(76, 28, 88, 0.9) 100%
    );
  }
  
  .cube{
    width: 30px;
    height: 30px;
    margin-right: 10px;
    background-color: rgb(235, 233, 233);
    
    &:first-child {
      animation: left 1s infinite;
    }
    &:last-child {
      animation: right 1s infinite .5s;
    }
  }

  @keyframes left {
    40% {
      transform: translateX(-60px);
    }
    50% {
      transform: translateX(0);      
    }
  }
  @keyframes right {
    40% {
      transform: translateX(60px);
    }
    50% {
      transform: translateX(0);
    }
  }
</style>