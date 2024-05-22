<template>
<div class="chart-container">
    <Line :data="chartData" :options="options"/>
  </div>
</template>

<script setup>
import { ref, defineProps, watch } from 'vue'
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
  kind: String,
  dates: Array,
  rates: Array,
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

const chartData = ref({
  labels: props.dates,
  datasets: [
    {
      label: `${props.kind} 통화 환율 추이`,
      backgroundColor: '#f87979',
      borderColor: '#f87979',
      data: props.rates
    }
  ]
});

const options = {
  responsive: true,
  maintainAspectRatio: false
}

// props의 변화를 감지하여 데이터 업데이트
watch(
  () => [props.dates, props.rates],
  ([newDates, newRates]) => {
    chartData.value.labels = newDates;
    chartData.value.datasets[0].data = newRates;
    console.log(props.rates)

  }
)

</script>

<style scoped>
.chart-container {
  position: relative;
  margin: auto;
  height: 300px;
  width: 400px;
}
</style>