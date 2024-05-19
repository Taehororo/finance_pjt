<template>
  <div class="signup-page">
    <div class="signup-form">
      <!-- 로고 이미지 -->
      <img src="@/assets/images/file.png" alt="Logo" class="logo mb-4">
      <!-- 제목 -->
      <span class="text-center mb-4 fs-2 fw-bold">THBank Signup</span>
      <!-- 회원가입 양식 -->
      <form @submit.prevent="signUp">

        <!-- 이름 입력 -->
        <div class="form-group mb-3">
          <label for="name" class="form-label">이름</label>
          <input type="text" v-model.trim="name" id="name" class="form-control">
        </div>

        <!-- 주소 입력 -->
        <div class="form-group mb-3">
          <label for="sample4_postcode" class="form-label">주소</label>
          <div class="input-group">
            <input type="text" id="sample4_postcode" placeholder="우편번호" class="form-control">
            <button type="button" @click="sample4_execDaumPostcode" class="btn btn-outline-secondary">우편번호 찾기</button>
          </div>
        </div>
        <!-- 도로명주소 입력 -->
        <div class="form-group mb-3">
          <input type="text" id="sample4_roadAddress" placeholder="도로명주소" class="form-control">
        </div>
        <!-- 지번주소 입력 -->
        <div class="form-group mb-3">
          <input type="text" id="sample4_jibunAddress" placeholder="지번주소" class="form-control">
        </div>
        <!-- 상세주소 입력 -->
        <div class="form-group mb-3">
          <input type="text" id="sample4_detailAddress" placeholder="상세주소" class="form-control">
        </div>

        <!-- 아이디 입력 -->
        <div class="form-group mb-3">
          <label for="username" class="form-label">아이디</label>
          <input type="text" v-model.trim="username" id="username" class="form-control">
        </div>
        <!-- 비밀번호 입력 -->
        <div class="form-group mb-3">
          <label for="password1" class="form-label">비밀번호</label>
          <input type="password" v-model.trim="password1" id="password1" class="form-control">
        </div>
        <!-- 비밀번호 확인 입력 -->
        <div class="form-group mb-3">
          <label for="password2" class="form-label">비밀번호 확인</label>
          <input type="password" v-model.trim="password2" id="password2" class="form-control">
        </div>
        <!-- 회원가입 버튼 -->
        <button type="submit" class="btn btn-primary w-100">회원가입</button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useFinanceStore } from '@/stores/finance'

// 데이터 바인딩
const name = ref('')
const username = ref('')
const password1 = ref('')
const password2 = ref('')
const store = useFinanceStore()

// 회원가입 함수
const signUp = () => {
  const payload = {
    name: name.value,
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    postcode: document.getElementById('sample4_postcode').value,
    roadAddress: document.getElementById('sample4_roadAddress').value,
    jibunAddress: document.getElementById('sample4_jibunAddress').value,
    detailAddress: document.getElementById('sample4_detailAddress').value
  }
  // 회원가입 정보 전달
  store.signUp(payload)

  // 회원가입 후 입력 필드 초기화
  name.value = ''
  username.value = ''
  password1.value = ''
  password2.value = ''
  document.getElementById('sample4_postcode').value = ''
  document.getElementById('sample4_roadAddress').value = ''
  document.getElementById('sample4_jibunAddress').value = ''
  document.getElementById('sample4_detailAddress').value = ''
}

// 우편번호 찾기 기능
const sample4_execDaumPostcode = () => {
  if (typeof daum !== 'undefined' && typeof daum.Postcode === 'function') {
    new daum.Postcode({
      oncomplete: function(data) {
        // 우편번호와 주소 필드에 값 채우기
        document.getElementById('sample4_postcode').value = data.zonecode;
        document.getElementById('sample4_roadAddress').value = data.roadAddress;
        document.getElementById('sample4_jibunAddress').value = data.jibunAddress;
      }
    }).open();
  } else {
    console.error('Daum postcode script is not loaded.');
  }
}
</script>

<style scoped>
.signup-page {
  height: 100vh;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  background: #f8f9fa;
  padding-top: 80px; /* 폼을 위로 올리기 위한 여백 조정 */
}

.signup-form {
  background: white;
  padding: 40px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 500px; /* 더 직사각형으로 만들기 위한 최대 너비 설정 */
}

.logo {
  width: 50px; /* 로고 이미지 크기 조정 */
  height: 50px;
}

.form-label {
  font-weight: bold;
}

.btn-primary {
  background-color: #007bff;
  border: none;
}

.btn-primary:hover {
  background-color: #0056b3;
}
</style>