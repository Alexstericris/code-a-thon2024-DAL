<script setup>

import {faDownLeftAndUpRightToCenter, faUpRightAndDownLeftFromCenter} from "@fortawesome/free-solid-svg-icons";
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";
import {useGlobalStore} from "@/stores/global.js";
const globalStore = useGlobalStore();
globalStore.backgroundImg='solar.webp'
</script>

<template>
  <main class="container" :style="{backgroundImage: 'url(/'+globalStore.backgroundImg+')'}">
    <div class="card">
      <div class="card-header">
        <div class="card-title">
          <div>
            Title
          </div>
          <RouterLink class="link-box" to="/">
            <FontAwesomeIcon :icon="faDownLeftAndUpRightToCenter"></FontAwesomeIcon>
          </RouterLink>
        </div>
        <div class="card-body">
          Test
        </div>
      </div>
    </div>
  </main>
</template>

<style scoped>

</style>