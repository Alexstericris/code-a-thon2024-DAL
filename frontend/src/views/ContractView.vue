<script setup>

import {faDownLeftAndUpRightToCenter, faUpRightAndDownLeftFromCenter} from "@fortawesome/free-solid-svg-icons";
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";
import {useGlobalStore} from "@/stores/global.js";

const globalStore = useGlobalStore();
globalStore.backgroundImg = 'solar.webp'
</script>

<template>
  <div class="card">
    <div class="card-header">
      <div class="card-title">
        <div>
          Vertrag {{ globalStore.viewContract.contractName }}
        </div>
        <RouterLink class="link-box" to="/">
          <FontAwesomeIcon :icon="faDownLeftAndUpRightToCenter"></FontAwesomeIcon>
        </RouterLink>
      </div>
      <div class="card-body">
        Contract leasing company {{ globalStore.viewContract.contractLeasingCompany }}
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>