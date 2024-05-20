<template>
  <div class="container mt-5">
    <h1>게시글 수정</h1>
    <form @submit.prevent="updateArticle">
      <div class="mb-3">
        <label for="title" class="form-label">제목</label>
        <input
          type="text"
          id="title"
          class="form-control"
          v-model="article.title"
        />
      </div>
      <div class="mb-3">
        <label for="content" class="form-label">내용</label>
        <textarea
          id="content"
          class="form-control"
          rows="5"
          v-model="article.content"
        ></textarea>
      </div>
      <button type="submit" class="btn btn-primary">수정 완료</button>
      <button type="button" class="btn btn-secondary ml-2" @click="goBack">수정 취소</button>
    </form>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios';
import { useFinanceStore } from '@/stores/finance';

const store = useFinanceStore();
const route = useRoute();
const router = useRouter();
const articleId = ref(route.params.articleid);

const article = reactive({
  title: '',
  content: ''
});

const fetchArticle = async () => {
  try {
    const response = await axios.get(`${store.API_URL}/articles/${articleId.value}/`);
    article.title = response.data.title;
    article.content = response.data.content;
  } catch (error) {
    console.error(error);
  }
};

onMounted(fetchArticle);

const updateArticle = () => {
  axios({
    method: 'put',
    url: `${store.API_URL}/articles/${articleId.value}/`,
    headers: {
      Authorization: `Token ${store.token}`
    },
    data: {
      title: article.title,
      content: article.content
    }
  })
  .then((response) => {
    console.log(response);
    store.write = true;
    router.replace({ name: 'articleall' });
  })
  .catch((error) => {
    console.error(error);
  });
};

const goBack = () => {
  router.replace({ name: 'articledetail', params: { 'articleid': articleId.value } });
};
</script>

<style scoped>
.container {
  max-width: 600px;
}
</style>