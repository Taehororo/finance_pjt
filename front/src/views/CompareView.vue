<template>
  <div>
    
    <div class="bg-info-subtle d-flex align-items-center justify-content-center" style="height: 100px;">
      <h2>예/적금 금리비교</h2>
    </div>

    <body class="container">
      <div class="container-fluid">
        <div class="row">
          <nav class="col-md-2 d-none d-md-block bg-light sidebar">
            <div class="sidebar-sticky">
              <ul class="nav flex-column">
                <div class="container mt-5">
                  <div>
                    <b class="text-info fs-5">정기예금</b>
                    <p class="text-info text-opacity-50 fs-6 ps-1">정렬기준</p>
                    <hr class="border border-info border-3 opacity-50">
                  </div>
                  
                  <div class="dropdown">
                    <p class="m-0 text-primary text-opacity-25">예치기간</p>
                    <button
                      class="btn btn-primary dropdown-toggle"
                      type="button"
                      id="dropdownMenuButton"
                      data-bs-toggle="dropdown"
                      aria-expanded="false"
                    >
                      {{ selectedText }}
                    </button>
                    <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                      <li>
                        <a class="dropdown-item" href="#" @click="setDropdownText('1개월')">1개월</a>
                      </li>
                      <li>
                        <a class="dropdown-item" href="#" @click="setDropdownText('3개월')">3개월</a>
                      </li>
                      <li>
                        <a class="dropdown-item" href="#" @click="setDropdownText('6개월')">6개월</a>
                      </li>
                      <li>
                        <a class="dropdown-item" href="#" @click="setDropdownText('12개월')">12개월</a>
                      </li>
                      <li>
                        <a class="dropdown-item" href="#" @click="setDropdownText('24개월')">24개월</a>
                      </li>
                      <li>
                        <a class="dropdown-item" href="#" @click="setDropdownText('36개월')">36개월</a>
                      </li>
                    </ul>
                  </div>
                </div>

                <!-- Other nav items -->
              </ul>

              <!-- Sidebar content -->
            </div>
          </nav>

          <main role="main" class="col-md-9 ml-sm-auto col-lg-10 pt-3 px-4">
            <h2>정기예금</h2>
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
          </main>
        </div>
      </div>
    </body>
  </div>
</template>

<script setup>
import { useFinanceStore } from '@/stores/finance'
import { ref } from 'vue'
import axios from 'axios'

const store = useFinanceStore() 
store.getDeposits()

// 기본 예/적금 예치기간은 default가 전체기간
const selectedText = ref('12개월')

// 드랍다운 버튼에 따라 선택된 값을 django에 보내기
const sendPeriod = function () {
    axios({
      method: 'post',
      url: `${store.API_URL}/deposit/products/`,
      data: {
        content: selectedText.value
      }
    }).then((response) => {
      // Handle response
    }).catch((error) => {
      // Handle error
    })
}

// 예/적금 예치기간 버튼을 위한 함수
const setDropdownText = function (text) {
  selectedText.value = text
  sendPeriod()
}
</script>

<style scoped>
.highlightedHeader {
  background-color: rgba(0, 238, 255, 0.1);

}
.highlightedCell {
  background-color: rgba(0, 238, 255, 0.1);
  
}
</style>