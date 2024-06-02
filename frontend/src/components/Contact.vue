<script setup>
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { faAddressBook } from "@fortawesome/free-solid-svg-icons";

function toggleCard() {
  var card = document.getElementById('card');
  if (card.style.display === 'none' || card.style.display === '') {
    card.style.display = 'block';
  } else {
    card.style.display = 'none';
  }
}
</script>

<template>
  <div class="body">
    <button @click="toggleCard" class="icon-button">
      <font-awesome-icon class="button" :icon="faAddressBook" />
    </button>
  </div>
  <div class="card" id="card">
    <div class="card-header">
      <h1>Kontakt Person</h1>
    </div>
    <div class="card-content">
      <p>Name: Max Mustermann</p>
      <p>Telefon: 0123 456789</p>
      <p>Email: max.mustermann@example.com</p>
      <p>Stadt: Musterstadt</p>
      <p>Ort: 12345</p>
      <p>Straße: Musterstraße</p>
      <p>Hausnummer: 1</p>
      <!-- Weitere Zeilen können hier hinzugefügt werden -->
    </div>
  </div>
</template>

<style scoped>
.icon-button {
  position: fixed;
  bottom: 48px;
  right: 20px;
  width: 50px;
  height: 50px;
  font-size: 30px;
  background-color: red;
  color: var(--bright-color);
  border: none;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  cursor: pointer;
}

.icon-button img {
  width: 45px;
  height: 45px;
}

.icon-button:hover {
  background-color: var(--bright-color);
  color: black;
}

.icon-button:active {
  background-color: var(--bright-color);
  color: black;
}

.card {
  background-color: var(--bright-color);
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  max-width: 400px;
  width: 100%;
  padding: 20px;
  box-sizing: border-box;
  display: none; /* Karte standardmäßig verstecken */
  position: fixed;
  bottom: 9%;
  right: 3%;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.card-header h1 {
  font-size: 24px;
  margin: 0;
}

.card-content p {
  margin: 5px 0;
  font-size: 16px;
}
</style>
