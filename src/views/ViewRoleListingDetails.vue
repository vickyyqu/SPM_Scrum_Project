
<script >
import { ref, onMounted } from 'vue'
import { useRoute } from "vue-router";
import Navbar from '../components/navbar.vue';
import roleListingService from '../../services/RoleListing.js'
import RoleSkillService from '../../services/RoleSkill.js'
import StaffSkillsService from '../../services/StaffSkill.js'
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
        var listingId = route.query.listingId
        var role_name = ""
        var role_desc = ""
        var role = {}
        var role_country = ""
        var role_dept = ""
        var applicationId = 0
        const applied = ref()

        return {
            role,
            role_country,
            role_dept,
            role_name,
            role_desc,
            route,
            listingId,
            staffId: 1,
            skillMatch_list: [],
            applications_list: [],
            overallMatch: 0.00,
            myRole: "",
            applied
        }
    },
    mounted() {
        this.myRole = sessionStorage.getItem("myRole")
        this.staffId = sessionStorage.getItem("staffId")
        this.getOverallMatch()
        this.getRoleDetails()
        this.getAppliedStatus()
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
                this.role = response.data[0]

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
        async getRoleSkill() {
            try {
                const response = await RoleSkillService.getRoleSkills(this.listingId)
                console.log(response.data)
                return response.data
            } catch (error) {
                console.log(error)
            }
        },
        async getStaffSkill() {
            try {
                this.staffId = sessionStorage.getItem("staffId")
                const response = await StaffSkillsService.getStaffSkills(this.staffId)
                console.log(response.data)
                return response.data
            } catch (error) {
                console.log(error)
            }
        },
        async getOverallMatch() {
            var roleSkills = await this.getRoleSkill()
            var staffSkills = await this.getStaffSkill()
            // var roleSkills = [{ "proficiency": 5, "skill": "Product Design and Development" }, { "proficiency": 2, "skill": "Programming and Coding" }, { "proficiency": 6, "skill": "Product Management" }]
            // var staffSkills = [{ "proficiency": 2, "isVisible": true, "skill": "Programming and Coding" }, { "proficiency": 4, "isVisible": true, "skill": "Product Management" }]
            
            if (staffSkills == null){
                staffSkills = []
            }
            if (roleSkills == null){
                roleSkills = []
            }

            var allSkills = []
            var count = 0
            this.overallMatch = 0
            this.skillMatch_list = []

            for (let i = 0; i < roleSkills.length; i++) {
                var rSkill = roleSkills[i].skill.toUpperCase()

                for (let j = 0; j < staffSkills.length; j++) {
                    var sSkill = staffSkills[j].skill.toUpperCase()

                    if (rSkill == sSkill && !allSkills.includes(rSkill)) {
                    // if (staffSkills[j].isVisible && rSkill == sSkill && !allSkills.includes(rSkill)) {
                        allSkills.push(rSkill)
                        var match = 100

                        if (roleSkills[i].proficiency > 0){
                            match = Math.min(staffSkills[j].proficiency / roleSkills[i].proficiency, 1) * 100
                        }
                        var out = {
                            "skill": roleSkills[i].skill,
                            "proficiency": roleSkills[i].proficiency,
                            "match": match.toFixed(0)
                        }
                        this.skillMatch_list.push(out)
                        this.overallMatch += match
                        count ++
                    }
                }
                if (!allSkills.includes(rSkill)) {
                    allSkills.push(rSkill)
                    var out = {
                        "skill": roleSkills[i].skill,
                        "proficiency": roleSkills[i].proficiency,
                        "match": 0
                    }
                    this.skillMatch_list.push(out)
                    count ++
                }
            }
            if (count > 0){
                this.overallMatch = this.overallMatch/count
            } else if (roleSkills.length  == 0){
                this.overallMatch = 100
            }
            this.overallMatch = this.overallMatch.toFixed(0)
        },

        async getAppliedStatus(){
            try {
                console.log(this.listingId)
                console.log(this.staffId)
                const response = await StaffApplicationService.getAppliedStatus(this.listingId, this.staffId)

                console.log(response)
                if(response.data['Application_ID'] == None){
                    applied = False
                }
                else{
                    applied = True
                }
                console.log(response.data)
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
            requestBody = {
                rolename: applicationId.value,
                country: listingId.value,
                dept: staffId.value,
                reportingManager: brief_description.value
            };

            try {
                const response = await axios.post(
                    "http://localhost:8000/apply_role" +
                        roleListing.value.id,
                    requestBody
                );
                console.log("Response:", response.data);
                alert("Listing successfully updated!");
            } catch (error) {
                console.error("Error:", error)
            }
        }
    }
};

</script>


<template>
    <Navbar />
    <div class="container rounded py-4" style="outline: black 2px solid; min-height: 80vh;background-color: white; width:80%;">

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
                <button class="btn btn-warning" v-if = "applied" disabled> Applied </button>
                <button class="btn btn-warning" v-if = "applied" @click = 'deleteRequest'>Cancel</button>
                <button class="btn btn-warning" v-else @click = 'sendRequest'>Apply for Role</button>
            </div>
        </div>

        <h2 class="mt-3 px-3 pt-3" style="text-align: left;align-items:center">{{role_name}}
            <button class="btn btn-dark py-2 ms-3" disabled>{{ overallMatch }}% Match</button>
        </h2>
        <br/>

        <p class="px-3" style="text-align: left;"><span style="font-weight: bold;">Department</span> : {{ role_dept }} <span class="ms-3" style="font-weight: bold;">Country</span> : {{ role_country }} </p>
        <br>

        <div class="mt-3 px-3" style="min-height: 50%; text-align: left;">
            <h6 style="font-style:italic;">Skills Required:</h6>

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
            <h6 style ="font-weight: bold;">Applications</h6>
            <ul class="list-group">
                <li v-for="application in applications_list" class="list-group-item">{{application.Staff_ID}} {{ application.Brief_Description }}</li>
            </ul>
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

