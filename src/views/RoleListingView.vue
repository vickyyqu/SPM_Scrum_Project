
<script >
import Navbar from '../components/navbar.vue';
import { ref, onMounted } from 'vue'
import { useRoute } from "vue-router";
import roleListingService from '../../services/RoleListing.js'
import router from '../main';

export default {
    setup() {
        const roleListings = ref([])
        const route = useRoute()
        var halfway = ref(0)

        roleListingService.getAllRoleListings().then(response => {
            roleListings.value = response.data
            console.log(roleListings.value)
            halfway.value = Math.ceil(roleListings.value.length / 2)
            console.log(halfway)
        })
        function viewDetails(roleName){
            router.push({path:"/rolelistingdetails", query:{ RoleName: roleName}})
        }


        return {
            roleListings,
            viewDetails,
            halfway
        }


    },


};

</script>


<template>
    <Navbar />
    <div class="container-fluid mt-5 pt-5" style="position: absolute;
 top: 0;
 right: 0;
 bottom: 0;
 left: 0;background-color: lightgray; outline: black 1px solid;">
        <div class="row">
            <div class="col-6">
                <div v-for="listing in roleListings.slice(0, halfway)" class="row mt-4"> 
                    <div class="card mx-auto rounded" style="width: 25rem;" @click="viewDetails(listing['name'])">
                        <div class="card-body">
                            <h5 class="card-title">{{listing['name']}}</h5>
                            <h6 class="card-subtitle mb-2 text-body-secondary">{{ listing['dept'] }}</h6>
                            <h6 href="#" class="subtitle">{{ listing['OpenW'] }}</h6>
                            <h6 href="#" class="subtitle">{{ listing['CloseW'] }}</h6>
                        </div>
                    </div>
                </div>
            </div>

            <div class="col-6">
                <div v-for="listing2 in roleListings.slice(halfway, roleListings.size)" class="row mt-4"> 
                    <div class="card mx-auto rounded" style="width: 25rem;">
                        <div class="card-body">
                            <h5 class="card-title">{{ listing2['name'] }}</h5>
                            <h6 class="card-subtitle mb-2 text-body-secondary">{{ listing2['dept'] }}</h6>
                            <h6 href="#" class="subtitle">{{ listing2['OpenW'] }}</h6>
                            <h6 href="#" class="subtitle">{{ listing2['CloseW'] }}</h6>
                        </div>
                    </div>
                </div> 
            </div>

        </div>
    </div>
</template>

<style>

body {
  margin: 0;
  display: flex;
  place-items: center;
  min-width: 320px;
  min-height: 100vh;
}

</style>

