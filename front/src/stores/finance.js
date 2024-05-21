import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { defineStore } from 'pinia'
import axios from 'axios'


const getDB = ref(true)

export const useFinanceStore = defineStore('finance', () => {

  // 서버 처음 시작될때 예적금 데이터 가져오기 위하여 설정
  if (getDB) {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/deposit/api'
    })
    getDB.value = false
  } 



  const getDB2 = ref(true)


  const dbSaving = function () {
    if (getDB2.value) {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/saving/api'
      })
    getDB2.value = false
    }
   
  }

  const API_URL = 'http://127.0.0.1:8000'
  // 예금을 위한 배열
  const finances = ref([])
  // 정기적금을 위한 배열
  const finances2 = ref([])
  // 자유적금을 위한 배열
  const finances3 = ref([])

  // 지금 로그인한 사용자 정보를 저장하기 위한 배열
  const userInfo = ref([])
  const userId = ref(null)

  const router = useRouter()
  // django에서 authorization header를 위한 토큰
  const token = ref(null)

  // 현재 게시글 작성 페이진지 아닌지 확인용 변수
  const write = ref(true)

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
    const { name, username, email, password1, password2, postcode, roadAddress, jibunAddress, detailAddress } = payload

    // 2. axios로 django에 요청을 보냄
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        name, username, email, password1, password2, postcode,
        roadaddress: roadAddress,
        jibunaddress : jibunAddress,
        detailaddress : detailAddress
      }
    })
     .then((response) => {
       console.log('회원가입 성공!')
       const password = password1
       logIn({ username, password })
     })
     .catch((error) => {
      if (error.response.status === 400) {
         // 사용자 데이터에 없는 경우 처리
         // 여기에서 모달 창을 띄우거나 적절한 메시지를 화면에 표시할 수 있습니다.
        alert("회원가입 실패 다시 시도해주세요.")
      }
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
        console.log('로그인 성공!')
        // console.log(response)
        // console.log(response.data.key)
        // 3. 로그인 성공 후 응답 받은 토큰을 저장
        token.value = response.data.key
        // 로그인성공후 로그이한 사용자의 정보를 받아오기
        axios({
          method: 'get',
          url: `${API_URL}/accounts/user/`,
          headers: {
            Authorization: `Token ${token.value}`
          }
        }).then((response) => {
          console.log(response.data)
          userInfo.value = response.data
          userId.value = userInfo.value['username']
        }).catch((error) => {
          console.log(error)
        })
        router.push({ name: 'MainPageView' })
      })
      .catch((error) => {
        console.log(error)
        if (error.response.status === 400) {
          // 사용자 데이터에 없는 경우 처리
          // 여기에서 모달 창을 띄우거나 적절한 메시지를 화면에 표시할 수 있습니다.
          alert("회원가입되지 않은 사용자입니다.")
        }
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


  return { API_URL, getDeposits, getFreeSaving, getFixedSaving, finances, finances2, finances3, changeFinances, changeFinances2, changeFinances3, token, isLogin, logIn, signUp, userInfo, userId, write, getDB2, dbSaving }
},{ persist: true })
