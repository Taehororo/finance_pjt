import { createRouter, createWebHistory } from 'vue-router'
import MainPageView from '@/views/MainPageView.vue'
import CompareView from '@/views/CompareView.vue'
import ExchangeView from '@/views/ExchangeView.vue'
import NearBankView from '@/views/NearBankView.vue'
import SuggestionView from '@/views/SuggestionView.vue'
import Login from '@/components/Login.vue'
import CompareViewDeposit from '@/views/CompareViewDeposit.vue'
import CompareViewSavings from '@/views/CompareViewSavings.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'MainPageView',
      component: MainPageView
    },
    {
      path: '/compare',
      name: 'CompareView',
      component: CompareView,
      // rediect를 넣어준 이유는 처음 화면에 들어갔을때 routerview에 기본적으로 화면을 띄워주기 위해
      redirect: '/compare/deposit',
      children: [
        { path: 'deposit', name: 'deposit', component: CompareViewDeposit },
        { path: 'savings', name: 'savings', component: CompareViewSavings }
      ]
    },
    {
      path: '/exchange',
      name: 'ExchangeView',
      component: ExchangeView
    },
    {
      path: '/nearbank',
      name: 'NearBankView',
      component: NearBankView
    },
    {
      path: '/suggestion',
      name: 'SuggestionView',
      component: SuggestionView
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    }
  ]
})

export default router
