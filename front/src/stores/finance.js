import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'


export const useFinanceStore = defineStore('finance', () => {
  const API_URL = 'http://127.0.0.1:8000'
  // 예금을 위한 배열
  const finances = ref([])
  // 정기적금을 위한 배열
  const finances2 = ref([])
  // 자유적금을 위한 배열
  const finances3 = ref([])

  const token = ref(null)
  
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

   // django에서 자유적금 데이터 받기
  const getFreeSaving = function () {
    axios({
      method: 'get',
      // 수정필요
      url: `${API_URL}/saving/products/`
    }).then(response => {
      finances2.value = response.data
    }).catch(error => {
      console.log(error)
    })
  }

  // django에서 정기적금 데이터 받기
  const getFixedSaving = function () {
    axios({
      method: 'get',
      // 수정필요
      url: `${API_URL}/saving/products/`
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


  return { API_URL, getDeposits, getFreeSaving,getFixedSaving, finances, changeFinances, changeFinances2, changeFinances3 }
})
