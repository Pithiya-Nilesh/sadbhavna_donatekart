import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/home',
    name: 'Home',
    component: () => import('@/pages/Home.vue'),
  },
  {
    path: '/sadbhavna/login',
    name: 'Login',
    component: () => import('@/pages/auth/Login.vue'),
  },
  {
    path: '/sadbhavna/campaign-donation/:name',
    name: 'CampaignDonation',
    component: () => import('@/pages/CampaignDonationPage.vue')
  },
  {
    path: '/sadbhavna/donate/:name',
    name: 'Donate',
    component: () => import('@/pages/Donate.vue')
  }
]

let router = createRouter({
  history: createWebHistory('/'),
  routes,
})

export default router
