import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap'
import { createRouter, createWebHistory } from "vue-router";
import 'bootstrap-icons/font/bootstrap-icons';

const routes = [
    {
        path: '/rolelistings', 
        name: 'roleListings',
        component: () => import("./views/RoleListingView.vue")
    },
    {
        path: '/addrolelistings',
        name: 'addRoleListings',
        component: () => import('./views/AddRoleListingView.vue')
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes,
});

const app = createApp(App)
app.use(router)
app.mount('#app')

export default router
