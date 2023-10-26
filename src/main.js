import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap'
import { createRouter, createWebHistory } from "vue-router";
import 'bootstrap-icons/font/bootstrap-icons';
import vSelect from 'vue-select'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes:[
        {
            path: '/', 
            name: 'homepage',
            component: () => import("./views/HomePage.vue")
        },
        {
            path: '/rolelistings', 
            name: 'roleListings',
            component: () => import("./views/RoleListingView.vue")
        },
        {
            path: '/rolelistingsstaff', 
            name: 'roleListingsStaff',
            component: () => import("./views/RoleListingStaffView.vue")
        },
        {
            path: '/addrolelisting',
            name: 'addRoleListing',
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
            path: '/rolelistingdetails', 
            name: 'roleListingdetails',
            component: () => import("./views/ViewRoleListingDetails.vue")
        },
        {
            path: '/viewapplication', 
            name: 'viewapplication',
            component: () => import("./views/ViewApplication.vue")
        }
    ]
});

export default router

const app = createApp(App)
app.component('v-select', vSelect)
app.use(router)
app.mount('#app')
