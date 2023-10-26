
<script >
import { ref, onMounted } from 'vue'
import { useRoute } from "vue-router";
import Navbar from '../components/Navbar.vue';
import RoleSkillService from '../../services/RoleSkill.js'
import StaffSkillsService from '../../services/StaffSkill.js'

export default {
    components: {
        Navbar
    },
    data() {
        const route = useRoute()
        var staffName = route.query.staffName
        var desc = route.query.desc
        var listingId = parseInt(route.query.listingId)
        var staffId = parseInt(route.query.staffId)
        var allstaffskills = []
        return {
            desc,
            route,
            staffName,
            listingId,
            staffId,
            skillMatch_list: [],
            overallMatch: 0.00,
            allstaffskills,
        }
    },
    mounted() {
        this.getOverallMatch()
    },
    methods: {
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
            this.allstaffskills = staffSkills;
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
        goBack(){
            this.$router.push({
                path: "/rolelistingdetails",
                query: { listingId: this.listingId },
            })
        }
    }


};

</script>


<template>
    <Navbar />
    <div class="container rounded py-4" style="outline: black 2px solid; min-height: 80vh;background-color: white; width:80%;">

        <div class="row" style="width: 100%;">
            <div class="col justify-content-start align-items-center" style="display: flex;">
                <svg class="ms-4 me-3" style="fill: black; align-items: left;" xmlns="http://www.w3.org/2000/svg"
                    height="1.5em" viewBox="0 0 448 512">
                    <path
                        d="M9.4 233.4c-12.5 12.5-12.5 32.8 0 45.3l160 160c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3L109.2 288 416 288c17.7 0 32-14.3 32-32s-14.3-32-32-32l-306.7 0L214.6 118.6c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0l-160 160z" />
                </svg>
                <button class="btn btn-light" @click="goBack()">Back</button>
            </div>
        </div>

        <h2 class="mt-3 px-3 pt-3" style="text-align: left;align-items:center">{{staffName}}
            <button class="btn btn-dark py-2 ms-3" disabled>{{ overallMatch }}% Match</button>
        </h2>

        <p class="px-3" style="text-align: left;">
            <span style="font-weight: bold;">Staff ID</span> : {{ staffId }}
        </p>

        <div class="mt-3 px-3" style="min-height: 50%; text-align: left;">
            <h6 style="font-style:italic;font-weight: bold;">Skills Match:</h6>

            <div v-if="skillMatch_list.length == 0">
                <button class="btn btn-warning px-2 py-1 w-100" disabled><span>There are no skills required for this role.</span></button>
            </div>

            <div class="row">
                <div v-for="skill in skillMatch_list" class="col-6 ">

                    <div v-if="skill.match == 100" class="mb-3">
                        <div class="d-flex justify-content-between">
                            <small>{{ skill.skill }}</small>
                            <small>Level {{ skill.proficiency }}</small>
                        </div>
                        <button class="btn btn-success px-2 py-1 w-100" disabled><span>100% Match</span></button>
                    </div>
    
                    <div v-else-if="skill.match == 0" class="mb-3">
                        <div class="d-flex justify-content-between">
                            <small>{{ skill.skill }}</small>
                            <small>Level {{ skill.proficiency }}</small>
                        </div>
                        <button class="btn btn-danger px-2 py-1 w-100" disabled><span>Applicant does not have this skill.</span></button>
                    </div>
    
                    <div v-else class="mb-3">
                        <div class="d-flex justify-content-between">
                            <small>{{ skill.skill }}</small>
                            <small>Level {{ skill.proficiency }}</small>
                        </div>
                        <button class="btn btn-warning px-2 py-1 w-100" disabled><span>{{ skill.match }}% Match</span></button>
                    </div>
                </div>
            </div>

        </div>

        <div class="p-3" style="width: 100%; height: 25%;text-align: left;">
            <h6 style="font-style:italic;font-weight: bold;">Applicant's Skills:</h6>
            <div v-for="skill in allstaffskills"><small>{{ skill.skill }}</small></div>
        </div>

        <div class="p-3" style="width: 100%; height: 25%;text-align: left;">
            <h6 style="font-style:italic;font-weight: bold;">Application Description:</h6>
            <p>{{ desc }}</p>
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