<script>
import Navbar from "../components/navbar.vue";
import { ref, watch, computed } from "vue";
import roleListingService from "../../services/RoleListing.js";
import roleService from "../../services/Role.js";
import staffService from "../../services/Staff.js";
import skillService from "../../services/Skill.js";
import countryService from "../../services/Country.js";
import axios from "axios";
import "vue-select/dist/vue-select.css";

export default {
    setup() {
        const roleListing = ref();
        const roles = ref();
        const roleName = ref('');
        const openW = ref();
        const closeW = ref();
        const roleDesc = ref();
        const selectedRoleDesc = ref('');
        const country = ref();
        const dept = ref();
        const reportingManager = ref('');
        const managers = ref();
        const skills = ref();

        const startD = new Date();
        const endD = new Date();
        openW.value = startD.toISOString().slice(0, 10); // Convert to "YYYY-MM-DD" format
        closeW.value = endD.toISOString().slice(0, 10);

        staffService.getAllManagers().then((response) => {
            managers.value = response.data;
            console.log(managers.value);
        });

        roleService.getAllRoles().then((response) => {
            roles.value = response.data;
            console.log(roles.value);
        });


        const countries = countryService.getAllCountries()
        console.log(countries)

        watch(roleName, async () => {
            try {

                const response_roleDesc = await roleService.getRoleDesc(roleName.value.roleName);

                selectedRoleDesc.value = response_roleDesc.data.Role_Desc;
                console.log(response_roleDesc.data.Role_Desc)

                const response_skillProficiency = await skillService.getSkillsAndProficiencyLevelForRole(
                    roleName.value.roleName
                );

                skills.value = response_skillProficiency.data;
                console.log(response_roleDesc.data.Role_Desc)

            } catch (error) {
                answer.value = 'Error! Could not get skills and proficiency. ' + error
            }

        })

        const sendRequest = async () => {
            const requestBody = {
                roleName: roleName.value,
                country: country.value,
                dept: dept.value,
                reportingManager: reportingManager.value,
                openWindow: openW.value,
                closeWindow: closeW.value,
            };

            console.log(requestBody)
            roleListingService.addRoleListing(requestBody)
                .then((response) => {
                    console.log("Response:", response.data);
                    alert("Listing successfully added!");
                })
                .catch((error) => {
                    console.error("Error:", error);
                });
        };

        return {
            roleListing,
            roles,
            roleName,
            reportingManager,
            openW,
            closeW,
            roleDesc,
            selectedRoleDesc,
            country,
            dept,
            managers,
            sendRequest,
            skills,
            countries
        };
    }
}
</script>

<template>
    <div>
        <div>
            <div class="container">
                <div class="row">
                    <label for="role_name" class="mt-5 form-label">Role Name:</label>
                </div>

                <v-select :options="roles" label="roleName" track-by="roleName" v-model="roleName"
                    :clearable="false"></v-select>

                <div class="row">
                    <label for="reporting_manager" class="form-label">Reporting Manager:</label>
                </div>

                <v-select v-model="reportingManager" :options="managers" label="staffFName" :clearable="false"></v-select>

                <div class="row">
                    <label for="country" class="form-label">Country:</label>
                </div>
                
                <v-select v-model="country" :options="countries" label="country" :clearable="false"></v-select>

                <div class="row">
                    <label for="dept" class="form-label">Department:</label>
                    <input type="text" id="dept" name="dept" v-model="dept" class="form-control"/>
                </div>

                <div class="row">
                    <label for="datePicker" class="form-label">Open Window:</label>
                    <input type="date" id="datePicker" name="datePicker" v-model="openW" class="form-control"/>
                </div>

                <div class="row">
                    <label for="datePicker" class="form-label">Close Window:</label>
                    <input type="date" id="datePicker" name="datePicker" v-model="closeW" class="form-control" />
                </div>

                <div class="row">
                    <label for="roleDesc" class="form-label">Role Description:</label>
                    <div id="roleDesc">{{ selectedRoleDesc }}</div>
                </div>

                <div class="row">
                    <label for="roleDesc" class="form-label">Skills Required:</label>
                </div>

                <span class="badge text-bg-primary" v-for="skill in skills">
                    {{ skill.Skill_Name }}  <!-- - {{ skill.Proficiency_Level }} -->
                </span>

                <button @click="sendRequest">Add Role Listing</button>
            </div>
        </div>
    </div>
</template>

<style></style>
