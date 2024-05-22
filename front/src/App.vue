<script setup>
import { RouterLink, RouterView, useRouter, useRoute } from 'vue-router'
import { useFinanceStore } from './stores/finance'
import { ref, onMounted } from 'vue'

// 상태 관리와 라우터 관련 설정
const store = useFinanceStore()
const router = useRouter()

// 화면 깜빡임 효과를 위한 상태 변수
const isScreenBlinking = ref(false)

// 로그인 페이지로 이동하는 함수
const goLogin = function () {
  router.push({ name: 'Login' })
}

// 회원가입 페이지로 이동하는 함수
const goSignup = function () {
  router.push({ name: 'Signup' })
}

// 로그아웃 함수
// 화면 깜빡임 효과를 주고, 토큰을 제거한 후 메인 페이지로 리디렉션
const goLogout = function () {
  isScreenBlinking.value = true
  store.token = null
  store.userInfo = null
  store.userId = null
  setTimeout(() => {
    router.replace({ name: 'MainPageView' })
    isScreenBlinking.value = false
  }, 500)
}

// 프로필 페이지로 이동하는 함수
// 로그인된 사용자의 ID를 사용하여 프로필 페이지로 이동
const goProfile = function () {
  router.push({ name: 'Profile', params: { 'userid': store.userId } })
}

// 게시판 페이지로 이동하는 함수
// 로그인 상태를 확인하고 로그인되어 있지 않다면 경고 창을 표시
const goArticles = function () {
  if (store.token) {
    router.push({ name: 'articles' })
  } else {
    if (confirm('로그인 사용자만 이용할 수 있습니다. 로그인하겠습니까?')) {
      goLogin()
    }
  }
}



</script>

<template>
  <!-- 화면 깜빡임 효과를 적용할 div -->
  <div :class="{ 'screen-blink': isScreenBlinking }" class="container">
    <nav class="navbar navbar-expand-lg bg-body">
      <div class="container-fluid">
        <!-- 메인 페이지 링크 및 로고 -->
        <RouterLink :to="{ name: 'MainPageView' }" class="navbar-brand fs-1">THB<span class="fs-5">ank</span>
          <img src="@/assets/images/file.png" alt="하얀고래비트고인">
        </RouterLink>
        <!-- 반응형 메뉴 버튼 -->
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText"
          aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <!-- 네비게이션 링크들 -->
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
            <li class="nav-item">
              <a @click="goArticles" class="nav-link active" style="cursor: pointer;">게시판</a>
            </li>
          </ul>
          <!-- 로그인 상태에 따른 버튼 표시 -->
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
        <div>
              <a href="http://127.0.0.1:8000/deposit/api">예금저장</a> |
              <a href="http://127.0.0.1:8000/saving/api">적금저장</a>
        </div>
  </div>

  <!-- 화면 깜빡임 효과를 적용할 RouterView -->
  <RouterView :class="{ 'screen-blink': isScreenBlinking }" />
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
}
</style>