<template>
	<div class="container mt-5">
		<h3 class="fw-bold">상세페이지</h3>
		<div class="card mb-3">
			<div class="card-body">
				<h5 class="card-title">{{ article.title }}</h5>
				<h6 class="card-subtitle mb-2 text-muted">작성자: {{ article.author }}</h6>
				<p class="card-text">{{ article.content }}</p>
				<div class="btn-group" v-if="article.author === store.userInfo.username">
					<button type="button" class="btn btn-primary" @click="goUpdate">수정하기</button>
					<button type="button" class="btn btn-danger" @click="deleteArticle">삭제하기</button>
					<button type="button" class="btn btn-secondary" @click="goBack">뒤로가기</button>
				</div>
				<div v-else>
					<button type="button" class="btn btn-secondary" @click="goBack">뒤로가기</button>
				</div>

			</div>
		</div>
		<CommentsAll :articleId="articleId" />
	</div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'
import { useFinanceStore } from '@/stores/finance'
import CommentsAll from '@/components/comments/CommentsAll.vue'

const store = useFinanceStore()
const route = useRoute()
const router = useRouter()
const articleId = ref(route.params.articleid)
const article = ref({})

const fetchArticle = () => {
	axios.get(`${store.API_URL}/articles/articles/${articleId.value}/`)
		.then(response => {
			article.value = response.data
		})
		.catch(error => {
			console.error(error)
		})
}

fetchArticle()

const goBack = () => {
	store.write = true
	router.replace({ name: 'articleall' })
}

const goUpdate = () => {
	router.push({ name: 'articleupdate', params: { articleid: articleId.value } })
}

const deleteArticle = () => {
	axios.delete(`${store.API_URL}/articles/articles/${articleId.value}/`, {
		headers: { Authorization: `Token ${store.token}` }
	})
		.then(response => {
			router.replace({ name: 'articleall' })
		})
		.catch(error => {
			console.error(error)
		})
}
</script>

<style scoped>
.container {
	max-width: 800px;
}
</style>
