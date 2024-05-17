<template>
  <div>
    <div class="container">
      <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
          <a class="navbar-brand" href="#">Navbar</a>
        </div>
      </nav>
    </div>

    <div class="bg-info-subtle d-flex align-items-center justify-content-center" style="height: 100px;">
      <h2>예/적금 금리비교</h2>
    </div>

    <div class="container">
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
          <div>
            <nav class="navbar navbar-expand-lg">
              <div>
                <a class="navbar-brand fs-3" href="#">정기예금</a>
                <RouterLink :to="{ name: 'deposit' }" class="navbar-brand fs-3">정기예금</RouterLink>
                <span class="fs-3">|</span>
                <RouterLink :to="{ name: 'savings' }" class="navbar-brand fs-3 ps-3">정기적금</RouterLink>
                <a class="navbar-brand fs-3 ps-3" href="#">정기적금</a>
              </div>
            </nav>
          </div>
          <!-- <RouterView /> -->
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
                <tr v-for="finance in store.finances" :key="finance.base_product_id">
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
        </main>
      </div>
    </div>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import { useFinanceStore } from '@/stores/finance'
import { ref } from 'vue'
import axios from 'axios'

const store = useFinanceStore()
store.getDeposits()

const selectedText = ref('12개월')

const sendPeriod = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/deposit/products/`,
    data: {
      content: selectedText.value
    }
  }).then((response) => {
    store.changeFinances(response.data)
  }).catch((error) => {
    console.log(error)
  })
}

const setDropdownText = function (text) {
  selectedText.value = text
  sendPeriod()
}

const getInterestRate = function (options, period) {
  const option = options.find(opt => opt.save_trm === period)
  return option ? option.intr_rate2 : '-'
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