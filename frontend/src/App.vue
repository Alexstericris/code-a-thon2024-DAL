<script setup>
import {RouterLink, RouterView} from 'vue-router'
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";
import {faCog} from "@fortawesome/free-solid-svg-icons";
import Navigation from '@/components/Navigation.vue'

</script>

<template>
  <header>
    <Navigation></Navigation>
<!--    <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125"/>-->
    <div class="wrapper">
      <font-awesome-icon :icon="faCog"/>
    </div>
  </header>

  <RouterView/>
</template>

<style scoped>

</style>
