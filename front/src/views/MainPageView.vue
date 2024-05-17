<template>



      <div class="row h-200 bg-info-subtle">
        <div class="col-md-7 d-flex align-items-center justify-content-center bg-light-gray">
          <div class="d-flex felx-row align-items-center mb-2">
            <h2 class="p-2">예금 적금을 알아볼까요?</h2>
            <button type="button" class="btn btn-outline-primary p-2" @click="goCompare">비교하러가기</button>
          </div>
        </div>
        <!-- <div class="col-md-4"></div> -->
        <div class="col-md-5 d-flex align-items-center justify-content-center">
          <img src="@/assets/images/tatemono_bank_money.png" class="img-fluid" alt="Sample Image">
        </div>
      </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()

const goCompare = function () {
  router.push({ name: 'CompareView' })
}
</script>

<style scoped>

  .image-container {
      position: relative;
      display: inline-block;
    }
    .text-overlay {
      position: absolute;
      top: 50%;
      left: 0;
      transform: translateY(-50%);
      color: white;
      padding: 10px;
    }
</style>