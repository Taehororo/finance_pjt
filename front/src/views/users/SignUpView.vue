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

        <!-- 이메일 입력 -->
        <div class="form-group mb-3">
          <label for="email_id" class="form-label">이메일</label>
          <div class="input-group">
            <input type="text" v-model.trim="emailId" id="email_id" class="form-control form_w200" placeholder="이메일"
              maxlength="18" title="이메일 아이디">
            <span class="input-group-text">@</span>
            <input type="text" v-model.trim="emailDomain" id="email_domain" class="form-control form_w200"
              placeholder="이메일 도메인" maxlength="18" title="이메일 도메인">
            <select class="form-select" title="이메일 도메인 주소 선택" @change="setEmailDomain($event.target.value)">
              <option value="">-선택-</option>
              <option value="naver.com">naver.com</option>
              <option value="gmail.com">gmail.com</option>
              <option value="hanmail.net">hanmail.net</option>
              <option value="hotmail.com">hotmail.com</option>
              <option value="korea.com">korea.com</option>
              <option value="nate.com">nate.com</option>
              <option value="yahoo.com">yahoo.com</option>
            </select>
          </div>
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
import { ref, onMounted } from 'vue'
import { useFinanceStore } from '@/stores/finance'

onMounted(() => {
  // script src='//t1.daumcdn.net/mapjsapi/bundle/postcode/prod/postcode.v2.js'이 코드를 쓸수 없기에 추가해준 것
  const script = document.createElement('script');
  script.src = '//t1.daumcdn.net/mapjsapi/bundle/postcode/prod/postcode.v2.js';
  script.onload = () => {
    // 외부 스크립트가 로드된 후에 실행할 코드를 작성합니다.
    // 이 곳에서 해당 스크립트를 사용하는 코드를 작성합니다.
  };
  document.head.appendChild(script);
})

// 데이터 바인딩
const name = ref('')
const username = ref('')
const emailId = ref('')
const emailDomain = ref('')
const password1 = ref('')
const password2 = ref('')
const store = useFinanceStore()

// 이메일 도메인 설정 함수
const setEmailDomain = (domain) => {
  emailDomain.value = domain
}

// 회원가입 함수
const signUp = () => {
  const email = `${emailId.value}@${emailDomain.value}`
  const emailRule = /^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$/i

  if (!emailId.value) {
    alert('이메일을 입력해주세요')
    document.getElementById('email_id').focus()
    return false
  }

  if (!emailDomain.value) {
    alert('도메인을 입력해주세요')
    document.getElementById('email_domain').focus()
    return false
  }

  if (!emailRule.test(email)) {
    alert('이메일을 형식에 맞게 입력해주세요.')
    return false
  }

  const payload = {
    name: name.value,
    username: username.value,
    email: email,
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
  emailId.value = ''
  emailDomain.value = ''
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
    const width = 500; // 창의 너비
    const height = 600; // 창의 높이
    const left = (window.innerWidth / 2) - (width / 2) + 20; // 살짝 오른쪽으로 이동
    const top = (window.innerHeight / 2) - (height / 2);

    const postcodeLayer = document.createElement('div');
    postcodeLayer.style.position = 'fixed';
    postcodeLayer.style.width = `${width}px`;
    postcodeLayer.style.height = `${height}px`;
    postcodeLayer.style.left = `${left}px`;
    postcodeLayer.style.top = `${top}px`;
    postcodeLayer.style.zIndex = 1000; // Ensure the layer is on top
    postcodeLayer.style.border = '1px solid #ccc'; // 테두리 추가
    postcodeLayer.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.1)'; // 그림자 추가
    postcodeLayer.id = 'postcodeLayer';
    document.body.appendChild(postcodeLayer);

    new daum.Postcode({
      oncomplete: function (data) {
        // 우편번호와 주소 필드에 값 채우기
        document.getElementById('sample4_postcode').value = data.zonecode;
        document.getElementById('sample4_roadAddress').value = data.roadAddress;
        document.getElementById('sample4_jibunAddress').value = data.jibunAddress;

        // 팝업 레이어 제거
        document.body.removeChild(postcodeLayer);
      },
      width: '100%',
      height: '100%'
    }).embed(postcodeLayer);
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
  padding-top: 80px;
  /* 폼을 위로 올리기 위한 여백 조정 */
}

.signup-form {
  background: white;
  padding: 40px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 500px;
  /* 더 직사각형으로 만들기 위한 최대 너비 설정 */
}

.logo {
  width: 50px;
  /* 로고 이미지 크기 조정 */
  height: 50px;
}

.form-label {
  font-weight: bold;
}

.form-group .input-group {
  display: flex;
  align-items: center;
}

.form-group .input-group .form-control.form_w200 {
  flex: 1;
  max-width: 200px;
}

.form-group .input-group .input-group-text {
  padding: 0.375rem 0.75rem;
  border-radius: 0;
  border-left: none;
  border-right: none;
}

.form-group .input-group .form-select {
  flex: 1;
  max-width: 200px;
}

.btn-primary {
  background-color: #007bff;
  border: none;
}

.btn-primary:hover {
  background-color: #0056b3;
}
</style>