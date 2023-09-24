
<script >
import Navbar from '../components/navbar.vue';
import { ref, onMounted } from 'vue'
import roleListingService from '../../services/RoleListing.js'

export default {
  setup() {
    const roleListings = ref([])

    roleListingService.getAllRoleListings().then(response=>{
        roleListings.value = response.data
        console.log(roleListings.value)
    })
    return{
        roleListings
    }
  },

  
};

</script>


<template>
    <Navbar />
    <div class="container-fluid mt-5 pt-5" 
    style="position: absolute;
 top: 0;
 right: 0;
 bottom: 0;
 left: 0;background-color: lightgray; outline: black 1px solid;">
        <div class="row">
            <div class="col-6">
                <div class="card mx-auto rounded" style="width: 25rem;">
                    <div class="card-body">
                        <h5 class="card-title">{{roleListings[0]['name']}}</h5>
                        <h6 class="card-subtitle mb-2 text-body-secondary">{{roleListings[0]['dept']}}</h6>
                        <h6 href="#" class="subtitle">{{roleListings[0]['OpenW']}}</h6>
                        <h6 href="#" class="subtitle">{{roleListings[0]['CloseW']}}</h6>
                    </div>
                </div>
            </div>

            <div class="col-6">
                <div class="card mx-auto rounded" style="width: 25rem;">
                    <div class="card-body">
                        <h5 class="card-title">{{roleListings[1]['name']}}</h5>
                        <h6 class="card-subtitle mb-2 text-body-secondary">{{roleListings[1]['dept']}}</h6>
                        <h6 href="#" class="subtitle">{{roleListings[1]['OpenW']}}</h6>
                        <h6 href="#" class="subtitle">{{roleListings[1]['CloseW']}}</h6>
                    </div>
                </div>
            </div>

        </div>
    </div>
</template>

<style>
</style>

