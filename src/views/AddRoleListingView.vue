<script>
import { ref, watch, computed } from "vue";
import Navbar from '../components/Navbar.vue';
import roleListingService from "../../services/RoleListing.js";
import roleService from "../../services/Role.js";
import staffService from "../../services/Staff.js";
import skillService from "../../services/Skill.js";
import countryService from "../../services/Country.js";
import departmentService from "../../services/Department.js"
import "vue-select/dist/vue-select.css";

export default {
    components: {
        Navbar
    },
    setup() {
        const roleListing = ref();
        const roles = ref();
        const roleName = ref('');
        const openW = ref();
        const closeW = ref();
        const roleDesc = ref();
        const selectedRoleDesc = ref('');
        const country = ref('');
        const dept = ref('');
        const reportingManager = ref('');
        const staff = ref();
        const skills = ref();

        const minDate = ref();
        const currentDate = ref(new Date(new Date().getTime() + 8 * 60 * 60 * 1000).toISOString())//ref(new Date().toISOString().split('T')[0]);
        const startD = new Date(new Date().getTime() + 8 * 60 * 60 * 1000)
        const endD = new Date(new Date().getTime() + 8 * 60 * 60 * 1000)
        openW.value = startD.toISOString().slice(0, 10); // Convert to "YYYY-MM-DD" format
        closeW.value = endD.toISOString().slice(0, 10);

        // const departments = ref(); //departmentService.getAllDepartments();

        // staffService.getAllManagers().then((response) => {
        //     managers.value = response.data;
        // });
        staffService.getAllStaffs().then((response) => {
            staff.value = response.data;
        });

        roleService.getAllRoles().then((response) => {
            roles.value = response.data;
        });

        const departments = departmentService.getAllDepartments()

        const countries = countryService.getAllCountries()

        watch(roleName, async () => {
            try {

                const response_roleDesc = await roleService.getRoleDesc(roleName.value.roleName);

                selectedRoleDesc.value = response_roleDesc.data.Role_Desc;

                const response_skillProficiency = await skillService.getSkillsAndProficiencyLevelForRole(
                    roleName.value.roleName
                );

                skills.value = response_skillProficiency.data;

            } catch (error) {
                answer.value = 'Error! Could not get skills and proficiency. ' + error
            }

        })

        const sendRequest = async () => {
            console.log(country.value)
            if (String(roleName.value).trim() == "" || String(country.value).trim() == "" || String(dept.value).trim() == "" || String(reportingManager.value).trim() == "" || String(openW.value).trim() == "" || String(closeW.value).trim() == "") {
                alert("Please ensure that all fields are filled in!");
            }
            else if (openW.value > closeW.value) {
                alert("Please ensure that the close window is after the open window!");
            
            } else {

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
                        window.location.href = `/rolelistings`;
                        alert("Listing successfully added!");
                        console.log(response);
                    })
                    .catch((error) => {
                        console.error("Error:", error);
                    });
            }
        };

        minDate.value = startD.toISOString().slice(0, 10);
        function handleDateChange() {
            const inputDate = openW.value;
            if (inputDate < minDate.value) {
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
            countries,
            departments,
            handleDateChange,
            handleCloseWChange,
        };
    }
}


</script>

<template>
    <Navbar />
    <div class="container-fluid" style="width: 80%">
        <div class="row">
            <div class="col">
                <h2 class="text-start">Add Listing</h2>
            </div>
        </div>
        <div class="text-start">
            <div class="row mb-3">
                <div class="col">
                    <label for="role_name" class="form-label fw-semibold">Role Name:</label>
                    <v-select :options="roles" label="roleName" track-by="roleName" v-model="roleName" :clearable="false"
                        class="custom-select rounded-1"></v-select>
                </div>
            </div>

            <div class="row mb-3">
                <div class="col">
                    <label for="country" class="form-label fw-semibold">Country:</label>
                    <v-select v-model="country" :options="countries" label="country" :clearable="false"
                        class="custom-select rounded-1"></v-select>
                </div>
                <div class="col">
                    <label for="dept" class="form-label fw-semibold">Department:</label>
                    <v-select v-model="dept" :options="departments" label="department" :clearable="false"
                        class="custom-select rounded-1"></v-select>
                </div>
                <div class="col">
                    <label for="reporting_manager" class="form-label fw-semibold">Reporting Manager:</label>
                    <v-select v-model="reportingManager" :options="staff" label="staffFName"
                        :reduce="(option) => option.staffID" :clearable="false" class="custom-select rounded-1">
                        <template #selected-option="{ staffFName, staffLName }">
                            <div>{{ staffFName }} {{ staffLName }}</div>
                        </template>
                        <template #option="{ staffID, staffFName, staffLName }">
                            <div>{{staffID}} {{ staffFName }} {{ staffLName }}</div>
                        </template></v-select>
                </div>

            </div>

            <div class="mb-3">
                <label for="datePicker" class="form-label fw-semibold">Open Window:</label>
                <input type="date" id="datePicker" name="datePicker" v-model="openW" @change="handleDateChange"
                    class="form-control" />
            </div>

            <div class="mb-3">
                <label for="datePicker" class="form-label fw-semibold">Close Window:</label>
                <input type="date" id="datePicker" name="datePicker" v-model="closeW" @change="handleCloseWChange"
                    class="form-control" />
            </div>

            <div class="mb-3">
                <label for="roleDesc" class="form-label fw-semibold">Role Description:</label>
                <div id="roleDesc" class="bg-white p-3 rounded-3">
                    {{ selectedRoleDesc }}
                </div>
            </div>

            <div class="mb-3 gap-2">
                <label for="roleDesc" class="form-label fw-semibold">Required Skills:</label>
                <div>
                    <span class="badge text-bg-primary me-2 mt-2" v-for="skill in skills">{{ skill.Skill_Name }}, Level {{ skill.Proficiency_Level }}</span>
                </div>
            </div>

            <button @click="sendRequest" class="btn btn-warning fw-semibold">
                Add Role Listing
            </button>
        </div>
    </div>
</template>

<style scoped>
.custom-select {
    background-color: white; 
}
</style>

