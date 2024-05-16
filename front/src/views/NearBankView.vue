<template>
  <div id="app" class="container">
    <h1>근처은행</h1>
    <KaKaoMap />
  </div>
</template>

<script setup>
import KaKaoMap from '@/components/KaKaoMap.vue'
</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>