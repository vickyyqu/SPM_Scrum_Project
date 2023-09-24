<script setup>
import Navbar from './components/navbar.vue';
import RoleListingView from './views/RoleListingView.vue';
import AddRoleListingView from './views/AddRoleListingView.vue';

</script>

<!-- <template>
  <RoleListingView />
  <AddRoleListingView />
</template> -->

<template>
  <Navbar />
  <div class="m-10">
    <RouterView />
  </div>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}

.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}

.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
