<script>
import Navbar from "../components/navbar.vue";
import { ref, watch } from "vue";
import { useRoute } from "vue-router";
import roleListingService from "../../services/RoleListing.js";
import roleService from "../../services/Role.js";
import staffService from "../../services/Staff.js";
import axios from "axios";

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

        const fetchRoleDesc = async () => {
            try {
                const response = await roleService.getRoleDesc(roleName.value);
                selectedRoleDesc.value = response.data.Role_Desc;
            } catch (error) {
                console.error("Error fetching roleDesc:", error);
            }
        };

        watch(roleName, fetchRoleDesc);

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
                    "http://localhost:8000/updaterolelisting/" +
                        roleListing.value.id,
                    requestBody
                );

                console.log("Response:", response.data);
                alert("Listing successfully updated!");
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
        };
    },
};
</script>

<template>
    <div>
        <Navbar />

        <div v-if="roleListing">
            <div class="container">
                <div class="row">
                    <label for="role_name" class="mt-5">Role Name:</label>
                    <select name="role_name" id="role_name" v-model="roleName">
                        <option
                            v-for="(role, key) in roles"
                            :key="role.roleName"
                            :value="role.roleName"
                        >
                            {{ role.roleName }}
                        </option>
                    </select>
                </div>

                <div class="row">
                    <label for="reporting_manager">Reporting Manager:</label>
                    <select name="reporting_manager" id="reporting_manager" v-model="reportingManager">
                        <option
                            v-for="(manager, key) in managers"
                            :key="manager.staffID"
                            :value="manager.staffID"
                        >
                            {{ manager.staffFName + " " + manager.staffLName }}
                        </option>
                    </select>
                </div>

                <div class="row">
                    <label for="country">Country:</label>
                    <input
                        type="text"
                        id="country"
                        name="country"
                        v-model="country"
                    />
                </div>

                <div class="row">
                    <label for="dept">Department:</label>
                    <input type="text" id="dept" name="dept" v-model="dept" />
                </div>

                <div class="row">
                    <label for="datePicker">Open Window:</label>
                    <input
                        type="date"
                        id="datePicker"
                        name="datePicker"
                        v-model="openW"
                    />
                </div>

                <div class="row">
                    <label for="datePicker">Close Window:</label>
                    <input
                        type="date"
                        id="datePicker"
                        name="datePicker"
                        v-model="closeW"
                    />
                </div>

                <div class="row">
                    <label for="roleDesc">Role Description:</label>
                    <div id="roleDesc">{{ selectedRoleDesc }}</div>
                </div>

                <button @click="sendRequest">Update</button>
            </div>
        </div>
        <div v-else>
            <h1>Role Listing does not exist</h1>
        </div>
    </div>
</template>

<style></style>
