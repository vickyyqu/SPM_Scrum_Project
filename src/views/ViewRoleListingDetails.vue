
<script >
import { ref, onMounted } from 'vue'
import { useRoute } from "vue-router";
import Navbar from '../components/navbar.vue';
import roleListingService from '../../services/RoleListing.js'
import RoleSkillMatchService from '../../services/RoleSkillMatch.js'
import StaffApplicationService from '../../services/Application.js'
import RoleService from '../../services/Role'
import axios, { all } from 'axios';
import Role from '../../services/Role';
import RoleListing from '../../services/RoleListing.js';
import router from '../main';

export default {
    components: {
        Navbar
    },
    data() {
        const route = useRoute()
        const currentDate = new Date(new Date().getTime() + 8 * 60 * 60 * 1000).toISOString().slice(0, 10)
        var listingId = route.query.listingId
        var role_name = ""
        var role_desc = ""
        var role = {}
        var role_country = ""
        var role_dept = ""
        var open_window = ""
        var close_window = ""
        var reporting_manager = ""
        var brief_description = ""
        var applicationId = 0
        var status = ""
        

        return {
            currentDate,
            role,
            role_country,
            role_dept,
            role_name,
            role_desc,
            route,
            listingId,
            staffId: 1,
            open_window,
            close_window,
            reporting_manager,
            brief_description,
            skillMatch_list: [],
            applications_list: [],
            overallMatch: 0.00,
            myRole: "",
            status
        }
    },
    mounted() {
        this.myRole = sessionStorage.getItem("myRole")
        this.staffId = sessionStorage.getItem("staffId")
        this.getOverallMatch()
        // this.getRoleDetails()
        // this.getAppliedStatus()
        this.getRoleDetails()
        .then(() => {
            this.getAppliedStatus();
        })
        this.getApplicationsByListingID()
    },
    methods: {
        async getRoleDetails(){
            try {
                console.log(this.listingId)
                const response = await roleListingService.getRoleListingById(this.listingId)
                // console.log(response.data[0])
                // console.log(response.data[0]['name'])
                this.role_name = response.data[0]['name']
                this.role_country = response.data[0]['country']
                this.role_dept = response.data[0]['dept']
                this.open_window = new Date(response.data[0]['OpenW'])
                this.close_window = new Date(response.data[0]['CloseW']).toISOString().slice(0, 10)
                this.reporting_manager = response.data[0]['reportingManager']

                const response2 = await RoleService.getRoleDesc(this.role_name)
                this.role_desc = response2.data['Role_Desc']
                // console.log(this.role)
                // console.log(this.role_name)
                // const response = await RoleService.getRoleDesc(this.role_name)
                // this.role_desc = response.data['Role_Desc']
            }
            catch(error){
                console.log(error)
            }
        },
        async getOverallMatch() {

            try {
                const response = await RoleSkillMatchService.getRoleSkillMatch(this.listingId, this.staffId)
                console.log(response.data)
                
                this.overallMatch = response.data.overall_match
                this.skillMatch_list = response.data.roleskill_match
            } catch (error) {
                console.log(error)
            }
        },
        async getAppliedStatus(){
            try {
                console.log(this.listingId)
                console.log(this.staffId)
                const response = await StaffApplicationService.getAppliedStatus(this.listingId, this.staffId)

                console.log(response)
                if(this.close_window < this.currentDate){
                    this.status = 'closed'
                }
                else if(response.data == null){
                    this.status = 'unapplied'
                }
                else{
                    this.status = 'applied'
                }
                console.log(response.data)
                console.log(this.status)
            } catch (error) {
                console.log(error)
            }
        },

        async getApplicationsByListingID(){
            try {
                const response = await StaffApplicationService.getApplicationsByListingID(this.listingId)
                this.applications_list = response.data
                console.log(response.data)
                return response.data
            } catch (error) {
                console.log(error)
            }
        },

        goBack(){
            if (this.myRole == "Staff"){
                this.$router.push("/rolelistingsstaff")
            }
            else if (this.myRole == "HR"){
                this.$router.push("/rolelistings")
            }
        },

        editListing(){
            this.$router.push("/updaterolelisting/" + this.listingId)
        },

        async sendRequest(){
            if (this.brief_description == ""){
                alert("Please write in more about yourself")
            }
            else{
                var requestBody = {
                    listing_ID: this.listingId,
                    staff_ID: this.staffId,
                    brief_description: this.brief_description
                };

                try {
                    const response = await axios.post(
                        "http://localhost:8000/apply_role", requestBody
                    );
                    console.log("Response:", response.data);
                    alert("Successfully applied for role!");

                    window.location.reload()
                } catch (error) {
                    console.error("Error:", error)
                }
            }
        },

        async deleteRequest(){
            try {
                const response = await axios.delete(
                    "http://localhost:8000/delete_application/" + this.listingId + '&' + this.staffId
                );

                console.log("Response:", response.data);
                alert("Application has been withdrawn");
                window.location.reload()
            } catch (error) {
                console.error("Error:", error);
            };
        },
        viewApplication(application){
            this.$router.push({
                path: "/viewapplication",
                query: { 
                    staffName: application.staff_fname + " " + application.staff_lname,
                    staffId: application.staff_id,
                    listingId: application.listing_id,
                    desc: application.brief_description
                },
            });
        }
    }
};

