<template>
  <b-navbar variant="light" type="light">
    <b-navbar-brand href="#">
      <router-link to="/">
        <img
          :src="require('../assets/Icons/post-it.png')"
          width="36"
          height="36"
          alt="Post-it"
        />
        Post-it Recognition
      </router-link>
    </b-navbar-brand>
  </b-navbar>
</template>

<script>
export default {};
</script>

<style scoped>
a {
  text-decoration: none !important;
  color: black !important;
}
</style>
