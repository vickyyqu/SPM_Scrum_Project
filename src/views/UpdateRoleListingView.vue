<script>
import Navbar from "../components/navbar.vue";
import { ref, watch, computed, onMounted } from "vue";
import { useRoute } from "vue-router";
import roleListingService from "../../services/RoleListing.js";
import roleService from "../../services/Role.js";
import staffService from "../../services/Staff.js";
import skillService from "../../services/Skill.js";
import axios from "axios";
import "vue-select/dist/vue-select.css";
import countryService from "../../services/Country.js";
import departmentService from "../../services/Department.js";

export default {
    setup() {
        const roleListing = ref();
        const roles = ref();
        const route = useRoute();
        const roleName = ref(0);
        const minDate = ref();
        const openW = ref();
        const closeW = ref();
        const currentDate = ref(new Date().toISOString().split("T")[0]);
        const roleDesc = ref();
        const selectedRoleDesc = ref();
        const country = ref();
        const dept = ref();
        const reportingManager = ref(0);
        const staff = ref();
        const skills = ref();
        const countries = countryService.getAllCountries();
        const departments = departmentService.getAllDepartments();

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
                minDate.value = startD.toISOString().slice(0, 10);
                openW.value = startD.toISOString().slice(0, 10); // Convert to "YYYY-MM-DD" format
                closeW.value = endD.toISOString().slice(0, 10); // Convert to "YYYY-MM-DD" format

                console.log(openW.value);
                console.log(closeW.value);
            });

        // staffService.getAllManagers().then((response) => {
        //     managers.value = response.data;
        //     console.log(managers.value);
        // });

        staffService.getAllStaffs().then((response) => {
            staff.value = response.data;
            console.log(staff.value);
        });

        roleService.getAllRoles().then((response) => {
            roles.value = response.data;
            console.log(roles.value);
        });

        const sendRequest = async () => {
            const requestBody = {
                roleName: roleName.value,
                country: country.value,
                dept: dept.value,
                reportingManager: reportingManager.value,
                openWindow: openW.value,
                closeWindow: closeW.value,
            };

            roleListingService
                .updateRoleListing(roleListing.value.id, requestBody)
                .then((response) => {
                    console.log("Response:", response.data);
                    alert("Listing successfully updated!");
                })
                .catch((error) => {
                    console.error("Error:", error);
                });
        };

        const handleDateChange = () => {
            const inputDate = openW.value;
            if(inputDate < currentDate.value){
                openW.value = minDate.value;
                alert("Please ensure that the open window is on or after today!")
            }
        };

        const handleCloseWChange = () => {
            const inputDate = closeW.value;
            if (inputDate <= openW.value) {
                closeW.value = openW.value;
                alert("Please ensure that the close window is later than open window!")
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
            staff,
            sendRequest,
            skills,
            handleDateChange,
            handleCloseWChange,
            countries,
            departments,
        };
    },
};
</script>

<template>
        <div>
            <div v-if="roleListing">
                <h1 class="text-start mt-5">Edit Listing</h1>

                <div class="text-start">
                    <div class="mb-3">
                        <label for="role_name" class="form-label fw-semibold"
                            >Role Name:</label
                        >
                        <v-select
                            :options="roles"
                            label="roleName"
                            track-by="roleName"
                            v-model="roleName"
                            :reduce="(option) => option.roleName"
                            :clearable="false"
                            class="custom-select rounded-1"
                        ></v-select>
                    </div>

                    <div class="row mb-3">
                        <div class="col">
                            <label for="country" class="form-label fw-semibold">Country:</label>
                        <v-select
                            v-model="country"
                            :options="countries"
                            label="country"
                            :clearable="false"
                            class="custom-select rounded-1"
                        ></v-select>
                        </div>
                        <div class="col">
                            <label for="dept" class="form-label fw-semibold">Department:</label>
                        <v-select
                            v-model="dept"
                            :options="departments"
                            label="department"
                            :clearable="false"
                            class="custom-select rounded-1"
                        ></v-select>
                        </div>
                        <div class="col">
                            <label for="reporting_manager" class="form-label fw-semibold"
                            >Reporting Manager:</label
                        >
                        <v-select
                            v-model="reportingManager"
                            :options="staff"
                            label="staffFName"
                            :reduce="(option) => option.staffID"
                            :clearable="false"
                            class="custom-select rounded-1"
                        >
                            <template
                                #selected-option="{ staffFName, staffLName }"
                            >
                                <div>{{ staffFName }} {{ staffLName }}</div>
                            </template>
                            <template #option="{ staffFName, staffLName }">
                                <div>{{ staffFName }} {{ staffLName }}</div>
                            </template></v-select
                        >
                        </div>

                    </div>

                    <div class="mb-3">
                        <label for="datePicker" class="form-label fw-semibold"
                            >Open Window:</label
                        >
                        <input
                            type="date"
                            id="datePicker"
                            name="datePicker"
                            v-model="openW"
                            @change="handleDateChange"
                            class="form-control"
                        />
                    </div>

                    <div class="mb-3">
                        <label for="datePicker" class="form-label fw-semibold"
                            >Close Window:</label
                        >
                        <input
                            type="date"
                            id="datePicker"
                            name="datePicker"
                            v-model="closeW"
                            @change="handleCloseWChange"
                            class="form-control"
                        />
                    </div>

                    <div class="mb-3">
                        <label for="roleDesc" class="form-label fw-semibold"
                            >Role Description:</label
                        >
                        <div id="roleDesc" class="bg-white p-3 rounded-3">
                            {{ selectedRoleDesc }}
                        </div>
                    </div>

                    <div class="mb-3 gap-2">
                        <label for="roleDesc" class="form-label fw-semibold"
                            >Required Skills:</label
                        >
                        <div>
                        <span
                            class="badge text-bg-primary me-2 mt-2"
                            v-for="skill in skills"
                            >{{ skill.Skill_Name }}</span
                        >
                        </div>
                    </div>

                    <button type="submit" @click="sendRequest" class="btn btn-warning fw-semibold">
                        Update Listing
                    </button>
                </div>

            </div>
            <div v-else>
                <div>Role Listing does not exist</div>
            </div>
        </div>
</template>

<style scoped>
.custom-select {
    background-color: white; 
}
</style>
