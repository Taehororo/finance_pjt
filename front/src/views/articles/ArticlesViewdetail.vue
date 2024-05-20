<template>
		<p>상세페이지</p>
    <div>
			<p>작성자 : {{ article.author }}</p>
			<p>제목 : {{ article.title }}</p>
			<p>내용 : {{ article.content }}</p>
			<button type="button" class="btn btn-primary ml-2" v-if="article.author === store.userInfo['username']" @click="goUpdate">수정하기</button>
			<!-- <RouterLink 
			:to="{name: 'articleupdate', params: {'articleid': articleId}}" 
			v-if="article.author === store.userInfo['username']"
			:article="article"
			>
				수정하기</RouterLink> -->
			<button type="button" class="btn btn-primary ml-2" v-if="article.author === store.userInfo['username']" @click="deleteArticle">삭제하기</button>
			<button type="button" class="btn btn-primary ml-2" @click="goBack">뒤로가기</button>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'
import { useFinanceStore } from '@/stores/finance'
const store = useFinanceStore()
const route = useRoute()
const router = useRouter()

// 현재 페이지의 아티클번호
const articleId = ref(route.params.articleid)

// 장고에서 페이지의 아티클 번호로 해당하는 아티클의 세부정보 받아오기
const article = ref({})
axios({
  method: 'get',
  url: `${store.API_URL}/articles/${articleId.value}/`
}).then((response) => {
	article.value = response.data
}).catch((error) => {
  console.log(error)
})

// 전체게시글로 돌아가기
const goBack = function () {
	store.write = true
	router.replace({ name: 'articleall'})
}

// 게시글 업데이트하러가기
const goUpdate = function () {
	router.push({name: 'articleupdate', params: {'articleid': articleId.value}})
}

// 게시글 삭제
const deleteArticle = function () {
	axios({
  method: 'delete',
  url: `${store.API_URL}/articles/${articleId.value}/`,
	headers: {
      Authorization: `Token ${store.token}`
  }
	}).then((response) => {
		router.replace({name: 'articleall'})
	}).catch((error) => {
		console.log(error)
	})
}
</script>

<style scoped>

</style>