<template>
  <div class="container mt-5">
    <div class="card mb-4">
      <div class="card-header bg-light">
        <h2 class="mb-0">나의 정보</h2>
      </div>
      <div class="card-body">
        <div class="mb-3">
          <strong>이름:</strong> {{ userInfo.name }}
        </div>
        <div class="mb-3">
          <strong>ID:</strong> {{ userInfo.username }}
        </div>
        <div class="mb-3">
          <strong>우편번호:</strong> {{ userInfo.postcode }}
        </div>
        <div class="mb-3">
          <strong>도로명주소:</strong> {{ userInfo.roadaddress }}
        </div>
        <div class="mb-3">
          <strong>지번주소:</strong> {{ userInfo.jibunaddress }}
        </div>
        <div class="mb-3">
          <strong>상세주소:</strong> {{ userInfo.detailaddress }}
        </div>
      </div>
    </div>

    <div class="card mb-4">
      <div class="card-header bg-light">
        <h2 class="mb-0">찜한 목록</h2>
      </div>
      <div class="card-body">
        <div v-if="hasLikedProducts">
          <h3 class="mb-3">정기 예금</h3>
          <template v-if="userInfo.liked_deposit_products.length">
            <div v-for="liked_product in userInfo.liked_deposit_products" :key="liked_product.base_product_id"
              class="mb-3 p-3 border rounded bg-light">
              <p><strong>은행명:</strong> {{ liked_product.kor_co_nm }}</p>
              <p><strong>상품명:</strong> {{ liked_product.fin_prdt_nm }}</p>
              <button type="button" class="btn btn-outline-success mt-2"
                @click="showPopup(liked_product, 'deposit/like/')">상세정보</button>
            </div>
          </template>
          <template v-else>
            <p>찜한 정기 예금 상품이 없습니다.</p>
          </template>

          <h3 class="mt-4 mb-3">정기 적금</h3>
          <template v-if="userInfo.liked_fixed_saving_products.length">
            <div v-for="liked_product in userInfo.liked_fixed_saving_products" :key="liked_product.base_product_id"
              class="mb-3 p-3 border rounded bg-light">
              <p><strong>은행명:</strong> {{ liked_product.kor_co_nm }}</p>
              <p><strong>상품명:</strong> {{ liked_product.fin_prdt_nm }}</p>
              <button type="button" class="btn btn-outline-success mt-2"
                @click="showPopup(liked_product, 'saving/like_fixed/')">상세정보</button>
            </div>
          </template>
          <template v-else>
            <p>찜한 정기 적금 상품이 없습니다.</p>
          </template>

          <h3 class="mt-4 mb-3">자유 적금</h3>
          <template v-if="userInfo.liked_free_saving_products.length">
            <div v-for="liked_product in userInfo.liked_free_saving_products" :key="liked_product.base_product_id"
              class="mb-3 p-3 border rounded bg-light">
              <p><strong>은행명:</strong> {{ liked_product.kor_co_nm }}</p>
              <p><strong>상품명:</strong> {{ liked_product.fin_prdt_nm }}</p>
              <button type="button" class="btn btn-outline-success mt-2"
                @click="showPopup(liked_product, 'saving/like_free/')">상세정보</button>
            </div>
          </template>
          <template v-else>
            <p>찜한 자유 적금 상품이 없습니다.</p>
          </template>
        </div>
        <template v-else>
          <p>찜한 상품이 없습니다.</p>
        </template>
      </div>
    </div>

    <DepostiDetail v-if="finance" :finance="finance" :kind="kind" @close="closePopup" />
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useFinanceStore } from '@/stores/finance'
import DepostiDetail from '@/components/DepositDetail.vue'
import axios from 'axios'

const store = useFinanceStore()
const route = useRoute()
const router = useRouter()

const userInfo = ref(store.userInfo)
const finance = ref(null)
const kind = ref('')

const showPopup = function (product, type) {
  finance.value = product
  kind.value = type
}

const closePopup = function () {
  finance.value = null
}

const hasLikedProducts = computed(() => {
  return userInfo.value.liked_deposit_products.length || userInfo.value.liked_fixed_saving_products.length || userInfo.value.liked_free_saving_products.length
})

// user의 정보를 받아오기 위해
onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/accounts/user/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  }).then((response) => {
    store.userInfo = response.data
    userInfo.value = response.data
  }).catch((error) => {
    console.log(error)
  })
})
</script>

<style scoped>
.container {
  margin-top: 20px;
}

.card {
  margin-bottom: 20px;
  
}


.card-header {
  background-color: #f8f9fa;
}

.card-body {
  padding: 20px;
}

.btn-outline-success {
  margin-top: 10px;
}

.bg-light {
  background-color: #f8f9fa !important;
}

.mb-3 {
  margin-bottom: 1rem;
}

.mt-4 {
  margin-top: 1.5rem;
}
</style>