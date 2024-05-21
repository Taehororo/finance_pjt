<template>
  <div class="container mt-4">
    <div v-for="article in allArticles" :key="article.id" class="card mb-3">
      <div class="card-body">
        <h5 class="card-title">{{ article.title }}</h5>
        <h6 class="card-subtitle mb-2 text-muted">작성자: {{ article.author }}</h6>
        <RouterLink :to="{ name: 'articledetail', params: { articleid: article.id } }" class="btn btn-primary">상세보기
        </RouterLink>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useFinanceStore } from '@/stores/finance'

const store = useFinanceStore()
const allArticles = ref([])

const fetchArticles = () => {
  axios.get(`${store.API_URL}/articles/articles/`)
    .then(response => {
      allArticles.value = response.data
    })
    .catch(error => {
      console.error(error)
    })
}

onMounted(fetchArticles)
</script>

<style scoped>
.container {
  max-width: 800px;
}
</style>
