<template>
  <h1>정기적금</h1>
  <div class="table-responsive">
      <table class="table">
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
            <tr v-for="finance in store.finances2" :key="finance.base_product_id">
              <td>{{ finance.kor_co_nm }}</td>
              <td>{{ finance.fin_prdt_nm }}</td>
              <td :class="{ highlightedCell: selectedText === '1개월' }">{{ getInterestRate(finance.options, '1') }}</td>
              <td :class="{ highlightedCell: selectedText === '3개월' }">{{ getInterestRate(finance.options, '3') }}</td>
              <td :class="{ highlightedCell: selectedText === '6개월' }">{{ getInterestRate(finance.options, '6') }}</td>
              <td :class="{ highlightedCell: selectedText === '12개월' }">{{ getInterestRate(finance.options, '12') }}</td>
              <td :class="{ highlightedCell: selectedText === '24개월' }">{{ getInterestRate(finance.options, '24') }}</td>
              <td :class="{ highlightedCell: selectedText === '36개월' }">{{ getInterestRate(finance.options, '36') }}</td>
            </tr>
          </tbody>
      </table>
  </div>
</template>

<script setup>
import { ref, defineProps } from 'vue'
import { useFinanceStore } from '@/stores/finance'
const store = useFinanceStore()

const getInterestRate = function (options, period) {
  const option = options.find(opt => opt.save_trm === period)
  return option ? option.intr_rate2 : '-'
}

defineProps({
  selectedText: String
})
</script>

<style scoped>
.highlightedHeader {
  background-color: rgba(0, 238, 255, 0.1);

}
.highlightedCell {
  background-color: rgba(0, 238, 255, 0.1);
  
}

</style>