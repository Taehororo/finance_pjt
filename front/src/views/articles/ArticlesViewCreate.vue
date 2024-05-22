<template>
  <div class="container mt-5">
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <div class="mb-3">
        <label for="title" class="form-label fw-bold">제목</label>
        <input type="text" id="title" class="form-control" v-model="title" />
      </div>
      <div class="mb-3">
        <label for="content" class="form-label">내용</label>
        <textarea id="content" class="form-control" rows="5" v-model="content"></textarea>
      </div>
      <button type="submit" class="btn btn-outline-primary">저장</button>
      <button type="button" class="btn btn-outline-secondary ml-2" @click="cancleWrite">작성 취소</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'
import { useFinanceStore } from '@/stores/finance'

const router = useRouter()
const store = useFinanceStore()
const title = ref('')
const content = ref('')

const createArticle = () => {
  axios.post(`${store.API_URL}/articles/articles/`, {
    title: title.value,
    content: content.value
  }, {
    headers: { Authorization: `Token ${store.token}` }
  })
    .then(response => {
      console.log(response)
      store.write = true
      router.replace({ name: 'articleall' })
    })
    .catch(error => {
      console.error(error)
    })
}

const cancleWrite = () => {
  store.write = true
  router.replace({ name: 'articleall' })
}
</script>

<style scoped>
.container {
  max-width: 600px;
}
</style>