</script>


<template>
    <Navbar />
    <div class="container rounded py-4" style="outline: black 2px solid; min-height: 80vh;background-color: white; width:90vh;">

        <div class="row" style="width: 100%;">
            <div class="col justify-content-start align-items-center" style="display: flex;">
                <svg  class="ms-4 me-3" style="fill: black; align-items: left;" xmlns="http://www.w3.org/2000/svg"
                    height="1.5em" viewBox="0 0 448 512" @click="goBack()">
                    <path
                        d="M9.4 233.4c-12.5 12.5-12.5 32.8 0 45.3l160 160c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3L109.2 288 416 288c17.7 0 32-14.3 32-32s-14.3-32-32-32l-306.7 0L214.6 118.6c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0l-160 160z" />
                </svg>
                <button class="btn btn-light" @click="goBack()">Back</button>
            </div>
            <div v-if="myRole=='HR'" class="col align-items-center justify-content-end" style="display: flex;">
                <svg class="mx-3" xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 512 512">
                    <path
                        d="M471.6 21.7c-21.9-21.9-57.3-21.9-79.2 0L362.3 51.7l97.9 97.9 30.1-30.1c21.9-21.9 21.9-57.3 0-79.2L471.6 21.7zm-299.2 220c-6.1 6.1-10.8 13.6-13.5 21.9l-29.6 88.8c-2.9 8.6-.6 18.1 5.8 24.6s15.9 8.7 24.6 5.8l88.8-29.6c8.2-2.7 15.7-7.4 21.9-13.5L437.7 172.3 339.7 74.3 172.4 241.7zM96 64C43 64 0 107 0 160V416c0 53 43 96 96 96H352c53 0 96-43 96-96V320c0-17.7-14.3-32-32-32s-32 14.3-32 32v96c0 17.7-14.3 32-32 32H96c-17.7 0-32-14.3-32-32V160c0-17.7 14.3-32 32-32h96c17.7 0 32-14.3 32-32s-14.3-32-32-32H96z" />
                </svg>
                <button class="btn btn-light" @click="editListing()">Edit</button>
            </div>
            <div v-else-if="myRole=='Staff'" class="col align-items-center justify-content-end" style="display: flex;">
                <button class="btn btn-secondary" v-if = "status=='closed'" disabled>Applications are closed</button>
                <button class="btn btn-warning me-3" v-if = "status=='applied'" disabled> Applied </button>
                <button class="btn btn-danger" v-if = "status=='applied'" @click = 'deleteRequest'>Cancel</button>
                <!-- Button trigger modal -->
                <button type="button" v-if = "status=='unapplied'" class="btn btn-warning" data-bs-toggle="modal" data-bs-target="#exampleModal">
                    Apply For Role
                </button>
                <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h1 class="modal-title fs-5" id="exampleModalLabel">Please state your reasons for applying:</h1>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                    <div class="modal-body">
                        <textarea v-model = "brief_description" class = 'form-control'></textarea>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-warning" @click = 'sendRequest'>Apply For Role</button>
                    </div>
                    </div>
                </div>
                </div>
            </div>
        </div>

        <h2 class="mt-3 px-3 pt-3" style="text-align: left;align-items:center">{{role_name}}
            <button v-if="myRole=='Staff'" class="btn btn-dark py-2 ms-3" disabled>{{ overallMatch }}% Match</button>
        </h2>

        <p class="px-3" style="text-align: left;">
            <span style="font-weight: bold;">Department</span> : {{ role_dept }} 
            <span class="ms-3" style="font-weight: bold;">Country</span> : {{ role_country }} 
            <span class="ms-3" style="font-weight: bold;">Reporting Manager</span> : {{ reporting_manager }}
            <br>
            <span style="font-weight: bold;">Closing Date</span> : {{ close_window }}
        </p>

        <br>

        <div class="px-3" style="min-height: 50%; text-align: left;">
            <h6 style="font-style:italic; font-weight: bold;">Skills Required:</h6>

            <div v-if="skillMatch_list.length == 0">
                <button class="btn btn-warning px-2 py-1 w-100" disabled><span>There are no skills required for this role.</span></button>
            </div>

            <div class="row">
                <div v-for="skill in skillMatch_list" class="col-6 ">

                    <div v-if="skill.match == 100 && myRole == 'Staff'" class="mb-3">
                        <div class="d-flex justify-content-between">
                            <small>{{ skill.skill }}</small>
                            <div v-if="myRole=='Staff'"><small>Level {{ skill.proficiency }}</small></div>
                        </div>
                        <div v-if="myRole=='Staff'"><button class="btn btn-success px-2 py-1 w-100" disabled><span>100% Match</span></button></div>
                    </div>
    
                    <div v-else-if="skill.match == 0 && myRole == 'Staff'" class="mb-3">
                        <div class="d-flex justify-content-between">
                            <small>{{ skill.skill }}</small>
                            <div v-if="myRole=='Staff'"><small>Level {{ skill.proficiency }}</small></div>
                        </div>
                        <div v-if="myRole=='Staff'"><button class="btn btn-danger px-2 py-1 w-100" disabled><span>You do not have this skill.</span></button></div>
                    </div>
    
                    <div v-else class="mb-3">
                        <div class="d-flex justify-content-between">
                            <small>{{ skill.skill }}</small>
                            <div v-if="myRole=='Staff'"><small>Level {{ skill.proficiency }}</small></div>
                        </div>
                        <div v-if="myRole=='Staff'"><button class="btn btn-warning px-2 py-1 w-100" disabled><span>{{ skill.match }}% Match</span></button></div>
                    </div>
                </div>
            </div>

        </div>

        <div class="mt-3 p-3" style="width: 100%; height: 25%;text-align: left;">
            <h6 style="font-style:italic; font-weight: bold;">Role Description:</h6>
            <p>{{ role_desc }}</p>
        </div>

        <div v-if="myRole=='HR'" class="mt-3 p-3" style="width: 100%; height: 25%;text-align: left;">
            <h6 style="font-style:italic; font-weight: bold;">Applications:</h6>
            <template v-if="applications_list.length > 0">
                <ul class="list-group">
                    <li v-for="application in applications_list" class="list-group-item p-2 d-flex justify-content-between">
                        {{ application.staff_fname }} {{ application.staff_lname }}
                        <button class="btn btn-outline-primary py-0 px-1 me-2" @click="viewApplication(application)"><small>View Application</small></button>
                    </li>
                </ul>
            </template>
            <template v-else>
                <p>There are currently no applications.</p>
            </template>

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

