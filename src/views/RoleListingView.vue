
<script >
import { ref, onMounted } from 'vue'
import { useRoute } from "vue-router";
import roleListingService from '../../services/RoleListing.js'
import router from '../main';

export default {
    setup() {
        const roleListings = ref([])
        const route = useRoute()

        roleListingService.getAllRoleListings().then(response => {
            roleListings.value = response.data
            console.log(roleListings.value)
        })
        function viewDetails(roleName){
            router.push({path:"/rolelistingdetails", query:{ RoleName: roleName}})
        }
        return {
            roleListings,
            viewDetails
        }
    },

};

</script>


<template>
    <div class="container-fluid" style="top: 0;right: 0;bottom: 0;left: 0;">
        <div class="row">
            <div v-for="each in roleListings" class="col-6">
                <div class="card mx-auto rounded" style="width: 25rem;" @click="viewDetails(each['name'])">
                    <div class="card-body">
                        <h5 class="card-title">{{each['name']}}</h5>
                        <h6 class="card-subtitle mb-2 text-body-secondary">{{ each['dept'] }}</h6>
                        <h6 href="#" class="subtitle">{{ each['OpenW'] }}</h6>
                        <h6 href="#" class="subtitle">{{ each['CloseW'] }}</h6>
                    </div>
                </div>
            </div>

            <div v-if="roleListings.length==0">
                <h6>There are currently no role listings open.</h6>
            </div>

        </div>
    </div>
</template>

<style></style>

