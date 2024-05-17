<template>
  <div>
    <h1>예/적금 금리비교</h1>
  </div>
</template>

<script setup>
import { useFinanceStore } from '@/stores/finance'
const store = useFinanceStore()
store.getDeposits()
</script>

<style scoped>

</style>