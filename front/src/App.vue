<script setup>
import { RouterLink, RouterView, useRouter, useRoute } from 'vue-router'
import { useFinanceStore } from './stores/finance'
import { ref } from 'vue'

const store = useFinanceStore()
const route = useRoute()
const router = useRouter()

const isScreenBlinking = ref(false)

const goLogin = function () {
  router.push({ name: 'Login' })
}

const goSignup = function () {
  router.push({ name: 'Signup' })
}

const goLogout = function () {
  isScreenBlinking.value = true
  store.token = null
  setTimeout(() => {
    router.replace({ name: 'MainPageView' })
    isScreenBlinking.value = false
  }, 500)
}

const goProfile = function () {
  router.push({ name: 'Profile', params: { 'userid': store.userId } })
}
</script>

<template>
  <div :class="{ 'screen-blink': isScreenBlinking }" class="container">
    <nav class="navbar navbar-expand-lg bg-body">
      <div class="container-fluid">
        <RouterLink :to="{ name: 'MainPageView' }" class="navbar-brand fs-1">THB<span class="fs-5">ank</span>
          <img src="@/assets/images/file.png" alt="하얀고래비트고인">
        </RouterLink>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText"
          aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
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
            <!-- 로그인 되어있을때 -->
            <div v-if="store.token">
              <button type="button" class="btn btn-outline-dark" @click="goProfile">나의 정보</button>
              <button type="button" class="btn btn-outline-dark ms-2" @click="goLogout">로그아웃</button>
            </div>
            <!-- 로그인 안되어있을때 -->
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
  <RouterView :class="{ 'screen-blink': isScreenBlinking }"/>
  </template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR&family=Jua&display=swap');

body,
html {
  font-family: "IBM Plex Sans KR", sans-serif;
  font-weight: 400;
  font-style: normal;
}

@keyframes screen-blink {
  0% {
    opacity: 1;
  }

  50% {
    opacity: 0;
  }

  100% {
    opacity: 1;
  }
}

.screen-blink {
  animation: screen-blink 0.5s ease-in-out;
}</style>