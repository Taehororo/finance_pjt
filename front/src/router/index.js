import { createRouter, createWebHistory } from 'vue-router'
import MainPageView from '@/views/MainPageView.vue'
import ExchangeView from '@/views/ExchangeView.vue'
import NearBankView from '@/views/NearBankView.vue'
import SuggestionView from '@/views/SuggestionView.vue'
// 예/적금 금리비교 관련
import CompareView from '@/views/CompareView.vue'
import CompareViewDeposit from '@/views/CompareViewDeposit.vue'
import CompareViewFixedSaving from '@/views/CompareViewFixedSaving.vue'
import CompareViewFreeSaving from '@/views/CompareViewFreeSaving.vue'

// user 로그인 회원가입 관련
import LoginView from '@/views/users/LoginView.vue'
import SignUpView from '@/views/users/SignUpView.vue'

// user profile 화면
import ProfileView from '@/views/users/ProfileView.vue'

// 게시판
import ArticlesView from '@/views/articles/ArticlesView.vue'
import ArticlesViewCreate from '@/views/articles/ArticlesViewCreate.vue'
import ArticlesViewDetail from '@/views/articles/ArticlesViewdetail.vue'
import ArticlesViewUpdate from '@/views/articles/ArticlesViewUpdate.vue'
import ArticlesViewAll from '@/views/articles/ArticlesViewAll.vue'



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
        // 정기예금
        { path: 'deposit', name: 'deposit', component: CompareViewDeposit },
        // 정기적금
        { path: 'saving', name: 'saving', component: CompareViewFixedSaving },
        // 자유적금
        { path: 'freesaving', name: 'freesaving', component: CompareViewFreeSaving }
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
      component: LoginView
    },
    {
      path: '/signup',
      name: 'Signup',
      component: SignUpView
    },
    {
      path: '/profile/:userid',
      name: 'Profile',
      component: ProfileView
    },
    {
      path: '/articles',
      name: 'articles',
      component: ArticlesView,
      children: [
        {path: 'all', name: 'articleall', component: ArticlesViewAll },
        {path: 'create', name: 'articlecreate', component: ArticlesViewCreate },
        //  variable routing 필요 path 수정필요
        { path: 'detail/:articleid', name: 'articledetail', component: ArticlesViewDetail },
        {path: 'update/:articleid', name: 'articleupdate', component: ArticlesViewUpdate },
      ]
    }

    
  ]
})

export default router
