<template>
  <div id="app">
    <Navbar/>
    <Upload msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue'
import Upload from './components/Upload.vue'

export default {
  name: 'App',
  components: {
    Navbar,
    Upload,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
