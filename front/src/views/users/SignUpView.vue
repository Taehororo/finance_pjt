<template>
    <div class="signup-page">
      <div class="signup-form">
        <img src="@/assets/images/file.png" alt="Logo" class="logo mb-4">
        <span class="text-center mb-4 fs-2 fw-bold">THBank Signup</span>
        <form @submit.prevent="signUp">
          <div class="form-group mb-3">
            <label for="username" class="form-label">아이디</label>
            <input type="text" v-model.trim="username" id="username" class="form-control">
          </div>
          <div class="form-group mb-3">
            <label for="password1" class="form-label">비밀번호</label>
            <input type="password" v-model.trim="password1" id="password1" class="form-control">
          </div>
          <div class="form-group mb-3">
            <label for="password2" class="form-label">비밀번호 확인</label>
            <input type="password" v-model.trim="password2" id="password2" class="form-control">
          </div>
          <button type="submit" class="btn btn-primary w-100">회원가입</button>
        </form>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { useFinanceStore } from '@/stores/finance'
  
  const username = ref(null)
  const password1 = ref(null)
  const password2 = ref(null)
  const store = useFinanceStore()
  
  const signUp = function () {
    const payload = {
      username: username.value,
      password1: password1.value,
      password2: password2.value
    }
    store.signUp(payload)
  }
  </script>
  
  <style scoped>
  .signup-page {
    height: 100vh;
    display: flex;
    align-items: flex-start;
    justify-content: center;
    background: #f8f9fa;
    padding-top: 80px; /* Adjust padding to move the form higher */
  }
  
  .signup-form {
    background: white;
    padding: 40px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    width: 100%;
    max-width: 500px; /* Increase width to make it more rectangular */
  }
  
  .logo {
    width: 50px; /* Adjust the size of the logo */
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