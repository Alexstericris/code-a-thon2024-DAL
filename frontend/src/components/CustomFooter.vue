<script setup>

</script>

<template>
  <footer></footer>
    <div class="footer">

      <a href="https://www.dal.de/de/footer/impressum">Impressum</a>
      <a href="https://www.dal.de/de/footer/datenschutz">Datenschutz</a>
      <a href="https://www.dal.de/de/footer/verschluesseln-sensibler-e-mails">IT-Sicherheit</a>
      <a href="https://www.dal.de/de/footer/hinweisgebersystem">Hinweisgebersystem</a>
      <a href="https://www.dal.de/de/footer/haftungsausschluss">Haftungsausschluss</a>
      <a> &copy; {{ year }} 2024 DAL </a>
    </div>
</template>

<style scoped>
.footer {
  background-color: var(--bright-color);
  text-align: center;
  padding: 10px;
  font-size: 12px;
  position: sticky;
  bottom: 0;
  width: 100%;
  display: flex;
  justify-content: center;
  gap: 20px;
}

.footer a {
  text-decoration: none;
  color: black;
}

.footer span {
  margin-left: auto;
  margin-right: 20px;
}
</style>