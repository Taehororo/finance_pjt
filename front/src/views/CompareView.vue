<template>
  <div>
    <h1>예/적금 금리비교</h1>
    <div>

    </div>
  </div>


  <head>
    <title>예/적금 금리비교</title>
  </head>

  <body>
    <div class="container-fluid">
      <div class="row">
        <nav class="col-md-2 d-none d-md-block bg-light sidebar">
          <div class="sidebar-sticky">
            <ul class="nav flex-column">
              <div class="container mt-5">
                <div class="dropdown">
                  정렬기준
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

              <li class="nav-item">
                <a class="nav-link" href="#">
                  <span data-feather="file"></span>
                  Orders
                </a>
              </li>

              <li class="nav-item">
                <a class="nav-link" href="#">
                  <span data-feather="shopping-cart"></span>
                  Products
                </a>
              </li>

              <li class="nav-item">
                <a class="nav-link" href="#">
                  <span data-feather="users"></span>
                  Customers
                </a>
              </li>

              <li class="nav-item">
                <a class="nav-link" href="#">
                  <span data-feather="bar-chart-2"></span>
                  Reports
                </a>
              </li>
              
              <li class="nav-item">
                <a class="nav-link" href="#">
                  <span data-feather="layers"></span>
                  Integrations
                </a>
              </li>
            </ul>

            <h6 class="sidebar-heading d-flex justify-content-between align-items-center px-3 mt-4 mb-1 text-muted">
              <span>Saved reports</span>
              <a class="d-flex align-items-center text-muted" href="#">
                <span data-feather="plus-circle"></span>
              </a>
            </h6>
            <ul class="nav flex-column mb-2">
              <li class="nav-item">
                <a class="nav-link" href="#">
                  <span data-feather="file-text"></span>
                  Current month
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">
                  <span data-feather="file-text"></span>
                  Last quarter
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">
                  <span data-feather="file-text"></span>
                  Social engagement
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">
                  <span data-feather="file-text"></span>
                  Year-end sale
                </a>
              </li>
            </ul>
          </div>
        </nav>

        <main role="main" class="col-md-9 ml-sm-auto col-lg-10 pt-3 px-4">
          <h2>정기예금</h2>
          <div class="table-responsive">
            <table class="table table-striped table-sm">
              <thead>
                <tr>
                  <th>금융회사명</th>
                  <th>상품명</th>
                  <th>1개월</th>
                  <th>3개월</th>
                  <th>6개월</th>
                  <th>12개월</th>
                  <th>24개월</th>
                  <th>36개월</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="finance in store.finances" :key="finance.base_product_id">
                  <td>{{ finance.kor_co_nm }}</td>
                  <td>{{ finance.fin_prdt_nm }}</td>
                  <!-- 1개월 -->
                  <td v-if="finance.options[0]">{{ finance.options[0]['intr_rate2']}}</td>
                  <td v-else>-</td>
                  <!-- 3개월 -->
                  <td v-if="finance.options[1]">{{ finance.options[1]['intr_rate2']}}</td>
                  <td v-else>-</td>
                  <!-- 6개월 -->
                  <td v-if="finance.options[2]">{{ finance.options[2]['intr_rate2']}}</td>
                  <td v-else>-</td>
                  <!-- 12개월 -->
                  <td v-if="finance.options[3]">{{ finance.options[3]['intr_rate2']}}</td>
                  <td v-else>-</td>
                  <!-- 24개월 -->
                  <td v-if="finance.options[4]">{{ finance.options[4]['intr_rate2']}}</td>
                  <td v-else>-</td>
                  <!-- 36개월 -->
                  <td v-if="finance.options[5]">{{ finance.options[5]['intr_rate2']}}</td>
                  <td v-else>-</td>
                  
                </tr>
              </tbody>
            </table>
          </div>
        </main>
      </div>
    </div>
    </body>
</template>

<script setup>
import { useFinanceStore } from '@/stores/finance'
import { ref } from 'vue'
import axios from 'axios'
const store = useFinanceStore() 
store.getDeposits()

// 이제 드랍다운 버튼에 따라 선택된 값을 django에 보내기
const sendPeriod = function () {
    axios({
      method: 'post',
      // 여기다가 너가 만든 view함수 url
      url: `${store.API_URL}/deposit/products/`,
      data: {
        content: selectedText.value
      }
    }).then((response) => {

    }).catch((error) => {

    })
  }


// 기본 예/적금 예치기간은 default가 전체기간
const selectedText = ref('12개월')
// 예/적금 예치기간 버튼을 위한 함수
const setDropdownText = function (text) {
  selectedText.value = text
  sendPeriod()
}


</script>

<style scoped>

</style>