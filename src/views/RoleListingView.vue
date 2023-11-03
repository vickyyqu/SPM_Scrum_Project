<script>
import { ref, onMounted, watch } from "vue";
import { useRoute } from "vue-router";
import Navbar from "../components/navbar.vue";
import roleListingService from "../../services/RoleListing.js";
import countryService from "../../services/Country.js";
import departmentService from "../../services/Department.js";
import skillService from "../../services/Skill.js";
import router from "../main";

export default {
    components: {
        Navbar,
    },
    
    data() {
        const route = useRoute()
        var listingId = route.query.listingId
        var role_name = ""
        var role_desc = ""
        var role = {}
        return {
            role,
            role_name,
            role_desc,
            route,
            listingId,
            staffId: 1,
            skillMatch_list: [],
            overallMatch: 0.00,
            myRole: ""
        }
    },
    mounted() {
        this.myRole = sessionStorage.getItem("myRole")
    },
    methods: {
        editListing(id){
            this.$router.push("/updaterolelisting/" + id)
        }
        
    },

    setup() {
        const roleListings = ref([]);
        // const route = useRoute();

        roleListingService.getAllRoleListings().then((response) => {
            roleListings.value = response.data;
        });
        function viewDetails(id) {
            router.push({
                path: "/rolelistingdetails",
                query: { listingId: id },
            });
        };


        return {
            roleListings,
            viewDetails
        };
    },
};
</script>

<template>
    <Navbar />
    <div class="container-fluid" style="width: 80%;">
        <div class="row">
            <div
                v-if="roleListings.length > 0"
                class="col-12 col-md-6 g-3"
                v-for="listing in roleListings"
            >
                <div class="card mx-auto rounded">

                    <div class="card-body" 
                    @click="viewDetails(listing['id'])"
                    style="cursor: pointer;">

                        <h5 class="card-title">
                            {{ listing["name"] }}
                        </h5>
                        <h6
                            class="card-subtitle mb-2 text-body-secondary"
                        >
                            {{ listing["dept"] }}
                        </h6>
                        <h6
                            class="card-subtitle mb-2 text-body-secondary"
                        >
                            {{ listing["country"] }}
                        </h6>
                        <small href="#" class="subtitle" style="font-size: 10px;">
                            {{ "Open From : " + listing["OpenW"].split(" ")[1] + " " + listing["OpenW"].split(" ")[2]+ " " + listing["OpenW"].split(" ")[3]  + " to " + listing["CloseW"].split(" ")[1] + " " + listing["CloseW"].split(" ")[2]+ " " + listing["CloseW"].split(" ")[3] }}
                        </small>
                        <h6 href="#" class="subtitle">
                            
                        </h6>
                    </div>

                    <!-- edit button -->
                    <button class="btn btn-light" @click="editListing(listing['id'])">Edit</button>
                    <!-- edit button -->

                </div>
            </div>
            <div v-else class="container mt-5">
                <h3>No role listings listed.</h3>
            </div>
        </div>
    </div>
</template>

<style>
.sidebar {
    font-size: small;
    text-align: left;
}
</style>
