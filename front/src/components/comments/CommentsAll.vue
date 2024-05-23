<template>
  <div class="comments-section mt-4">
    <hr>
    <h5>댓글</h5>
    <CommentCreate @comment-added="fetchComments" />
    <div class="comment-list mt-3">
      <div v-for="comment in reversedComments" :key="comment.id" class="card mb-3">
        <div class="card-body">
          <h6 class="card-subtitle mb-2 text-info" v-if="comment.author === store.userInfo['username']">내 댓글</h6>
          <h6 class="card-title">작성자: {{ comment.author }}</h6>
          <p class="card-text">{{ comment.content }}</p>
          <button type="button" class="btn btn-sm btn-outline-danger" v-if="comment.author === store.userInfo['username']"
            @click="deleteComment(comment.id)">삭제하기</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import CommentCreate from '@/components/comments/CommentCreate.vue'
import axios from 'axios'
import { ref, defineProps, computed } from 'vue'
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

// comments 배열을 역순으로 반환하는 computed 속성
const reversedComments = computed(() => {
  return comments.value.slice().reverse()
})
</script>

<style scoped>
.comments-section {
  max-width: 600px;
  margin: 0 auto;
}

.comment-list .card {
  background-color: #f8f9fa;
}
</style>