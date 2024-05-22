<template>
  <div class="chat-container">
    <!-- ChatGPT 스타일의 채팅 창 -->
    <div class="chat-box">
      <div class="chat-message">
        <div class="chat-bubble">
          <p>ChatGPT: 안녕하세요! 어떤 상품에 대해 궁금하신가요?</p>
        </div>
      </div>
      <div class="chat-message">
        <div class="chat-bubble">
          <p>ChatGPT: {{ responseData }}</p>
          <div v-for="recommend in recommendArr" :key="recommend.id">
            <button type="button" class="btn btn-custom" @click="showPopup(recommend, kindToUrl())">{{
              recommend.fin_prdt_nm }}</button>
            <h5> </h5>
          </div>
        </div>
        <DepostiDetail v-if="finance" :finance="finance" :kind="sendUrl" @close="closePopup" />
      </div>
    </div>

    <!-- 상품 유형 선택 -->
    <div class="radio-container">
      <label>상품 유형:</label>
      <div class="radio-option" :class="{ 'selected': productType === '예금' }" @click="selectProductType('예금')">
        <label for="deposit">예금</label>
      </div>
      <div class="radio-option" :class="{ 'selected': productType === '정기적금' }" @click="selectProductType('정기적금')">
        <label for="regularInvestment">정기적금</label>
      </div>
      <div class="radio-option" :class="{ 'selected': productType === '자유적금' }" @click="selectProductType('자유적금')">
        <label for="savings">자유적금</label>
      </div>
    </div>

    <!-- 궁금증 입력 -->
    <div class="question-container">
      <label for="questionInput">궁금한 것:</label>
      <input type="text" id="questionInput" v-model="userQuestion" @keyup.enter="submitQuestion">
      <button type="button" class="btn btn-custom" @click="submitQuestion">제출</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useFinanceStore } from '@/stores/finance'
import DepostiDetail from '@/components/DepositDetail.vue'

const store = useFinanceStore()
// 초기 데이터
const productType = ref('예금') // 초기값은 '예금'
const userQuestion = ref('')
const responseData = ref('')

// chatgpt가 추천해준 상품들의 product_id 를 저장할 배열
const recommendArr = ref([])
// chatgpt가 추천해준 상품의 종류 deposit,
const kind = ref('')
// chat gpt가 추천해준 상품들의 product_id를 통해 db에서 해당하는 상품을 찾아
// 배열 형태로 저장
const recommendFinances = ref([])
// 입력 제출
const submitQuestion = () => {
  sendDataToBackend()
}

const finance = ref(null)
const sendUrl = ref('')

// 추천해준 예금, 정기적금, 자유적금 종류에 따라 마땅한 url 값을 알려주기
const kindToUrl = function () {
  if (productType.value === '예금') {
    return 'deposit/like/'
  } else if (productType.value === '정기적금') {
    return 'saving/like_fixed/'
  } else {
    return 'saving/like_free/'
  }
}

const showPopup = function (product, url) {
  finance.value = product
  sendUrl.value = url
}

const closePopup = function () {
  finance.value = null
}

// 백엔드로 데이터 전송
const sendDataToBackend = async () => {
  try {
    const producttype = ref(productType.value)
    if (producttype.value === '예금') {
      producttype.value = 'deposit'
    } else if (producttype.value === '정기적금') {
      producttype.value = 'fixedsaving'
    } else {
      producttype.value = 'freesaving'
    }
    responseData.value = '데이타 생성중~~^^'
    const response = await axios({
      method: 'post',
      url: `${store.API_URL}/recommender/chatbot/`,
      data: {
        message: userQuestion.value,
        producttype: producttype.value
      }
    })
    console.log(response)
    responseData.value = response.data.message
    recommendArr.value = response.data.product
    // 입력창 초기화
    userQuestion.value = ''
    console.log(recommendArrId.value)
    for (let recommend of recommendArr.value) {
      console.log(recommend)
    }
  } catch (error) {
    console.error('Error sending data to backend:', error)
  }
}

// 상품 유형 선택 함수
const selectProductType = (type) => {
  productType.value = type
}
</script>

<style scoped>
/* ChatGPT 스타일 */
.chat-container {
  max-width: 800px;
  margin: 0 auto;
}

.chat-box {
  background-color: #f5f5f5;
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 20px;
  overflow-y: auto;
  height: 500px;
}

.chat-message {
  margin-bottom: 10px;
}

.chat-bubble {
  background-color: #fff;
  border-radius: 15px;
  padding: 10px 15px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  max-width: 90%;
}

.radio-container {
  margin-bottom: 20px;
}

.radio-container label {
  margin-right: 10px;
}

.radio-option {
  display: inline-block;
  margin-right: 15px;
  cursor: pointer;
}

.radio-option.selected label {
  color: #007bff;
}

.radio-option:hover label {
  cursor: pointer;
}

.question-container {
  margin-bottom: 20px;
}

.question-container label {
  margin-right: 10px;
}

.question-container input[type="text"] {
  width: calc(100% - 100px);
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-right: 10px;
}

.question-container button {
  padding: 8px 15px;
  background-color: #4CAF50;
  /* Custom green */
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.question-container button:hover {
  background-color: #45a049;
  /* Darker green */
}

/* 커스텀 버튼 색상 */
.btn-custom {
  background-color: #4CAF50;
  /* Custom green */
  color: white;
  border: none;
  border-radius: 4px;
  padding: 8px 15px;
  margin-top: 5px;
}

.btn-custom:hover {
  background-color: #45a049;
  /* Darker green */
}</style>