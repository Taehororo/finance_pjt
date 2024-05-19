import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'


export const useFinanceStore = defineStore('finance', () => {
  const API_URL = 'http://127.0.0.1:8000/'
  // 예금을 위한 배열
  const finances = ref([])
  // 정기적금을 위한 배열
  const finances2 = ref([])
  // 자유적금을 위한 배열
  const finances3 = ref([])


  // django에서 authorization header를 위한 토큰
  const token = ref(null)

  // 로그인한 상태냐 아니냐를 위한 함수
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  // 회원가입 함수
  const signUp = function (payload) {
    // 1. 사용자 입력 데이터를 받아
    // const username = payload.username
    // const password1 = payload.password1
    // const password2 = payload.password2
    const { username, password1, password2 } = payload

    // 2. axios로 django에 요청을 보냄
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        // username: username,
        // password1: password1,
        // password2: password2
        username, password1, password2
      }
    })
     .then((response) => {
       console.log('회원가입 성공!')
       const password = password1
       logIn({ username, password })
     })
     .catch((error) => {
       console.log(error)
     })
  }
  // 로그인 로직
  const logIn = function (payload) {
    // 1. 사용자 입력 데이터를 받아
    const { username, password } = payload
    // 2. axios로 django에 요청을 보냄
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((response) => {
        // console.log('로그인 성공!')
        // console.log(response)
        // console.log(response.data.key)
        // 3. 로그인 성공 후 응답 받은 토큰을 저장
        token.value = response.data.key
        router.push({ name : 'ArticleView' })
      })
      .catch((error) => {
        console.log(error)
      })
  }


  

  // django에서 정기예금 데이터 넣기
  const getDeposits = function () {
    axios({
      method: 'get',
      url: `${API_URL}/deposit/products/`
    }).then(response => {
      finances.value = response.data
    }).catch(error => {
      console.log(error)
    })
  }
    // django에서 정기적금 데이터 받기
    const getFixedSaving = function () {
      axios({
        method: 'get',
        // 수정필요
        url: `${API_URL}/saving/fixed/products/`
      }).then(response => {
        finances2.value = response.data
      }).catch(error => {
        console.log(error)
      })
    }
    
   // django에서 자유적금 데이터 받기
  const getFreeSaving = function () {
    axios({
      method: 'get',
      // 수정필요
      url: `${API_URL}/saving/free/products/`
    }).then(response => {
      finances3.value = response.data
      console.log(response.data)
    }).catch(error => {
      console.log(error)
    })
  }



  // django에서 정렬된 기준으로 새로 온 데이터를 finances에 저장
  const changeFinances = function (data) {
    finances.value = data
  }

  // django에서 정렬된 기준으로 새로 온 정기적금 데이터를 finances2에 저장
  const changeFinances2 = function (data) {
    finances2.value = data
  }

  // django에서 정렬된 기준으로 새로 온 자유적금 데이터를 finances3에 저장
  const changeFinances3 = function (data) {
    finances3.value = data
  }  


  return { API_URL, getDeposits, getFreeSaving,getFixedSaving, finances, finances2, finances3, changeFinances, changeFinances2, changeFinances3 }
})
