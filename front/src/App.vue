<script setup>
import { RouterLink, RouterView } from 'vue-router'
import KaKaoMap from '@/components/KaKaoMap.vue'
</script>

<template>
  <header>

  </header>
  <!-- <div id="app">
    <KaKaoMap />
  </div> -->
  <RouterLink :to="{name: 'MainPageView'}">THB</RouterLink> |
  <RouterLink :to="{name: 'ExchangeView'}">환율비교</RouterLink>|
  <RouterLink :to="{name: 'CompareView'}">예/적금 금리비교</RouterLink> |
  <RouterLink :to="{name:'NearBankView'}">근처은행</RouterLink>|
  <RouterLink :to="{name: 'SuggestionView'}">상품 추천</RouterLink>
  <RouterView />

</template>

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
