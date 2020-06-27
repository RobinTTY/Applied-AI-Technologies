<template>
  <div>
    <b-container id="main-content" fluid>
      <b-row class="vh-100 text-center" align-v="center">
        <b-card-group>
          <b-card title="Upload a picture">
            <b-card-text>
              <div class="h2 mb-0">
                <b-icon-cloud-upload style="width: 360px; height: 360px;"></b-icon-cloud-upload>
              </div>
            </b-card-text>
            <template v-slot:footer>
              <small class="text-muted">More info?</small>
            </template>
          </b-card>

          <b-card title="Take a picture">
            <b-card-text>
              <div class="h2 mb-0">
                <b-icon-camera style="width: 360px; height: 360px;"></b-icon-camera>
              </div>
            </b-card-text>
            <template v-slot:footer>
              <small class="text-muted">More info?</small>
            </template>
          </b-card>
        </b-card-group>
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
#main-content {
  margin-top: 60px;
}
</style>
