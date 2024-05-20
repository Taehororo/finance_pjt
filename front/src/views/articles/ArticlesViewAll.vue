<template>
    <div>
        <h1>전체 게시글</h1>
        <div v-for="article in allArticles">
					<p>작성자: {{ article.author }}</p>
					<p>제목: {{ article.title }}</p>
					<p>내용 :{{ article.content }}</p>
					<RouterLink :to="{ name: 'articledetail', params: { 'articleid': article.id} }">상세보기</RouterLink>
					<hr>
        </div>
    </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useFinanceStore } from '@/stores/finance'
const router = useRouter()
const store = useFinanceStore()
const allArticles = ref([])
axios({
  method: 'get',
  url: `${store.API_URL}/articles/`
}).then((response) => {
	allArticles.value = response.data
  console.log(response)
}).catch((error) => {
  console.log(error)
})

// 게시글 상세보기로 각기

</script>

<style scoped>

</style>