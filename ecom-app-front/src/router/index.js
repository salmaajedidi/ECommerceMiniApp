import { createRouter, createWebHistory } from 'vue-router'
import ProductList from '../views/ProductView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'productList',
      component: ProductList,
    },
   
  ],
})

export default router
