<script setup>
import {ref} from "vue";
import {RouterLink, useRouter} from "vue-router";
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";
import {faMailBulk, faRightToBracket,faRightFromBracket} from "@fortawesome/free-solid-svg-icons";
import {useAuthStore} from "@/stores/auth.js";
const authStore=useAuthStore()
const router = useRouter();

// Datenquelle für E-Mails
const emails = ref([
  { subject: 'Das ist keine Fake Nachricht', body: 'This is Fine 🐶', read: false },
  { subject: 'Vertragsbestätigung E-Mail 2', body: 'Hiermit übersende ich ihnen eine Kopie des Vertrags', read: true },
  { subject: 'Unterbreitung der Vertragskondizionen', body: 'Hiermit übersende ich ihnen die Vertrakskondizonen zur Förderung des Besprochenen projekts', read: true },
  { subject: 'Willkommen auf der Homepage der DAL', body: 'Wir freuen uns das sie ein Konnte bei der DAL angelegt habenw', read: false },
  // Weitere E-Mails hier hinzufügen...
]);

function logout() {
  console.log('t')
  authStore.authUser = null
  console.log('t2')
  localStorage.removeItem('companyID')
  console.log('t3')
  router.push('login')
}

function toggleCard() {
  var card = document.getElementById('card');
  if (card.style.display === 'none' || card.style.display === '') {
    card.style.display = 'block';
    console.log(1)
  } else {
    card.style.display = 'none';
    console.log(1)
  }
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
      <div v-if="authStore.authUser" @click="toggleCard()">
          <font-awesome-icon class="navtab" :icon="faMailBulk"/>
      </div>
      <RouterLink v-if="!authStore.authUser" to="/login">
        <font-awesome-icon class="navtab" :icon="faRightToBracket"/>
      </RouterLink>
      <div v-if="authStore.authUser" @click="logout()">
        <font-awesome-icon class="navtab" :icon="faRightFromBracket"/>
      </div>
    </div>
    <div class="mail-holder" id="card">
      <div class="card-header">
        <h1>Benachrichtigungen</h1>
      </div>
      <div v-for="(email, index) in emails" :key="index" class="mail-card" :class="{ 'unread': !email.read }">
        <!-- Wenn die E-Mail ungelesen ist, wird der Text fett angezeigt -->
        <h2 :style="{ fontWeight: email.read ? 'normal' : 'bold' }">{{ email.subject }}</h2>
        <p>{{ email.body }}</p>
      </div>
    </div>
  </nav>
</template>

<style scoped>
.mail-holder {
  background-color: var(--bright-color);
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 1);
  max-width: 400px;
  width: 100%;
  padding: 20px;
  box-sizing: border-box;
  display: none; /* Karte standardmäßig verstecken */
  position: fixed;
  top: 5%;
  right: 4.5%;
  font-size: 15px;
  max-height: 50%;
  overflow: auto;

}

.mail-card {
  background-color: var(--bright-color);
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
  max-width: 100%;
  width: 100%;
  padding: 20px;
  box-sizing: border-box;
  margin-bottom: 20px; /* Abstand zwischen den Karten */
}

.unread h2 {
  font-weight: bold; /* Text fett anzeigen, wenn die E-Mail ungelesen ist */
  width : 300px;
  overflow:hidden;
  display:inline-block;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.mail-card h2,
.mail-card p {
  max-width: 300px; /* Maximal zulässige Breite */
  overflow: hidden; /* Overflow verstecken */
  white-space: nowrap; /* Kein Umbruch von Text */
  text-overflow: ellipsis; /* Text mit Ellipsen (...) anzeigen, wenn er abgeschnitten wird */
}
</style>