<script setup>
import { RouterLink, RouterView, routerKey, useRouter, useRoute } from 'vue-router'
import { useFinanceStore } from './stores/finance'

const store = useFinanceStore()
const route = useRoute()
const router = useRouter()

const goLogin = function () {
  router.push({name:'Login'})
}

const goSignup = function () {
  router.push({name:'Signup'})
}

const goLogout = function () {
  store.token = null
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
          <div v-if="store.token">
            <button type="button" class="btn btn-outline-dark" @click="goLogout">로그아웃</button>
          </div>
          <div v-else>
            <button type="button" class="btn btn-outline-dark" @click="goLogin">로그인</button>
            <button type="button" class="btn btn-outline-dark ms-2" @click="goSignup">회원가입</button>
          </div>
          
        </span>
      </div>
    </div>
  </nav>

  <!-- 삭제해라 -->
  <p>나중에 삭제할것</p>
  <a href="http://127.0.0.1:8000/deposit/api">예금 db 생성</a>
  <span>|</span>
  <a href="http://127.0.0.1:8000/saving/api">적금 db 생성</a>
  <!-- 삭제해라 -->
</div>
  <RouterView />

</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR&family=Jua&display=swap');
body, html {
  font-family: "IBM Plex Sans KR", sans-serif;
  font-weight: 400;
  font-style: normal;
}

</style>
