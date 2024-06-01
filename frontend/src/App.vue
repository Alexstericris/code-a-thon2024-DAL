<script setup>
import {RouterLink, RouterView, useRoute} from 'vue-router'
import Navigation from '@/components/Navigation.vue'
import {computed} from "vue";

const route = useRoute();
const path = computed(() => route.path)
</script>

<template>
  <header>
    <Navigation v-if="path!=='/login'"></Navigation>
  </header>

  <RouterView/>
</template>

<style scoped>

</style>
