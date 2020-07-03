<template>
<!-- TODO: USE card group -->
  <div id="root">
    <b-container id="main-content" fluid>
      <b-row class="vh-100 p-5 text-center" align-v="center">
        <b-col class="h-50">
          <b-card class="p-4">
            <b-card-img :src="require('../assets/cloud-upload.svg')"></b-card-img>
            <b-card-text><h2>Upload a picture</h2></b-card-text>
          </b-card>
        </b-col>

        <b-col class="h-50">
          <b-card class="p-4">
            <b-card-img :src="require('../assets/camera2.svg')"></b-card-img>
            <b-card-text><h2>Take a picture</h2></b-card-text>
          </b-card>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
export default {
  props: {
    msg: String
  }
};
</script>

<style scoped>
#root {
  font-size: 1em;
}
</style>
