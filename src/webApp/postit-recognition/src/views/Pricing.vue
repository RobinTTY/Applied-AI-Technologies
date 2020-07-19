<template>
  <b-container id="main-content">
    <h1 class="p-3">Our pricing structure</h1>
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
              <b-list-group-item href="#"
                >20 API Calls per month</b-list-group-item
              >
              <b-list-group-item href="#"
                >Access to client libraries</b-list-group-item
              >
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
              <b-list-group-item href="#"
                >1 000 API Calls per month</b-list-group-item
              >
              <b-list-group-item href="#"
                >Access to client libraries</b-list-group-item
              >
              <b-list-group-item href="#"
                >Support from our engineers</b-list-group-item
              >
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
              <b-list-group-item href="#"
                >Discuss your needs with us</b-list-group-item
              >
              <b-list-group-item href="#"
                >Access to client libraries</b-list-group-item
              >
              <b-list-group-item href="#"
                >Support from our engineers</b-list-group-item
              >
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
  </b-container>
</template>

<script>
export default {
  data() {
    return {
      table_fields: [
        { key: "Free", sortable: false },
        { key: "Individual", sortable: false },
        { key: "Enterprise", sortable: false }
      ],
      table_items: [{ Free: "test", Individual: "test", Enterprise: "wow" }]
    };
  }
};
</script>
<style scoped>
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
