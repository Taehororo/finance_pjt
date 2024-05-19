<template>
    <div class="login-page">
      <div class="login-form">
        <img src="@/assets/images/file.png" alt="Logo" class="logo mb-4">
        <span class="text-center mb-4 fs-2 fw-bold">THBank Login</span>
        <form @submit.prevent="logIn">
          <div class="form-group mb-3">
            <label for="username" class="form-label">아이디</label>
            <input type="text" v-model.trim="username" id="username" class="form-control">
          </div>
          <div class="form-group mb-3">
            <label for="password" class="form-label">비밀번호</label>
            <input type="password" v-model.trim="password" id="password" class="form-control">
          </div>
          <button type="submit" class="btn btn-primary w-100">로그인</button>
        </form>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { useFinanceStore } from '@/stores/finance'
  
  const username = ref(null)
  const password = ref(null)
  const store = useFinanceStore()
  
  const logIn = function () {
    const payload = {
      username: username.value,
      password: password.value
    }
    store.logIn(payload)
  }
  </script>
  
  <style scoped>
  .login-page {
    height: 100vh;
    display: flex;
    align-items: flex-start;
    justify-content: center;
    background: #f8f9fa;
    padding-top: 80px; /* Adjust padding to move the form higher */
  }
  
  .login-form {
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