<template>
  <b-container fluid id="main-content">
    <b-row class="justify-content-md-center">
      <b-col>
        <h1 class="pt-3 text-center">Digitalize your Post-it notes today!</h1>
        <b-img
          fluid-grow
          id="picture-main"
          :src="require('../assets/Illustrations/Search.svg')"
        >
        </b-img>
      </b-col>
    </b-row>

    <b-row id="buttons-container" class="p-5 text-center" align-v="center">
      <b-container>
        <b-row>
          <b-col id="upload-col" md="6" sm="12">
            <router-link to="/upload">
              <b-card class="shadow-lg card-container">
                <b-card-img
                  :src="require('../assets/Icons/cloud-upload.svg')"
                  class="picture p-3"
                ></b-card-img>
                <b-card-text>
                  <h2>Upload a picture</h2>
                </b-card-text>
              </b-card>
            </router-link>
          </b-col>

          <b-col id="camera-col" md="6" sm="12">
            <b-card class="shadow-lg card-container">
              <b-card-img
                :src="require('../assets/Icons/camera.svg')"
                class="picture p-3"
              ></b-card-img>
              <b-card-text>
                <h2>Take a picture</h2>
              </b-card-text>
            </b-card>
          </b-col>
        </b-row>
      </b-container>
    </b-row>
  </b-container>
</template>

<script>
export default {
  name: "Home",
  props: {
    msg: String
  },
  mounted() {
    let recaptchaScript = document.createElement("script");
    recaptchaScript.setAttribute(
      "src",
      "https://editor.swagger.io/dist/swagger-editor-bundle.js"
    );
    document.head.appendChild(recaptchaScript);
  }
};
</script>

<style scoped>
a {
  text-decoration: none !important;
  color: black !important;
}

.picture {
  max-width: 300px;
}

.card-container {
  background: rgb(209, 230, 255);
  background: radial-gradient(
    circle,
    rgba(209, 230, 255, 1) 57%,
    rgba(255, 205, 234, 1) 100%
  );
}

#root {
  font-size: 1em;
}

#picture-main {
  padding: 0 10%;
  max-height: 600px;
}

@media (max-width: 768px) {
  h1 {
    font-size: 2em;
  }

  #camera-col {
    padding-top: 3%;
  }
}

@media (max-width: 576px) {
  h1 {
    font-size: 1.5em;
  }
}
</style>
