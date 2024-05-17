import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'


export const useFinanceStore = defineStore('finance', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const finances = ref([])
  const token = ref(null)
  
  // django에서 정기예금 데이터 넣기
  const getDeposits = function () {
    axios({
      method: 'get',
      url: `${API_URL}/deposit/products/`
    }).then(response => {
      console.log(response.data)
      finances.value = response.data
    }).catch(error => {
      console.log(error)
    })
  }

  // django에서 정렬된 기준으로 새로 온 데이터를 finances에 저장
  const changeFinances = function (data) {
    console.log(data)
    finances.value = data
  }


  return { API_URL, getDeposits, finances, changeFinances }
})
