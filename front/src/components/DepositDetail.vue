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
    </div>
  </div>
</template>

<script setup>
import { defineProps } from 'vue'
import { useFinanceStore } from '@/stores/finance'
const store = useFinanceStore()
const props = defineProps({
  finance: {
      type: Object,
      required: true,
  }
})
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