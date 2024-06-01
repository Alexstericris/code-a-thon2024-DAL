<script setup>
import {ref} from "vue";
import {RouterLink} from "vue-router";
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";
import {faMailBulk, faRightToBracket} from "@fortawesome/free-solid-svg-icons";

</script>

<template>
  <nav class="navbar">
    <div class="navtab-group">
      <RouterLink to="/">
        <img alt="DAL" class="logo" src="@/assets/Logo_DAL_RGB.svg"/>
      </RouterLink>
      <RouterLink class="navtab" to="/">Home</RouterLink>
      <RouterLink class="navtab" to="/about">About</RouterLink>
      <RouterLink class="navtab" to="/assets">Assets</RouterLink>
    </div>
    <div class="navtab-group">
      <RouterLink to="/mails">
        <font-awesome-icon class="navtab" :icon="faMailBulk"/>
      </RouterLink>
      <RouterLink to="/login">
        <font-awesome-icon class="navtab" :icon="faRightToBracket"/>
      </RouterLink>

    </div>
  </nav>
</template>

<style scoped>

</style>