<script setup>
import {RouterLink, RouterView, useRoute, useRouter} from 'vue-router'
import Navigation from '@/components/Navigation.vue'
import {computed} from "vue";
import {useGlobalStore} from "@/stores/global.js";
import {useAuthStore} from "@/stores/auth.js";

const globalStore = useGlobalStore();
const authStore = useAuthStore();
const router = useRouter();
const route = useRoute();

if (!authStore.authUser) {
  router.push('/login')
}
const path = computed(() => route.path)
</script>

<template>
  <div id="app-background" :style="{backgroundImage: 'url(/'+globalStore.backgroundImg+')'}"></div>
  <header>
    <Navigation v-if="path!=='/login'"></Navigation>
  </header>
  <main class="container mt-80">
    <RouterView/>
  </main>
</template>

<style scoped>

</style>
