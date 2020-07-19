<template>
  <b-container id="main-content">
    <b-row>
      <b-col>
        <h1 class="p-3" style="text-align: center">{{ title }}</h1>
        <img
          v-if="!processing"
          id="picture"
          :src="require('../assets/Illustrations/Upload.svg')"
          alt="Upload"
        />
        <lottie
          v-if="processing"
          :options="defaultOptions"
          :height="600"
          :width="900"
        />
      </b-col>
    </b-row>
    <b-row id="file-upload" class="p-4">
      <b-col class="p-0" cols="10">
        <div class="custom-file" align-v="center">
          <b-form-file
            v-model="file"
            :state="Boolean(file)"
            placeholder="Choose a file or drop it here..."
            drop-placeholder="Drop file here..."
          ></b-form-file>
        </div>
      </b-col>
      <b-col class="pl-1" cols="2">
        <b-button v-on:click="submitFile()" id="submit">Submit</b-button>
      </b-col>
    </b-row>
    <b-row>
      <b-col>
        <h2 v-if="done">Your results</h2>
        <b-card-group deck>
          <b-card v-for="postIt in postIts" :key="postIt.id">
            <b-card-text>{{ postIt.contents }}</b-card-text>
            <template v-slot:footer>
              <small class="text-muted"
                >Position: x={{ postIt.coordinates.posX }} y={{
                  postIt.coordinates.posY
                }}
              </small>
            </template>
          </b-card>
        </b-card-group>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import Lottie from "vue-lottie";
import * as animationData from "../assets/lottie/discovery.json";

export default {
  components: {
    lottie: Lottie
  },
  data() {
    return {
      // general
      processing: false,
      done: false,
      title: "Upload your picture",

      // lottie
      defaultOptions: { animationData: animationData.default },
      animationSpeed: 1,
      anim: null,

      // file upload
      file: null,
      baseServerUrl: "http://localhost:8090/RobinTTYTeam/AppliedAI/1.0.0",
      postIts: []
    };
  },
  methods: {
    async submitFile() {
      // Update page
      this.processing = true;
      this.title = "We are working on it...";
      console.log(this.file);

      // send post request
      let formData = new FormData();
      formData.append("file", this.file);
      this.$http
        .post(this.baseServerUrl + "/indexPostIts", this.file, {
          params: {
            pictureLink: this.file.name
          },
          headers: {
            "Content-Type": "image/png"
          }
        })
        .then(response => {
          //console.log(response);
          console.log(response.data);
          response.data.forEach(obj => this.postIts.push(obj));
          this.title = "Your results are ready!";
          this.done = true;
        });
    }
  }
};
</script>

<style scoped>
#file-upload {
  font-size: 1.5em;
}

#submit {
  font-size: 1em;
}

#picture {
  max-width: 100%;
}

#results {
  font-size: 20pt;
}

@media (max-width: 768px) {
  #file-upload {
    font-size: 1.2em;
  }
}

@media (max-width: 576px) {
  #file-upload {
    font-size: 1em;
  }
}
</style>
