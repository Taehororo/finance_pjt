<template>
  <div>
    <div class="bg-info-subtle d-flex align-items-center justify-content-center container" style="height: 100px;">
      <h2 class="fw-bold">환율변환</h2>
    </div>
    <!-- 입력 통화에 대한 그래프 -->
    <div class="container mt-5">
      <div class="row">
        <div class="col">
          <createChart :dates="inCountry['dates']" :rates="inCountry['rates']" :kind="'입력'" :key="inCountry['dates']" />
        </div>
        <!-- 가운데 영역은 그대로 두세요 -->
        <div class="col">
          <!-- 입력 및 출력 통화 선택 등의 요소 -->
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
        </div>
        <!-- 출력 통화에 대한 그래프 -->
        <div class="col">
          <createChart :dates="outCountry['dates']" :rates="outCountry['rates']" :kind="'출력'"
            :key="outCountry['dates']" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
// chart.js 써볼까?
import createChart from '@/components/createChart.vue'


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

// 그래프를 입력통화나라와 출력통화나라별 정보를 저장할거임
const inCountry = ref({})
const outCountry = ref({})


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
    // 그래프를 그리기위해 각나라별 일주일간 환율정보 저장
    inCountry.value = response.data.input_country
    outCountry.value = response.data.output_country
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
  }).then((response) => {
    inCountry.value = response.data.input_country
    outCountry.value = response.data.output_country
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