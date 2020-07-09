<template>
  <b-container id="main-content">
    <b-row>
      <b-col>
        <h1 class="p-3" style="text-align: center">Upload your picture</h1>
        <img id="picture" :src="require('../assets/Illustrations/Upload.svg')" alt="Upload" />
      </b-col>
    </b-row>
    <b-row class="p-3">
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
        <b-button v-on:click="submitFile()">Submit</b-button>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
export default {
  data() {
    return {
      file: null
    };
  },
  methods: {
    submitFile() {
      let formData = new FormData();
      formData.append("file", this.file);
      this.$http.get("https://api.github.com/users/mapbox").then(response => {
        console.log(response.data);
        console.log(response.status);
        console.log(response.statusText);
        console.log(response.headers);
        console.log(response.config);
      });
    }
  }
};
</script>

<style scoped>
#picture {
  max-width: 100%;
}
</style>
