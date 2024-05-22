<template>
	<div class="container mt-5">
		<h4 class="fw-bold">상세페이지</h4>
		<div class="card mb-3">
			<div class="card-body">
				<h4 class="card-title fw-bold">{{ article.title }}</h4>
				<h6 class="card-subtitle mb-2 text-muted text-end">작성자: {{ article.author }}</h6>
				<hr>
				<h4 class="card-text">{{ article.content }}</h4>
				<div class="d-flex justify-content-end" v-if="article.author === store.userInfo.username">
					<button type="button" class="btn btn-outline-primary me-2" @click="goUpdate">수정하기</button>
					<button type="button" class="btn btn-outline-danger me-2" @click="deleteArticle">삭제하기</button>
					<button type="button" class="btn btn-outline-secondary" @click="goBack">뒤로가기</button>
				</div>
				<div class="d-flex justify-content-end" v-else>
					<button type="button" class="btn btn-outline-secondary" @click="goBack">뒤로가기</button>
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
.card-subtitle {
	display: flex;
	justify-content: flex-end;
}
.btn-group {
	display: flex;
	justify-content: flex-end;
	margin-top: 10px;
}


</style>