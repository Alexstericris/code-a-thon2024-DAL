<script setup>
import {ref} from "vue";
import {RouterLink} from "vue-router";

</script>

<template>
  <nav class="navbar">
    <RouterLink to="/">
          <img alt="DAL" class="logo" src="@/assets/Logo_DAL_RGB.svg"/>
    </RouterLink>

    <RouterLink to="/">Home</RouterLink>
    <RouterLink to="/about">About</RouterLink>
    <RouterLink to="/assets">Assets</RouterLink>
  </nav>
</template>

<style scoped>

</style>