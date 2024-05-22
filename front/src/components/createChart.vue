<template>
  <div class="chart-container">
    <Line :data="data" :options="options" />
  </div>
</template>

<script setup lang="ts">
import { reactive, defineProps } from 'vue'
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js'
import { Line } from 'vue-chartjs'
const props = defineProps({
  
})

// Chart.js에 사용할 모듈들을 등록합니다.
ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

const data = reactive({
  labels: ['1','2','3','4','5','6','7'],
  datasets: [
    {
      label: '입력 통화 환율 추이',
      backgroundColor: '#f87979',
      borderColor: '#f87979',
      data: [40, 20, 12, 39, 10, 40, 39]
    }
  ]
});

const options = reactive({
  responsive: true,
  maintainAspectRatio: false
});
</script>

<style scoped>
.chart-container {
  position: relative;
  margin: auto;
  height: 300px;
  /* 변경된 높이 */
  width: 400px;
  /* 변경된 너비 */
}
</style>