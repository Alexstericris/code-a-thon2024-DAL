import {createRouter, createWebHistory} from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from "@/views/LoginView.vue";
import ContractView from "@/views/ContractView.vue";
import AssetsView from "@/views/AssetsView.vue";
import AssetView from "@/views/AssetView.vue";
import InvoiceView from "@/views/InvoiceView.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'home',
            component: HomeView
        },
        {
            path: '/about',
            name: 'about',
            // route level code-splitting
            // this generates a separate chunk (About.[hash].js) for this route
            // which is lazy-loaded when the route is visited.
            component: () => import('../views/AboutView.vue')
        },
        {
            path: '/login',
            name: 'login',
            component: LoginView
        },
        {
            path: '/contracts/:contractId/view',
            name: 'viewContract',
            component: ContractView
        },
        {
            path: '/assets',
            name: 'AssesView',
            component: AssetsView
        },
        {
            path: '/assets/:assetId/view',
            name: 'viewAsset',
            component: AssetView
        },
        {
            path: '/invoices/:invoiceid/view',
            name: 'viewInvoice',
            component: InvoiceView
        },
    ]
})

export default router
