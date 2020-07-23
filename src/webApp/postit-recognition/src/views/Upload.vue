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
    <b-row id="result-row">
      <b-col>
        <h2 v-if="done" class="p-2 text-center">Your results</h2>
        <b-card
          no-body
          class="mb-1"
          v-for="(postItGroup, index) in postItGroups"
          :key="postItGroup[0]"
        >
          <b-card-header header-tag="header" class="p-1" role="tab">
            <b-button block v-b-toggle.accordion-1 variant="info"
              >Group {{ index + 1 }}</b-button
            >
          </b-card-header>
          <b-collapse
            id="accordion-1"
            visible
            accordion="my-accordion"
            role="tabpanel"
          >
            <b-card-body>
              <b-card-text>
                <b-card-group columns>
                  <b-card
                    v-for="postIt in postItGroup[1]"
                    :key="postIt.id"
                    v-bind:style="{ backgroundColor: postIt.color.color }"
                  >
                    <b-card-text class="text-center">
                      <b>{{ postIt.contents }}</b>
                    </b-card-text>
                    <template v-slot:footer>
                      <small>
                        Position: x={{ postIt.coordinates.posX }} y={{
                          postIt.coordinates.posY
                        }}
                      </small>
                    </template>
                  </b-card>
                </b-card-group>
              </b-card-text>
            </b-card-body>
          </b-collapse>
        </b-card>
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

      // presentation
      postIts: [],
      postItGroups: []
    };
  },
  methods: {
    async submitFile() {
      // Update page
      this.processing = true;
      this.title = "We are working on it...";

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
        // handle response
        .then(response => {
          response.data.forEach(obj => {
            obj.color = JSON.parse(obj.color);

            // format color property correctly
            obj.color.color = this.decodeColorToRgb(obj.color.color);
            obj.color.color_group = this.decodeColorToRgb(
              obj.color.color_group
            );
            this.postIts.push(obj);
          });

          // group post-its by color
          this.postItGroups = Array.from(
            this.groupBy(this.postIts, postIt => postIt.color.color_group)
          );
          this.title = "Your results are ready!";
          this.done = true;
        });
    },
    decodeColorToRgb(colorArray) {
      return `rgb(${colorArray[0]},${colorArray[1]},${colorArray[2]})`;
    },
    groupBy(list, keyGetter) {
      const map = new Map();
      list.forEach(item => {
        const key = keyGetter(item);
        const collection = map.get(key);
        if (!collection) {
          map.set(key, [item]);
        } else {
          collection.push(item);
        }
      });
      return map;
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

#result-row {
  padding-bottom: 2%;
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
