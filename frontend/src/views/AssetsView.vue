<script setup>

import AssetsMap from "@/components/AssetsMap.vue";
import Card from "@/components/reuseables/Card.vue";
</script>

<template>
  <div>
    <Card :hide-footer="true" :hide-corner="true" :hide-subtitle="true">
      <template #title>
        <div style="width: 100%; text-align: center">
          Assets Karte
        </div>
      </template>
      <template #text>
        <AssetsMap></AssetsMap>
      </template>
    </Card>
  </div>
</template>

<style>
</style>