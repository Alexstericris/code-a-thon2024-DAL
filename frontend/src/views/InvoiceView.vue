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
    <template #title>Rechnung:</template>
    <template #subtitle>{{ globalStore.viewInvoice.invoiceID }}</template>
    <template #text>
      <div>Datum: {{ globalStore.viewInvoice.invoiceDate }}</div>
      <div>Summe: {{ globalStore.viewInvoice.invoiceCosts }}</div>
    </template>
    <template #footer>
      <div>Status: {{ globalStore.viewInvoice.invoiceStatus }}</div>
    </template>
  </Card>
</template>

<style scoped>

</style>