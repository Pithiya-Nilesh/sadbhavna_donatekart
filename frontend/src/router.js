import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/home',
    name: 'Home',
    component: () => import('@/pages/Home.vue'),
  },
]

let router = createRouter({
  history: createWebHistory('/'),
  routes,
})

export default router
