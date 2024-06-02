<script setup>
import Card from "@/components/reuseables/Card.vue";
import {faUpRightAndDownLeftFromCenter} from "@fortawesome/free-solid-svg-icons";
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";
import {useGlobalStore} from "@/stores/global.js";
import Http from "@/helpers/Http.js";
import {useAuthStore} from "@/stores/auth.js";
import {ref} from "vue";
import {useRouter} from "vue-router";

const globalStore = useGlobalStore();
const authStore = useAuthStore();
const router = useRouter();
globalStore.backgroundImg = 'wind.jpg'
const contracts = ref([])
if (contracts.value.length <= 0) {
  fetchContracts();
}

function fetchContracts() {
  Http.get('/customerportal/getcontracts', {companyID: authStore.authUser}).then(async response => {
    contracts.value = await response.json()
  });
}

function onExpand(contract) {
  globalStore.viewContract = contract
  router.push('/contracts/' + contract.contractName + '/view')
}

function onExpandAsset(contract) {
  globalStore.viewContract = contract
  router.push('/contracts/' + contract.contractName + '/view')
}

function onExpandInvoice(contract) {
  globalStore.viewContract = contract
  router.push('/contracts/' + contract.contractName + '/view')
}

</script>

<template>
  <div class="row" style="justify-content: space-around">
    <Card v-for="contract in contracts" :hide-footer="true">
      <template #right-corner>
        <FontAwesomeIcon @click="onExpand(contract)" class="link-box"
                         :icon="faUpRightAndDownLeftFromCenter"></FontAwesomeIcon>

      </template>
      <template #title>Vertrag {{ contract.contractName }}</template>
      <template #subtitle>Begonnen am: {{ contract.contractStart }}</template>
      <template #text>
        <div class="mb-10">
          Contract leasing company: {{ contract.contractLeasingCompany }}
        </div>
        <div style="display: flex">
          <div style="width: 50%">
            <Card>
              <template #right-corner>
                <FontAwesomeIcon @click="onExpandAsset(contract.asset)" class="link-box"
                                 :icon="faUpRightAndDownLeftFromCenter"></FontAwesomeIcon>
              </template>
              <template #title>Asset:</template>
              <template #subtitle>{{contract.asset.assetID}}</template>
              <template #text>
                <div>{{contract.asset.assetDescription}}</div>
                <div>Strasse : {{contract.asset.assetStreet}}</div>
                <div>Ort: {{contract.asset.assetPLZ}} {{contract.asset.assetTown}}</div>
              </template>
               <template #footer>
                <div>Status: {{ contract.asset.assetStatus }}</div>
              </template>
            </Card>
          </div>
          <div style="width: 50%">
            <Card v-if="contract.invoices.length>0">
              <template #right-corner>
                <FontAwesomeIcon @click="onExpandInvoice(contract.invoices.at(-1))" class="link-box"
                                 :icon="faUpRightAndDownLeftFromCenter"></FontAwesomeIcon>
              </template>
              <template #title>Rechnung:</template>
              <template #subtitle>{{ contract.invoices.at(-1).invoiceID }}</template>
              <template #text>
                <div>Datum: {{ contract.invoices.at(-1).invoiceDate }}</div>
                <div>Summe: {{ contract.invoices.at(-1).invoiceCosts }}</div>
              </template>
              <template #footer>
                <div>Status: {{ contract.invoices.at(-1).invoiceStatus }}</div>
              </template>
            </Card>
            <Card v-else :hide-body="true" :hide-subtitle="true" :hide-corner="true" :hide-footer="true">
              <template #title>Keine Rechnungen</template>
            </Card>
          </div>
        </div>
      </template>
      <!--      <template #footer>My my footer</template>-->
    </Card>
  </div>
</template>
