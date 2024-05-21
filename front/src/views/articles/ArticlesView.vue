<template>
  <div class="container mt-4">
    <h1 class="text-center">게시판</h1>
    <div class="text-end mb-3">
      <button type="button" class="btn btn-outline-dark" @click="goWrite" v-if="store.write">글 쓰기</button>
    </div>
    <RouterView />
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { useFinanceStore } from '@/stores/finance'

const router = useRouter()
const store = useFinanceStore()

router.push({ name: 'articleall' })
store.write = true

const goWrite = () => {
  router.push({ name: 'articlecreate' })
  store.write = false
}
</script>

<style scoped>
.container {
  max-width: 800px;
}
</style>
