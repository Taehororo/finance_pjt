<template>
  <div class="bg-info-subtle d-flex align-items-center justify-content-center" style="height: 100px;">
    <h2 class="fw-bold">근처은행</h2>
  </div>
  <div id="app" class="container">
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