<script setup>

import AssetsMap from "@/components/AssetsMap.vue";
</script>

<template>
  <div class="about">
  <div style="display: flex; justify-content: center">
    <p style="font-family:'Courier New'; font-size: 30px;"><strong>Assets Karte</strong></p>
    </div>
    <div style="display: flex; justify-content: center">
    <AssetsMap></AssetsMap>
  </div>
  </div>

</template>

<style>
  .about {
    background-image: url("/wind.jpg");
    background-size: cover;
  }
</style>