<script>
import Navbar from "../components/navbar.vue";
import { ref, watch, computed } from "vue";
import { useRoute } from "vue-router";
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
        const route = useRoute();
        const roleName = ref(0);
        const openW = ref();
        const closeW = ref();
        const roleDesc = ref();
        const selectedRoleDesc = ref();
        const country = ref();
        const dept = ref();
        const reportingManager = ref(0);
        const managers = ref();
        const skills = ref();

        const searchText = ref("");
        const isOpen = ref(false);
        const selectedOption = ref(null);

        const fetchRoleDesc = async () => {
            try {
                const response = await roleService.getRoleDesc(roleName.value);
                selectedRoleDesc.value = response.data.Role_Desc;
            } catch (error) {
                console.error("Error fetching roleDesc:", error);
            }
        };

        const fetchRoleSkill = async () => {
            try {
                const response = await skillService.getSkillsForRole(
                    roleName.value
                );
                skills.value = response.data;
            } catch (error) {
                console.error("Error fetching role skills:", error);
            }
        };

        watch(roleName, fetchRoleDesc);
        watch(roleName, fetchRoleSkill);

        roleListingService
            .getRoleListingById(route.params.listing_id)
            .then((response) => {
                roleListing.value = response.data[0];
                console.log(roleListing.value);
                roleName.value = roleListing.value.name;
                country.value = roleListing.value.country;
                dept.value = roleListing.value.dept;
                reportingManager.value = roleListing.value.reportingManager;

                const startD = new Date(roleListing.value.OpenW);
                const endD = new Date(roleListing.value.CloseW);
                openW.value = startD.toISOString().slice(0, 10); // Convert to "YYYY-MM-DD" format
                closeW.value = endD.toISOString().slice(0, 10); // Convert to "YYYY-MM-DD" format

                console.log(openW.value);
                console.log(closeW.value);
            });

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


        const sendRequest = async () => {
            const requestBody = {
                roleName: roleName.value,
                country: country.value,
                dept: dept.value,
                reportingManager: reportingManager.value,
                openWindow: openW.value,
                closeWindow: closeW.value,
            };

            try {
                const response = await axios.post(
                    "http://localhost:8000/addrolelisting/"
                );
                console.log("Response:", response.data);
                alert("Listing successfully added!");

            } catch (error) {
                console.error("Error:", error);
            }
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
    },
};
</script>

<template>
    <div>
        <div>
            <div class="container">
                <div class="row">
                    <label for="role_name" class="mt-5">Role Name:</label>
                </div>

                <v-select :options="roles" label="roleName" track-by="roleName" v-model="roleName"
                    :reduce="(option) => option.roleName" :clearable="false"></v-select>

                <div class="row">
                    <label for="reporting_manager">Reporting Manager:</label>
                </div>

                <v-select v-model="reportingManager" :options="managers" label="staffFName"
                    :reduce="(option) => option.staffID" :clearable="false"></v-select>

                <div class="row">
                    <label for="country">Country:</label>
                </div>
                <v-select v-model="country" :options="countries" label="country" :clearable="false"></v-select>

                <div class="row">
                    <label for="dept">Department:</label>
                    <input type="text" id="dept" name="dept" v-model="dept" />
                </div>

                <div class="row">
                    <label for="datePicker">Open Window:</label>
                    <input type="date" id="datePicker" name="datePicker" v-model="openW" />
                </div>

                <div class="row">
                    <label for="datePicker">Close Window:</label>
                    <input type="date" id="datePicker" name="datePicker" v-model="closeW" />
                </div>

                <div class="row">
                    <label for="roleDesc">Role Description:</label>
                    <div id="roleDesc">{{ selectedRoleDesc }}</div>
                </div>

                <div class="row">
                    <label for="roleDesc">Skills Required:</label>
                </div>

                <span class="badge text-bg-primary" v-for="skill in skills">{{
                    skill.Skill_Name
                }}</span>

                <button @click="sendRequest">Add Role Listing</button>
            </div>
        </div>
    </div>
</template>

<style></style>
