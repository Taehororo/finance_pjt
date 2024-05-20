<template>
  <div class="container">
    <p>이름 : {{ userInfo.name }}</p>
    <p>ID : {{ userInfo.username }}</p>
    <p>우편번호 : {{ userInfo.postcode }}</p>
    <p>도로명주소 : {{ userInfo.roadaddress }}</p>
    <p>지번주소 : {{ userInfo.jibunaddress }}</p>
    <p>상세주소 : {{ userInfo.detailaddress }}</p>

    <div>
      <h1>찜한 목록</h1>
      <h3>정기 예금</h3>
      <div v-for="liked_product in userInfo.liked_deposit_products" v-if="Length(userInfo.liked_deposit_products)">
        <button  type="button" class="btn btn-info" @click="showPopup(liked_product)">상세정보</button>
        <p>은행명 : {{ liked_product.kor_co_nm }}</p>
        <p>상품명 : {{ liked_product.fin_prdt_nm }}</p>
        <DepostiDetail v-if="finance" :finance="finance" :kind="'deposit/like/'" @close="finance = null" />
        <hr>
      </div>
      <div v-else>
        <p>찜한 상품이 없습니다.</p>
        <hr>
      </div>

      <h3>정기 적금</h3>
      <div v-for="liked_product in userInfo.liked_fixed_saving_products" v-if="Length(userInfo.liked_fixed_saving_products)">
          <p>은행명 : {{ liked_product.kor_co_nm }}</p>
          <p>상품명 : {{ liked_product.fin_prdt_nm }}</p>
          <DepostiDetail v-if="finance" :finance="finance" :kind="'saving/like_fixed/'" @close="finance = null" />
          <button type="button" class="btn btn-info" @click="showPopup(liked_product)">상세정보</button>
          <hr>

        
      </div>
      <div v-else>
        <p>찜한 상품이 없습니다.</p>
        <hr>
      </div>

      <h3>자유 적금</h3>
      <div v-for="liked_product in userInfo.liked_free_saving_products" v-if="Length(userInfo.liked_free_saving_products)">
        <button type="button" class="btn btn-info" @click="showPopup(liked_product)">상세정보</button>
        <p>은행명 : {{ liked_product.kor_co_nm }}</p>
        <p>상품명 : {{ liked_product.fin_prdt_nm }}</p>
        <DepostiDetail v-if="finance" :finance="finance" :kind="'saving/like_free/'" @close="finance = null" />
        <hr>
      </div>
      <div v-else>
        <p>찜한 상품이 없습니다.</p>
        <hr>
      </div>
    </div>
    
    
    
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useFinanceStore } from '@/stores/finance'
import DepostiDetail from '@/components/DepositDetail.vue'
import axios from 'axios'
const store = useFinanceStore()
const route = useRoute()
const router = useRouter()

const reload = function () {
  router.go(0)
}
const userInfo = ref(store.userInfo)

const finance = ref(null)

const showPopup = function (arr) {
  finance.value = arr
  console.log(finance.value)
}

const Length = function (arr) {
  if (arr.length > 0) {
    return true
  }
  else {
    return false
  }
}
// user의 정보를 받아오기 위해
onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/accounts/user/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  }).then((response) => {
    console.log(response.data)
    store.userInfo = response.data
  }).catch((error) => {
    console.log(error)
  })

})


</script>

<style scoped>

</style>