<script setup>

import {faDownLeftAndUpRightToCenter, faUpRightAndDownLeftFromCenter} from "@fortawesome/free-solid-svg-icons";
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";
import {useGlobalStore} from "@/stores/global.js";
import Card from "@/components/reuseables/Card.vue";

const globalStore = useGlobalStore();
globalStore.backgroundImg = 'solar.webp'
</script>

<template>
  <Card :hide-footer="true">
    <template #right-corner>
      <RouterLink class="link-box" style="background: var(--primary-red)" to="/">
          <FontAwesomeIcon :icon="faDownLeftAndUpRightToCenter"></FontAwesomeIcon>
        </RouterLink>
    </template>
    <template #title>
      Vertrag: {{ globalStore.viewContract.contractName }}
    </template>
    <template #subtitle>
        Contract leasing company: {{ globalStore.viewContract.contractLeasingCompany }}
    </template>
    <template #text>
              <div style="display: flex">
          <div style="width: 50%">
            <Card :hide-corner="true">
              <template #title>Asset:</template>
              <template #subtitle>{{globalStore.viewContract.asset.assetID}}</template>
              <template #text>
                <div>{{globalStore.viewContract.asset.assetDescription}}</div>
                <div>Strasse : {{globalStore.viewContract.asset.assetStreet}}</div>
                <div>Ort: {{globalStore.viewContract.asset.assetPLZ}} {{globalStore.viewContract.asset.assetTown}}</div>
              </template>
               <template #footer>
                <div>Status: {{ globalStore.viewContract.asset.assetStatus }}</div>
              </template>
            </Card>
          </div>
          <div style="width: 50%">
            <Card v-if="globalStore.viewContract.invoices.length>0"
                  v-for="invoice in globalStore.viewContract.invoices" :hide-corner="true">
              <template #title>Rechnung:</template>
              <template #subtitle>{{ invoice.invoiceID }}</template>
              <template #text>
                <div>Datum: {{ invoice.invoiceDate }}</div>
                <div>Summe: {{ invoice.invoiceCosts }}</div>
              </template>
              <template #footer>
                <div>Status: {{ invoice.invoiceStatus }}</div>
              </template>
            </Card>
            <Card v-else :hide-body="true" :hide-subtitle="true" :hide-corner="true" :hide-footer="true">
              <template #title>Keine Rechnungen</template>
            </Card>
          </div>
        </div>
    </template>
  </Card>
</template>

<style scoped>

</style>