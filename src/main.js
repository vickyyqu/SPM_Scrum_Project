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
    },
    {
        path: '/viewskills',
        name: 'viewskills',
        component: () => import('./views/ViewSkillsView.vue')
    },
    {
        path: '/updaterolelisting/:listing_id',
        name: 'updaterolelisting',
        component: () => import('./views/UpdateRoleListingView.vue')
    },
    {
        path: '/rolelistingdetails/:RoleName', 
        name: 'roleListingdetails',
        component: () => import("./views/ViewRoleListingDetails.vue")
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
