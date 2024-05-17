import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'


export const useFinanceStore = defineStore('finance', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const finances = ref([])
  const token = ref(null)
  
  const getDeposits = function () {
    axios({
      method: 'get',
      url: `${API_URL}/deposit/products/`
    }).then(response => {
      // console.log(response)
      finances.value = response.data
      console.log(response.data)
    }).catch(error => {
      console.log(error)
    })
  }


  return { API_URL, getDeposits, finances }
})
