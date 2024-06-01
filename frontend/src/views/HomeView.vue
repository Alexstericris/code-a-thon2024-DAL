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
  console
  router.push('/contracts/' + contract.contractName + '/view')
}

</script>

<template>
  <div class="row">
    <Card v-for="contract in contracts" :hide-footer="true">
      <template #right-corner>
        <FontAwesomeIcon @click="onExpand(contract)" class="link-box"
                         :icon="faUpRightAndDownLeftFromCenter"></FontAwesomeIcon>

      </template>
      <template #title>Vertrag {{ contract.contractName }}</template>
      <template #subtitle>Begonnen am: {{ contract.contractStart }}</template>
      <template #text>Contract leasing company {{ contract.contractLeasingCompany }}</template>
      <!--      <template #footer>My my footer</template>-->
    </Card>
  </div>
</template>
