<template>
  <div class="bg-info-subtle d-flex align-items-center justify-content-center" style="height: 100px;">
    <h2 class="fw-bold">환율 변환기</h2>
  </div>

  <div class="container mt-5 d-flex flex-column align-items-center">
    <div class="mb-3">
      <label for="fromCurrency" class="form-label text-info fw-bold">입력 통화를 선택하세요:</label>
      <select id="fromCurrency" class="form-select fs-5" style="width: 300px;" v-model="fromCurrency">
        <option v-for="currency in currencies" :key="currency" :value="currency">{{ currency }}</option>
      </select>
    </div>
    <div class="mb-3">
      <label for="amount" class="form-label text-info fw-bold">숫자를 입력하세요:</label>
      <input type="number" id="amount" class="form-control fs-5 fw-bold" style="width: 300px;" v-model="amount">
    </div>
    <div class="mb-3">
      <label for="toCurrency" class="form-label text-info fw-bold">변환할 통화를 선택하세요:</label>
      <select id="toCurrency" class="form-select fs-5" style="width: 300px;" v-model="toCurrency">
        <option v-for="currency in currencies" :key="currency" :value="currency">{{ currency }}</option>
      </select>
    </div>
    <div>
      <span class="m-0 fw-light text-info fw-bold">바뀐 돈</span>
      <span class="m-0 fw-light fw-bold" v-if="date"> | </span>
      <span class="m-0 fw-light text-info fw-bold" v-if="date">기준: {{ date }}</span>
      
      <h2 class="fs-1 fw-bold mt-0">{{ changeAmount }} {{ toCurrency }}</h2>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue'
import { useFinanceStore } from '@/stores/finance'
const store = useFinanceStore()

const currencies = ref([
  '미국 달러', '유로', '일본 옌', '한국 원', '위안화', '스위스 프랑', 
  '캐나다 달러', '브루나이 달러', '바레인 디나르', '덴마아크 크로네', 
  '영국 파운드', '태국 바트', '홍콩 달러', '싱가포르 달러', 
  '스웨덴 크로나', '사우디 리얄', '뉴질랜드 달러', '노르웨이 크로네', 
  '말레이지아 링기트', '쿠웨이트 디나르', '인도네시아 루피아', 
  '호주 달러', '아랍에미리트 디르함'
])

const fromCurrency = ref('미국 달러')
const toCurrency = ref('한국 원')
const amount = ref(0)

// 이제 django에서 받아온 바뀐 데이터를 여기다 저장
const changeAmount = ref(0)
// 환율적용날짜
const date = ref(null)

// django에 입력 통화와 변경할 통화 나라 보내주기
import axios from 'axios'
const sendCountry = function () {
  // 정기 예금을 위한 axios
  axios({
    method: 'post',
    url: `${store.API_URL}/exchange/calculate/`,
    data: {
      // 입력통화
      inputcountry : fromCurrency.value,
      // 출력통화
      outputcountry: toCurrency.value,
      // 바꿀 돈
      money : amount.value
    }
  }).then((response) => {
    changeAmount.value = response.data.result
    date.value = response.data.exchange_date
  }).catch((error) => {
    console.log(error)
  })
}

// 이제 입력 통화나 입력한 숫자나, 변결할 통화가 바뀔 때마다 sendCountry를 통해 새로운 데이터를 받아옴
watch([fromCurrency, toCurrency, amount], () => {
  sendCountry()
})

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/exchange/api/`
  }).then((respoonse) => {
    console.log(respoonse.data)
  }).catch((error) => {
    console.log(error)
  })
  
})

</script>

<style scoped>
h1 {
  margin-bottom: 20px;
}
</style>