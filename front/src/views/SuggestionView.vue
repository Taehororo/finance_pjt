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
        </div>
      </div>
    </div>

    <!-- 상품 유형 선택 -->
    <div class="radio-container">
      <label>상품 유형:</label>
      <div>
        <input type="radio" id="deposit" value="예금" v-model="productType" @change="sendDataToBackend">
        <label for="deposit">예금</label>
      </div>
      <div>
        <input type="radio" id="investment" value="장기적금" v-model="productType" @change="sendDataToBackend">
        <label for="investment">장기적금</label>
      </div>
      <div>
        <input type="radio" id="savings" value="자유적금" v-model="productType" @change="sendDataToBackend">
        <label for="savings">자유적금</label>
      </div>
    </div>

    <!-- 궁금증 입력 -->
    <div class="question-container">
      <label for="questionInput">궁금한 것:</label>
      <input type="text" id="questionInput" v-model="userQuestion" @keyup.enter="submitQuestion">
      <button type="button" @click="submitQuestion">제출</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

// 초기 데이터
const productType = ref('예금') // 초기값은 '예금'
const userQuestion = ref('')
const responseData = ref('')

// 입력 제출
const submitQuestion = () => {
  sendDataToBackend()
}

// 백엔드로 데이터 전송
const sendDataToBackend = async () => {
  try {
    const response = await axios.post('/api/chatgpt', {
      productType: productType.value,
      userQuestion: userQuestion.value
    })
    responseData.value = response.data.answer
    // 입력창 초기화
    userQuestion.value = ''
  } catch (error) {
    console.error('Error sending data to backend:', error)
  }
}
</script>

<style scoped>
/* ChatGPT 스타일 */
.chat-container {
  max-width: 600px;
  margin: 0 auto;
}

.chat-box {
  background-color: #f5f5f5;
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 20px;
  overflow-y: auto;
  max-height: 300px;
}

.chat-message {
  margin-bottom: 10px;
}

.chat-bubble {
  background-color: #fff;
  border-radius: 15px;
  padding: 10px 15px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  max-width: 70%;
}

.radio-container {
  margin-bottom: 20px;
}

.radio-container label {
  margin-right: 10px;
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
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.question-container button:hover {
  background-color: #45a049;
}
</style>