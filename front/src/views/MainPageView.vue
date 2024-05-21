<template>
  <div>
    <!-- First Section -->
    <div class="row h-100 bg-gradient-primary">
      <div class="col-md-7 d-flex align-items-center justify-content-center">
        <div class="text-container">
          <h2 class="text-white">예금 적금을 알아볼까요?</h2>
          <button type="button" class="btn btn-primary btn-lg mt-3" @click="goCompare">비교하러가기</button>
        </div>
      </div>
      <div class="col-md-5 d-flex align-items-center justify-content-center">
        <img src="@/assets/images/tatemono_bank_money.png" class="img-fluid" alt="Sample Image">
      </div>
    </div>

    <!-- Second Section -->
    <div class="row h-100 bg-gradient-secondary mt-3">
      <div class="col-md-5 d-flex align-items-center justify-content-center order-md-last">
        <img src="@/assets/images/airplane1_red.png" class="img-fluid" alt="Sample Image">
      </div>
      <div class="col-md-7 d-flex align-items-center justify-content-center">
        <div class="text-container">
          <h2 class="text-white">환율을 확인해볼까요?</h2>
          <button type="button" class="btn btn-primary btn-lg mt-3" @click="goExchange">환율 보러가기</button>
        </div>
      </div>
    </div>

    <!-- Third Section -->
    <div class="row h-100 bg-gradient-tertiary mt-3">
      <div class="col-md-7 d-flex align-items-center justify-content-center">
        <div class="text-container">
          <h2 class="text-white">AI추천을 받아볼래요?</h2>
          <button type="button" class="btn btn-primary btn-lg mt-3" @click="goSuggestion">상품 추천받으러 가기</button>
        </div>
      </div>
      <div class="col-md-5 d-flex align-items-center justify-content-center">
        <img src="@/assets/images/ai_talk_ai.png" class="img-fluid" alt="Sample Image">
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()

const goCompare = () => {
  router.push({ name: 'CompareView' })
}

const goExchange = () => {
  router.push({ name: 'ExchangeView' })
}

const goSuggestion = () => {
  router.push({ name: 'SuggestionView' })
}
</script>

<style scoped>
/* Container for text content */
.text-container {
  text-align: center;
}

/* Button hover effect */
.btn-primary:hover {
  background-color: #4c6ef5;
}

/* Adjust image height */
.img-fluid {
  max-height: 80%;
}

/* Gradient backgrounds */
.bg-gradient-primary {
  background: linear-gradient(45deg, #64b5f6, #1976d2);
}

.bg-gradient-secondary {
  background: linear-gradient(45deg, #81c784, #388e3c);
}

.bg-gradient-tertiary {
  background: linear-gradient(45deg, #ffb74d, #f57c00);
}
</style>