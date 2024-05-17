<template>
   <div class="table-responsive">
              <table class="table">
              <!-- <table class="table table-striped table-sm"> -->
                <thead>
                  <tr>
                    <th>금융회사명</th>
                    <th>상품명</th>
                    <th :class="{ highlightedHeader: selectedText === '1개월' }">1개월</th>
                    <th :class="{ highlightedHeader: selectedText === '3개월' }">3개월</th>
                    <th :class="{ highlightedHeader: selectedText === '6개월' }">6개월</th>
                    <th :class="{ highlightedHeader: selectedText === '12개월' }">12개월</th>
                    <th :class="{ highlightedHeader: selectedText === '24개월' }">24개월</th>
                    <th :class="{ highlightedHeader: selectedText === '36개월' }">36개월</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="finance in store.finances" :key="finance.base_product_id">
                    <td>{{ finance.kor_co_nm }}</td>
                    <td>{{ finance.fin_prdt_nm }}</td>
                    <!-- 1개월 -->
                    <td :class="{ highlightedCell: selectedText === '1개월' }" v-if="finance.options[0]">{{ finance.options[0]['intr_rate2']}}</td>
                    <td v-else :class="{ highlightedCell: selectedText === '1개월' }">-</td>
                    <!-- 3개월 -->
                    <td :class="{ highlightedCell: selectedText === '3개월' }" v-if="finance.options[1]">{{ finance.options[1]['intr_rate2']}}</td>
                    <td v-else :class="{ highlightedCell: selectedText === '3개월' }">-</td>
                    <!-- 6개월 -->
                    <td :class="{ highlightedCell: selectedText === '6개월' }" v-if="finance.options[2]">{{ finance.options[2]['intr_rate2']}}</td>
                    <td v-else :class="{ highlightedCell: selectedText === '6개월' }">-</td>
                    <!-- 12개월 -->
                    <td :class="{ highlightedCell: selectedText === '12개월' }" v-if="finance.options[3]">{{ finance.options[3]['intr_rate2']}}</td>
                    <td v-else :class="{ highlightedCell: selectedText === '12개월' }">-</td>
                    <!-- 24개월 -->
                    <td :class="{ highlightedCell: selectedText === '24개월' }" v-if="finance.options[4]">{{ finance.options[4]['intr_rate2']}}</td>
                    <td v-else :class="{ highlightedCell: selectedText === '24개월' }">-</td>
                    <!-- 36개월 -->
                    <td :class="{ highlightedCell: selectedText === '36개월' }" v-if="finance.options[5]">{{ finance.options[5]['intr_rate2']}}</td>
                    <td v-else :class="{ highlightedCell: selectedText === '36개월' }">-</td>
                  </tr>
                </tbody>
              </table>
            </div>
</template>

<script setup>
import { ref } from 'vue'
import { useFinanceStore } from '@/stores/finance'
const store = useFinanceStore()
const selectedText = ref('12개월')

</script>

<style scoped>
.highlightedHeader {
  background-color: rgba(0, 238, 255, 0.1);

}
.highlightedCell {
  background-color: rgba(0, 238, 255, 0.1);
  
}
</style>