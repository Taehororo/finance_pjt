<template>
  <div class="container mt-4">
    <div v-for="article in reversedArticles" :key="article.id" class="card mb-4 shadow">
      <div class="card-body">
        <h6 class="card-subtitle mb-2 text-info" v-if="article.author=== store.userInfo.username">내 글</h6>
        <h5 class="card-title fw-bold">{{ article.title }}</h5>
        <h6 class="card-subtitle mb-2 text-muted text-end">작성자: {{ article.author }}</h6>     
        <RouterLink :to="{ name: 'articledetail', params: { articleid: article.id } }"
          class="btn btn-outline-primary float-end">상세보기</RouterLink>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import axios from 'axios'
import { useFinanceStore } from '@/stores/finance'

const store = useFinanceStore()
const allArticles = ref([])
const reversedArticles = ref([])

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

// allArticles 배열이 업데이트될 때마다 역순으로 정렬된 배열을 업데이트
watch(allArticles, (newValue) => {
  reversedArticles.value = newValue.slice().reverse()
})
</script>

<style scoped>
.container {
  max-width: 800px;
}

.card {
  transition: transform 0.3s ease;
}

.card:hover {
  transform: translateY(-5px);
}
</style>