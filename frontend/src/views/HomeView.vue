<script setup>
import Card from "@/components/reuseables/Card.vue";
import {faUpRightAndDownLeftFromCenter} from "@fortawesome/free-solid-svg-icons";
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";
import {useGlobalStore} from "@/stores/global.js";
import Http from "@/helpers/Http.js";
import AssetsMap from "@/components/AssetsMap.vue";

const globalStore = useGlobalStore();
globalStore.backgroundImg='wind.jpg'

Http.get('/customerportal/getcompanies').then(async response=>{
  console.log(await response.json());
})

</script>

<template>
  <main class="container" :style="{backgroundImage: 'url(/'+globalStore.backgroundImg+')'}">
    <div class="row">
      <Card :hide-footer="true">
        <template #right-corner>
          <RouterLink class="link-box" to="/contracts/1/view">
            <FontAwesomeIcon :icon="faUpRightAndDownLeftFromCenter"></FontAwesomeIcon>
          </RouterLink>
        </template>
        <template #title>My title</template>
        <template #subtitle>My subtitle</template>
        <template #text>My text</template>
        <!--      <template #footer>My my footer</template>-->
      </Card>
      <Card :hide-corner="true" :hide-footer="true">
        <template #right-corner>
          <RouterLink class="link-box" to="/contracts/view/contractId1">
            <FontAwesomeIcon :icon="faUpRightAndDownLeftFromCenter"></FontAwesomeIcon>
          </RouterLink>
        </template>
        <template #title>My title</template>
        <template #subtitle>My subtitle</template>
        <template #text>My text</template>
        <!--      <template #footer>My my footer</template>-->
      </Card>
      <Card :hide-corner="true" :hide-footer="true">
        <template #right-corner>
          <RouterLink class="link-box" to="/contracts/view/contractId2">
            <FontAwesomeIcon :icon="faUpRightAndDownLeftFromCenter"></FontAwesomeIcon>
          </RouterLink>
        </template>
        <template #title>My title</template>
        <template #subtitle>My subtitle</template>
        <template #text>My text</template>
        <!--      <template #footer>My my footer</template>-->
      </Card>
      <Card :hide-corner="true" :hide-footer="true">
        <template #right-corner>
          <RouterLink class="link-box" to="/contracts/view/contractId3">
            <FontAwesomeIcon :icon="faUpRightAndDownLeftFromCenter"></FontAwesomeIcon>
          </RouterLink>
        </template>
        <template #title>My title</template>
        <template #subtitle>My subtitle</template>
        <template #text>My text</template>
        <!--      <template #footer>My my footer</template>-->
      </Card>
    </div>
  </main>
</template>
