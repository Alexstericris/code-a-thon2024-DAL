<script setup>

import {faDownLeftAndUpRightToCenter, faUpRightAndDownLeftFromCenter} from "@fortawesome/free-solid-svg-icons";
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";
import {useGlobalStore} from "@/stores/global.js";
import Card from "@/components/reuseables/Card.vue";

const globalStore = useGlobalStore();
globalStore.backgroundImg = 'solar.webp'
</script>

<template>
  <Card>
    <template #right-corner>
      <RouterLink class="link-box" style="background: var(--primary-red)" to="/">
        <FontAwesomeIcon :icon="faDownLeftAndUpRightToCenter"></FontAwesomeIcon>
      </RouterLink>
    </template>
    <template #title>Asset</template>
    <template #subtitle>{{ globalStore.viewAsset.assetID }}</template>
    <template #text>
      <div>{{ globalStore.viewAsset.assetDescription }}</div>
      <div>Strasse : {{ globalStore.viewAsset.assetStreet }}</div>
      <div>Ort: {{ globalStore.viewAsset.assetPLZ }} {{ globalStore.viewAsset.assetTown }}</div>
    </template>
    <template #footer>
      <div>Status: {{ globalStore.viewAsset.assetStatus }}</div>
    </template>
  </Card>
</template>

<style scoped>

</style>