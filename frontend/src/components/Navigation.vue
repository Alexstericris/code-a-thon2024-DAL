<script setup>
import {ref} from "vue";
import {RouterLink, useRouter} from "vue-router";
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";
import {faMailBulk, faRightToBracket,faRightFromBracket} from "@fortawesome/free-solid-svg-icons";
import {useAuthStore} from "@/stores/auth.js";
const authStore=useAuthStore()
const router = useRouter();
function logout() {
  console.log('t')
  authStore.authUser = null
  console.log('t2')
  localStorage.removeItem('companyID')
  console.log('t3')
  router.push('login')
}

</script>

<template>
  <nav class="navbar">
    <div class="navtab-group">
      <RouterLink to="/">
        <img alt="DAL" class="logo" src="@/assets/Logo_DAL_RGB.svg"/>
      </RouterLink>
      <RouterLink class="navtab" to="/">Verträge</RouterLink>
      <RouterLink class="navtab" to="/invoices">Rechnungen</RouterLink>
      <RouterLink class="navtab" to="/assets">Assets</RouterLink>
    </div>
    <div class="navtab-group">
      <RouterLink to="/mails">
        <font-awesome-icon class="navtab" :icon="faMailBulk"/>
      </RouterLink>
      <RouterLink v-if="!authStore.authUser" to="/login">
        <font-awesome-icon class="navtab" :icon="faRightToBracket"/>
      </RouterLink>
       <div v-if="authStore.authUser" @click="logout()">
        <font-awesome-icon class="navtab" :icon="faRightFromBracket"/>
      </div>

    </div>
  </nav>
</template>

<style scoped>

</style>