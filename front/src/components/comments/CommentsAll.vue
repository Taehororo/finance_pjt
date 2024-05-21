<template>
  <div>
    <hr>
    <p>댓글</p>
    <CommentCreate @comment-added="fetchComments" />
    <div v-for="comment in comments" :key="comment.id">
      <p>작성자: {{ comment.author }}</p>
      <p>내용: {{ comment.content }}</p>
      <button type="button" class="btn btn-primary ml-2" v-if="comment.author === store.userInfo['username']"
        @click="deleteComment(comment.id)">삭제하기</button>
      <hr>
    </div>
  </div>
</template>

<script setup>
import CommentCreate from '@/components/comments/CommentCreate.vue'
import axios from 'axios'
import { ref, defineProps } from 'vue'
import { useFinanceStore } from '@/stores/finance'

const store = useFinanceStore()
const props = defineProps({
  articleId: String
})

const comments = ref([])

const fetchComments = () => {
  axios({
    method: 'get',
    url: `${store.API_URL}/articles/articles/${props.articleId}/`
  }).then((response) => {
    comments.value = response.data.comments
  }).catch((error) => {
    console.log(error)
  })
}

fetchComments()

const deleteComment = (commentId) => {
  axios({
    method: 'delete',
    url: `${store.API_URL}/articles/comments/${commentId}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  }).then((response) => {
    fetchComments()
  }).catch((error) => {
    console.log(error)
  })
}
</script>

<style scoped></style>