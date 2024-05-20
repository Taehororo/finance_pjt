<template>
  <div>
    {{ userid }}
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const userid = ref(route.params.userid)
</script>

<style scoped>

</style>