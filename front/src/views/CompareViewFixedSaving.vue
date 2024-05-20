<template>
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
            <tr v-for="finance in store.finances2" 
            :key="finance.base_product_id" 
            @click="showPopup(finance)"
            @mouseover="highlightedID = finance.base_product_id"
            @mouseleave="highlightedID = null"
            :class="{ highlightedRow: highlightedID === finance.base_product_id }"
            >
              <!-- {{ finance.base_product_id }} -->
              <td :class="{ highlightedRow: highlightedID === finance.base_product_id }">{{ finance.kor_co_nm }}</td>
              <td :class="{ highlightedRow: highlightedID === finance.base_product_id }">{{ finance.fin_prdt_nm }}</td>
              <td :class="{ highlightedRow: highlightedID === finance.base_product_id, highlightedCell: selectedText === '1개월' }">{{ getInterestRate(finance.options, '1') }}</td>
              <td :class="{ highlightedRow: highlightedID === finance.base_product_id, highlightedCell: selectedText === '3개월' }">{{ getInterestRate(finance.options, '3') }}</td>
              <td :class="{ highlightedRow: highlightedID === finance.base_product_id, highlightedCell: selectedText === '6개월' }">{{ getInterestRate(finance.options, '6') }}</td>
              <td :class="{ highlightedRow: highlightedID === finance.base_product_id, highlightedCell: selectedText === '12개월' }">{{ getInterestRate(finance.options, '12') }}</td>
              <td :class="{ highlightedRow: highlightedID === finance.base_product_id, highlightedCell: selectedText === '24개월' }">{{ getInterestRate(finance.options, '24') }}</td>
              <td :class="{ highlightedRow: highlightedID === finance.base_product_id, highlightedCell: selectedText === '36개월' }">{{ getInterestRate(finance.options, '36') }}</td>
            </tr>
            <DepostiDetail v-if="finance" :finance="finance" :kind="kind" @close="finance = null" />
          </tbody>
      </table>
  </div>
</template>

<script setup>
import { ref, defineProps } from 'vue'
import { useFinanceStore } from '@/stores/finance'
import DepostiDetail from '@/components/DepositDetail.vue'
const store = useFinanceStore()

const highlightedID = ref(null)
const finance = ref(null)

// DepositDetail에서 찜하기 버튼을 위해 이게 무엇에 관한건지 알려주는 변수 추가
const kind = ref('saving/like_fixed/')

const showPopup = (item) => {
  finance.value = item
}

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

/* 행에 마우스가 올라갔을때의 색깔을 변경 */
.highlightedRow {
  background-color: rgba(9, 177, 189, 0.25);
  cursor: pointer; /* 마우스 포인터를 클릭 형태로 설정 */
}


</style>