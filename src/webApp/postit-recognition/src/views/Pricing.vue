<template>
  <b-container id="main-content">
    <h1 class="p-3 text-center">Our pricing structure</h1>
    <b-row class="justify-content-center">
      <b-card-group id="test">
        <b-card>
          <template v-slot:header>
            <h3 class="tier-header">Free</h3>
            <p>
              <b class="tier-sub-header">Basics for teams and developers</b>
            </p>
          </template>
          <b-card-text>
            <b-list-group>
              <b-list-group-item>20 API Calls per month</b-list-group-item>
              <b-list-group-item>Access to client libraries</b-list-group-item>
            </b-list-group>
          </b-card-text>
          <template v-slot:footer>
            <div class="text-center">
              <p><b>$0 /month</b></p>
              <b-button variant="primary" class="buy-btn">Choose Free</b-button>
            </div>
          </template>
        </b-card>
        <b-card>
          <template v-slot:header>
            <h3 class="tier-header">Individual</h3>
            <p>
              <b class="tier-sub-header">More flexibility for advanced users</b>
            </p>
          </template>
          <b-card-text>
            <b-list-group>
              <b-list-group-item>1 000 API Calls per month</b-list-group-item>
              <b-list-group-item>Access to client libraries</b-list-group-item>
              <b-list-group-item>Support from our engineers</b-list-group-item>
            </b-list-group>
          </b-card-text>
          <template v-slot:footer>
            <div class="text-center">
              <p><b>$9 /month</b></p>
              <b-button variant="primary" class="buy-btn"
                >Choose Individual</b-button
              >
            </div>
          </template>
        </b-card>
        <b-card>
          <template v-slot:header>
            <h3 class="tier-header">Personalized</h3>
            <p>
              <b class="tier-sub-header"
                >Personalized solution for your needs</b
              >
            </p>
          </template>
          <b-card-text>
            <b-list-group>
              <b-list-group-item>Discuss your needs with us</b-list-group-item>
              <b-list-group-item>Access to client libraries</b-list-group-item>
              <b-list-group-item>Support from our engineers</b-list-group-item>
            </b-list-group>
          </b-card-text>
          <template v-slot:footer>
            <div class="text-center">
              <p><b>Individual price</b></p>
              <b-button variant="primary" class="buy-btn"
                >Contact Sales</b-button
              >
            </div>
          </template>
        </b-card>
      </b-card-group>
    </b-row>
    <b-row>
      <b-col>
        <b-container>
          <h1 id="client-libs" class="text-center">Our client libraries</h1>
          <div class="text-center">
            <img
              :src="require('../assets/Icons/icons8-java.svg')"
              width="128"
              height="128"
              alt="Post-it"
            />
            <img
              :src="require('../assets/Icons/icons8-c-sharp-logo.svg')"
              width="128"
              height="128"
              alt="Post-it"
            />
            <img
              :src="require('../assets/Icons/icons8-python.svg')"
              width="128"
              height="128"
              alt="Post-it"
            />
            <img
              :src="require('../assets/Icons/icons8-swift.svg')"
              width="128"
              height="128"
              alt="Post-it"
            />
            <img
              :src="require('../assets/Icons/icons8-kotlin.svg')"
              width="128"
              height="128"
              alt="Post-it"
            />
            <img
              :src="require('../assets/Icons/icons8-php-logo.svg')"
              width="128"
              height="128"
              alt="Post-it"
            />
            <img
              :src="require('../assets/Icons/icons8-typescript.svg')"
              width="128"
              height="128"
              alt="Post-it"
            />
          </div>
          <div class="text-center p-3">
            <b-button
              href="https://github.com/RobinTTY/Applied-AI-Technologies/tree/TeamB%40aai2020/clients"
              target="_blank"
              rel="noopener noreferrer"
              variant="primary"
              >Download via Github</b-button
            >
          </div>
        </b-container>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
export default {};
</script>
<style scoped>
#client-libs {
  padding-top: 5%;
}

#test {
  width: 90%;
}

#main-content {
  padding-top: 3%;
}

#table {
  background: white;
}

@media (max-width: 1200px) {
  .tier-sub-header {
    font-size: 1.1em;
  }
}

@media (max-width: 992px) {
  .tier-sub-header {
    font-size: 1em;
  }
}

@media (max-width: 768px) {
  .tier-header {
    font-size: 1.3em;
  }

  .buy-btn {
    font-size: 0.7em;
  }
}

@media (max-width: 576px) {
  .tier-header {
    font-size: 1.8em;
  }

  .buy-btn {
    font-size: 1em;
  }
}
</style>
