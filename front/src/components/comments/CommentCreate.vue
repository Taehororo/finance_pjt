<template>
  <div>
    <form @submit.prevent="createComment">
      <div class="mb-3">
        <label for="content" class="form-label">내용</label>
        <input id="content" class="form-control" rows="5" v-model="content">
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
.container {
  max-width: 600px;
}
</style>