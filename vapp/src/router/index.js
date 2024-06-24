import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'view1',
    component: () => import('../views/IndexData1.vue')
  },
  {
    path: '/view2',
    name: 'view2',
    component: () => import('../views/IndexData2.vue')
  },
]

const router = new VueRouter({
  routes
})

export default router
