<template>
    <nav class="navbar fixed-top " style="background-color: #22277A;" >
        <div class="container-fluid" style="background-color: #22277A;">
        <a class="navbar-brand" href="#" style="color: white;">All - In - One</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNavbar" aria-controls="offcanvasNavbar" aria-label="Toggle navigation">
            <span><i class="bi bi-list" style="color: white;"></i></span>
        </button>
        <div class="offcanvas offcanvas-end" tabindex="-1" id="offcanvasNavbar" aria-labelledby="offcanvasNavbarLabel" >
            <div class="offcanvas-header">
            <h5 class="offcanvas-title" id="offcanvasNavbarLabel">{{ getRole() }}</h5>
            <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
            </div>
            <div class="offcanvas-body">
            <ul class="navbar-nav justify-content-end flex-grow-1 pe-3">
                <li class="nav-item" v-if="getRole().length==0">
                <a class="nav-link active" aria-current="page" href="/">Home</a>
                </li>

                <li class="nav-item" v-if="getRole()=='HR'">
                <a class="nav-link" href="/rolelistings">Role Listings</a>
                </li>

                <li class="nav-item" v-if="getRole()=='Staff'">
                <a class="nav-link" href="/rolelistingsstaff">Role Listings</a>
                </li>

                <li class="nav-item" v-if="getRole()=='HR'">
                    <a class="nav-link" href="/addrolelisting">Add Role Listing</a>
                </li>

                <li class="nav-item" v-if="getRole()=='HR'">
                    <a class="nav-link" href="/viewskills">View All Skills</a>
                </li>

                <li class="nav-item" v-if="getRole().length>0">
                    <a class="nav-link" href="/" @click="logOut()">Log Out</a>
                </li>

            </ul>
            </div>
        </div>
        </div>
    </nav>
</template>
<script>
export default {
    methods: {
        logOut(){
            sessionStorage.clear()
            window.location.href = `/`;
        },
        getRole(){
            if (sessionStorage.getItem("myRole") === null) {
                return ""
            } else {
                return sessionStorage.getItem("myRole")
            }
        }
    }
}
</script>