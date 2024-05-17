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
                <RouterLink :to="{ name: 'deposit' }" class="navbar-brand fs-3">정기예금</RouterLink>
                <span class="fs-3">|</span>
                <RouterLink :to="{ name: 'savings' }" class="navbar-brand fs-3 ps-3">정기적금</RouterLink>
              </div>
            </nav>
          </div>
          <RouterView :selectedText="selectedText"/>
          
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