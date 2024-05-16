<script setup>
import { RouterLink, RouterView, routerKey, useRouter } from 'vue-router'
import Login from '@/components/Login.vue'

const router = useRouter()

const goLogin = function () {
  router.push({name:'Login'})
}
</script>

<template>
<div class="container">

  
  <nav class="navbar navbar-expand-lg bg-body">
    <div class="container-fluid">
      <RouterLink :to="{ name: 'MainPageView' }" class="navbar-brand fs-1">THB<span class="fs-5">ank</span>
      <img src="@/assets/images/file.png" alt="하얀고래비트고인"></RouterLink>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarText">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <RouterLink :to="{ name: 'CompareView' }" class="nav-link active">예/적금 금리비교</RouterLink>

          </li>
          <li class="nav-item">
            <RouterLink :to="{ name: 'ExchangeView' }" class="nav-link active">환율비교</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink :to="{ name: 'NearBankView' }" class="nav-link active">근처은행</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink :to="{ name: 'SuggestionView' }" class="nav-link active">상품 추천</RouterLink>
          </li>
        </ul>
        <span class="navbar-text">
          <button type="button" class="btn btn-outline-dark" @click="goLogin">로그인</button>
        </span>
      </div>
    </div>
  </nav>
</div>
  <!-- <RouterLink :to="{name: 'MainPageView'}">THB</RouterLink> |
  <RouterLink :to="{name: 'ExchangeView'}">환율비교</RouterLink>|
  <RouterLink :to="{name: 'CompareView'}">예/적금 금리비교</RouterLink> |
  <RouterLink :to="{name:'NearBankView'}">근처은행</RouterLink>|
  <RouterLink :to="{name: 'SuggestionView'}">상품 추천</RouterLink> -->
  <RouterView />

</template>

<style scoped>

</style>
