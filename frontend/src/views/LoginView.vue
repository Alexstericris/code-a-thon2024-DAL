<script setup>

import Http from "@/helpers/Http.js";
import {ref} from "vue";
import {useAuthStore} from "@/stores/auth.js";
import {useRouter} from "vue-router";

const authStore = useAuthStore();
const email = ref('')

const router = useRouter();

function login() {
  Http.post('/customerportal/authcompany', {companyEmail: email.value}).then(async response => {
    let user = await response.json()
    console.log(user)
    authStore.authUser = user.companyID
    localStorage.setItem('companyID', user.companyID)
    router.push('/');
  })
}
</script>

<template>
  <div class="box-container">
    <div class="box">
      <div class="box-inner">
        <img alt="DAL" src="@/assets/Logo_DAL_RGB.svg"/>
        <form @submit.prevent="login()">
          <div class="input-container">
            <input v-model="email" name="email" class="mb-10" type="text" placeholder="Email" required>
          </div>
          <div class="input-container">
            <input v-model="passwort" name="password" class="mb-10" type="text" placeholder="Passwort" required>
          </div>
          <div style="display: flex; justify-content: space-between;">
            <button class="btn-primary">Sign in</button>
            <button class="btn-primary">Login</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<style>
.btn-primary{
  width: 40%;
}

.input-container {
  margin-bottom: 10px;
}
</style>