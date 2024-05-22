import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { defineStore } from 'pinia'
import axios from 'axios'

const getDB = ref(true)
const getDB2 = ref(true)

export const useFinanceStore = defineStore('finance', () => {

  // 서버 처음 시작될 때 예적금 데이터 가져오기 위하여 설정
  const initializeData = async () => {
    try {
      if (getDB.value === true) {
        await axios({
          method: 'get',
          url: 'http://127.0.0.1:8000/deposit/api'
        })
        console.log('예금DB저장완료')
        getDB.value = false
      }
    } catch (error) {
      console.log('예금DB저장실패')
    }

    try {
      if (getDB2.value === true) {
        await axios({
          method: 'get',
          url: 'http://127.0.0.1:8000/saving/api'
        })
        console.log('적금DB저장완료')
        getDB2.value = false
      }
    } catch (error) {
      console.log('적금DB저장실패')
    }
  }

  // 초기 데이터 로드
  initializeData()

  const dbSaving = function () {
    if (getDB2.value === true) {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/saving/api'
      }).then((response) => {
        console.log('적금DB저장완료')
        getDB2.value = false
      }).catch((error) => {
        console.log('적금DB저장실패')
      })
    }
  }

  const API_URL = 'http://127.0.0.1:8000'
  const finances = ref([])
  const finances2 = ref([])
  const finances3 = ref([])

  const userInfo = ref([])
  const userId = ref(null)
  const router = useRouter()
  const token = ref(null)
  const write = ref(true)

  const isLogin = computed(() => {
    return token.value !== null
  })

  const signUp = function (payload) {
    const { name, username, email, password1, password2, postcode, roadAddress, jibunAddress, detailAddress } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        name, username, email, password1, password2, postcode,
        roadaddress: roadAddress,
        jibunaddress: jibunAddress,
        detailaddress: detailAddress
      }
    })
      .then((response) => {
        console.log('회원가입 성공!')
        const password = password1
        logIn({ username, password })
      })
      .catch((error) => {
        if (error.response.status === 400) {
          alert("회원가입 실패 다시 시도해주세요.")
        }
      })
  }

  const logIn = function (payload) {
    const { username, password } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((response) => {
        console.log('로그인 성공!')
        token.value = response.data.key

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
          alert("회원가입되지 않은 사용자입니다.")
        }
      })
  }

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

  const getFixedSaving = function () {
    axios({
      method: 'get',
      url: `${API_URL}/saving/fixed/products/`
    }).then(response => {
      finances2.value = response.data
    }).catch(error => {
      console.log(error)
    })
  }

  const getFreeSaving = function () {
    axios({
      method: 'get',
      url: `${API_URL}/saving/free/products/`
    }).then(response => {
      finances3.value = response.data
    }).catch(error => {
      console.log(error)
    })
  }

  const changeFinances = function (data) {
    finances.value = data
  }

  const changeFinances2 = function (data) {
    finances2.value = data
  }

  const changeFinances3 = function (data) {
    finances3.value = data
  }

  return {
    API_URL, getDeposits, getFreeSaving, getFixedSaving, finances, finances2, finances3,
    changeFinances, changeFinances2, changeFinances3, token, isLogin, logIn, signUp,
    userInfo, userId, write, getDB2, dbSaving
  }
}, { persist: true })