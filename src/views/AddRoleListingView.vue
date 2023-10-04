<template>
    <div class="container-fluid pt-5">

        <div class="container">
            <div class="row">
                <div class="col text-start">
                    <div class="mb-3">
                        <label for="roleTitle" class="form-label">Role Name</label>
                        <input type="text" class="form-control" id="roleTitle" v-model="search_role_name"
                            placeholder="Search for Roles">
                        <div class="form-text">Please enter at least 3 letters.</div>
                    </div>
                </div>
                <div class="row">
                    <div class="col d-flex flex-column">
                        <div v-for="(value, index) in role_names" class="form-check d-inline-flex">
                            <input class="form-check-input" type="radio" name="role_name" v-bind:id="value.role_name"
                                v-bind:value="value.role_name" v-model="role_name">
                            <label class="form-check-label" v-bind:for="value.role_name">
                                <strong>{{ value.Role_Name }}</strong>
                            </label>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col">
                        <button type="button" class="btn btn-info" @click="searched = true">Search</button>
                    </div>
                </div>
            </div>

            <div class="container-fluid" v-show="searched">
                <div class="row">
                    <div class="col text-start">
                        <label for="roleRequiredSkills1" class="form-label">Required Skills - Proficiency</label>
                    </div>
                </div>
                <div class="row">
                    <div>
                        <span v-for="(badge, index) in badges" :key="index" class="badge text-bg-primary rounded-pill">
                            {{ badge }}
                        </span>
                    </div>
                </div>


                <div class="row mb-3">
                    <div class="col-4 text-start">
                        <label for="roleCountry" class="form-label">Country</label>
                        <input type="text" class="form-control" id="roleCountry">
                    </div>
                    <div class="col-4 text-start">
                        <label for="roleDepartment" class="form-label">Department</label>
                        <input type="text" class="form-control" id="roleDepartment">
                    </div>
                    <div class="col-4 text-start">
                        <label for="roleReportingManager" class="form-label">Reporting Manager</label>
                        <input type="text" class="form-control" id="roleReportingManager">
                    </div>
                </div>

                <div class="row">
                    <div class="col text-start">
                        <label for="roleDescription" class="form-label">Description</label>
                        <textarea class="form-control" id="roleDescription" rows="5"></textarea>
                    </div>
                </div>

                <div class="row mt-5">
                    <div class="col d-flex justify-content-end">
                        <button type="button" class="btn btn-warning rounded-pill">Post Listing</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<style></style>

<script>
import { ref, onMounted } from 'vue'
import skillService from '../../services/Skill.js'
import axios from 'axios'


export default {
    data() {
        return {
            search_role_name: "",
            role_names: [],
            badges: ['Badge 1', 'Badge 2', 'Badge 3', 'Badge 4'], // Your badge data
            searched: false
        };
    },
    watch: {
        search_role_name: function () {
            if (this.search_role_name.length > 2) {
                axios.get('http://localhost:8000/getroles/' + this.search_role_name)
                    .then(response => {
                        console.log(response.data)
                        this.role_names = response.data;
                    })
                    .catch(error => {
                        console.log(error);
                    });
            } else {
                this.role_names = [];
            }
        },
    },
    methods() {
    }
};
</script>