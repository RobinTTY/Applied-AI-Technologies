<template>
  <b-navbar toggleable="sm" variant="light" type="light">
    <b-navbar-brand id="brand" href="#">
      <router-link to="/">
        <img
          :src="require('../assets/Icons/icon.png')"
          width="36"
          height="36"
          alt="Post-it"
        />
        Post-it Recognition
      </router-link>
    </b-navbar-brand>
    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item :to="'/api'" :active="$route.name == 'Api'">API</b-nav-item>
        <b-nav-item :to="'/pricing'" :active="$route.name == 'Pricing'"
          >Pricing</b-nav-item
        >
        <b-nav-item :to="'/about'" :active="$route.name == 'About'"
          >About</b-nav-item
        >
      </b-navbar-nav>
    </b-collapse>
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

@media (max-width: 576px) {
  #brand {
    font-size: 1.1em;
  }
}
</style>
