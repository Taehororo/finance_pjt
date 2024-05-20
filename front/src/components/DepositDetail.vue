<template>
  <div class="popup">
    <div class="popup-content">
      <span class="close" @click="$emit('close')">&times;</span>
      <b class="text-info fs-2">{{ finance.fin_prdt_nm  }}</b>
      <h5 class="mt-3 font-weight-bold">{{ finance.kor_co_nm  }}</h5>
      <hr class="mt-4 mb-4">
      <h6 class="mt-3 font-weight-bold text-info"> 우대
        <h5 class="m-1 text-dark">{{ finance.spcl_cnd  }}</h5>
      </h6>
      <h6 class="mt-3 font-weight-bold text-info"> 가입 방법 
        <h5 class="m-1 text-dark">{{ finance.join_way }}</h5>
      </h6>
      <h6 class="mt-3 font-weight-bold text-info"> 가입 대상자 
        <h5 class="m-1 text-dark">{{ finance.join_member }}</h5>
      </h6>
      <h6 class="mt-3 font-weight-bold text-info"> 만기 후 이자율 
        <h5 class="m-1 text-dark">{{ finance.mtrt_int }}</h5>
      </h6>
      <h6 class="text-body-tertiary">*{{ finance.etc_note }}</h6>
      <!-- 로그인한 사용자만 이버튼이 보이도록 -->
      <div v-if="store.token">
        <!-- 이미 찜목록에 추가한 사용자 -->
        <button type="button" class="btn btn-info" @click="checkLiked" v-if="liked===true">찜취소</button>
        <!-- 찜목록에 들어가있지 않은 사용자 -->
        <button type="button" class="btn btn-info" @click="checkLiked" v-if="liked===false">찜하기</button>
      </div>
      
    </div>
  </div>
</template>

<script setup>
import { defineProps, onMounted, ref } from 'vue'
import { useFinanceStore } from '@/stores/finance'
import axios from 'axios'
// 찜하기가 나올지 찜취소가 나올지 설정

const liked = ref(false)
const store = useFinanceStore()
const props = defineProps({
  finance: {
      type: Object,
      required: true,
  },
  kind: {
    type: String,
    required: true,
  }
})

// 찜하기 버튼이 나올지 찜취소 버튼이 나올지 설정을 위해 처음에 이게 user의 db안에 들어가있는지 받아온다.
onMounted(() => {
  if (store.token) {
    axios({
      method: 'get',
      // 수정필요
      url: `${store.API_URL}/${props.kind}check/${props.finance['base_product_id']}/`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    }).then((respoonse) => {
      if (respoonse.data.liked === false) {
        liked.value = false
      } else {
        liked.value = true
      }
    }).catch((error) => {
      console.log(error)
    })
  }
})

// 찜하기, 찜취소 버튼을 눌렀을때 django에 db를 보내고 그결과를 리턴받는다.
const checkLiked = function () {
   axios({
    method: 'post',
    url: `${store.API_URL}/${props.kind}${props.finance['base_product_id']}/`,
    headers: {
      Authorization: `Token ${store.token}`
     },
    data: {
      base_product_id : props.finance['base_product_id']
    }
   }).then((respoonse) => {
    console.log(respoonse.data['message'])
    if (respoonse.data.liked === false) {
      liked.value = false
    } else {
      liked.value = true
    }

  }).catch((error) => {
    console.log(error)
  })
} 

</script>

<style>
.popup {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  background: transparent; /* 배경을 투명하게 설정 */
  z-index: 1000; /* 팝업이 최상단에 오도록 설정 */
}

.popup-content {
  background: white;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  position: relative;
  width: 800px; /* 너비 설정 */
  height: 600px; /* 높이 설정 */
  max-width: 80%; /* 최대 너비 설정 */
  max-height: 80%; /* 최대 높이 설정 */
  border: 2px solid black; /* 검은 테두리 추가 */
}

.close {
  position: absolute;
  top: 0px;
  right: 10px;
  font-size: 50px; /* 폰트 크기 키우기 */
  cursor: pointer;
}
</style>