<script setup>
import Card from "@/components/reuseables/Card.vue";
import {faUpRightAndDownLeftFromCenter} from "@fortawesome/free-solid-svg-icons";
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";
import {ref} from "vue";

const rechnungen = ref([1, 2, 3, 4, 5, 6, 7, 8, 9])

</script>
<template>
  <div>
    <Card v-for="rechnung in rechnungen" :hide-corner="true">
      <template #title>Rechnung: {{ rechnung }}</template>
      <template #subtitle>Rechnungsnummer: {{ rechnung }}ABCDEF</template>
      <template #text>Kosten:</template>
      <template #footer>Status:bezahlt</template>

    </Card>
  </div>
</template>

<style>
</style>
