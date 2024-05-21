<template>
  <div class="comment-create mb-3">
    <form @submit.prevent="createComment">
      <div class="mb-3">
        <label for="content" class="form-label">내용</label>
        <textarea id="content" class="form-control" rows="3" v-model="content"></textarea>
      </div>
      <button type="submit" class="btn btn-primary">저장</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRoute } from 'vue-router'
import { useFinanceStore } from '@/stores/finance'

const store = useFinanceStore()
const route = useRoute()

const content = ref('')
const emit = defineEmits(['comment-added'])

const createComment = () => {
  axios({
    method: 'post',
    url: `${store.API_URL}/articles/comments/`,
    headers: {
      Authorization: `Token ${store.token}`
    },
    data: {
      article: route.params.articleid,
      content: content.value
    }
  }).then((response) => {
    content.value = ''
    emit('comment-added')
  }).catch((error) => {
    console.log(error)
  })
}
</script>

<style scoped>
.comment-create {
  max-width: 600px;
  margin: 0 auto;
}
</style>