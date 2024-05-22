<template>
  <div class="bg-info-subtle d-flex align-items-center justify-content-center container" style="height: 100px;">
    <h2 class="fw-bold">근처은행</h2>
  </div>
  <div id="app" class="container">
    <div class="input-group my-3">
      <input type="text" class="form-control" placeholder="주소를 입력하세요" v-model="address" @keyup.enter="searchNearbyBanks">
      <button class="btn btn-primary" @click="searchNearbyBanks">검색</button>
    </div>
    <KaKaoMap :initial-address="initialAddress" :user-address="sendaddress"/>

  </div>
</template>

<script setup>
import { ref } from 'vue'
import KaKaoMap from '@/components/KaKaoMap.vue'

// 초기 주소 설정 (역삼역)
const initialAddress = ref('서울 강남구 역삼동 837-11')

// 사용자 입력 주소
const address = ref('')
// KaKaoMap으로 보낼 주소
const sendaddress = ref('')



// 주소 검색 함수
const searchNearbyBanks = function() {
  if (address.value.trim() !== '') { // 주소가 비어있지 않을 때에만 검색
    sendaddress.value = address.value
  }
}
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