<template>
  <div>
    <h1>게시판</h1>
    <button type="button" class="btn btn-outline-dark" @click="goWrite" v-if="store.write">글 쓰기</button>
  </div>
  <RouterView />
</template>




<script setup>

import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
const route = useRoute()
const router = useRouter()
import { useFinanceStore } from '@/stores/finance'
const store = useFinanceStore()


router.push({ name: 'articleall'})
store.write = true


const goWrite = function () {
  router.push({ name: 'articlecreate'})
  store.write= false
}
</script>

<style scoped>

</style>