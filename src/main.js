import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap'

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

createApp(App).mount('#app')
