<template>
    <div class="container mt-5">
      <h1>게시글 작성</h1>
      <form @submit.prevent="createArticle">
        <div class="mb-3">
          <label for="title" class="form-label">제목</label>
          <input
            type="text"
            id="title"
            class="form-control"
            v-model="title"
          />
        </div>
        <div class="mb-3">
          <label for="content" class="form-label">내용</label>
          <textarea
            id="content"
            class="form-control"
            rows="5"
            v-model="content"
          ></textarea>
        </div>
        <button type="submit" class="btn btn-primary">저장</button>
				<button type="button" class="btn btn-primary ml-2" @click="cancleWrite">작성취소</button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import axios from 'axios'
	import router from '@/router'
	import { useFinanceStore } from '@/stores/finance'
	const store = useFinanceStore()
  const title = ref('')
	const content = ref('')
  
	const createArticle = function () {
		axios({
			method: 'post',
			url: `${store.API_URL}/articles/`,
			headers: {
      Authorization: `Token ${store.token}`
    	},
			data : {
				title : title.value,
				content : content.value
			}
		}).then((response) => {
			console.log(response)
			store.write = true
			router.replace({ name:'articleall'})
		}).catch((error) => {
			console.log(error)
		})
	}
  
	const cancleWrite = function () {
		store.write = true
		router.replace({ name: 'articleall'})
	}

  </script>
  
  <style scoped>
  .container {
    max-width: 600px;
  }
  </style>