<template>
    <div class="container-fluid pt-5">

        <div class="container">
            <div class="row">
                <div class="col text-start">
                    <div class="mb-3">
                        <label for="roleTitle" class="form-label">Role Name</label>
                        <input type="text" class="form-control" id="roleTitle" v-model="search_role_name" placeholder="Search for Roles">
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
                        <button type="button" class="btn btn-info">Search</button>
                    </div>
                </div>
            </div>

            <div class="container-fluid">
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

                <div class="row mb-5">
                    <div class="form-group">
                        <div v-for="(input, index) in skills_required" :key="`skillsInput-${index}`"
                            class="input wrapper flex items-center">
                            <div class="row">
                                <!-- <div class="col-9"><input v-model="input.skill" type="text" class="form-control" /></div> -->
                                <div class="col-9">
                                    <select v-model="selected" class="form-select">
                                        <option v-for="skill in skills" :value="skill.value">
                                            {{ skill.skillName }}
                                        </option>
                                    </select>
                                </div>
                                <div class="col-3"><input v-model="input.proficiency" type="number" class="form-control" />
                                </div>
                            </div>

                            <!--Add Svg Icon-->
                            <svg @click="addField(input, skills_required)" xmlns="http://www.w3.org/2000/svg"
                                viewBox="0 0 24 24" width="24" height="24" class="ml-2 cursor-pointer">
                                <path fill="none" d="M0 0h24v24H0z" />
                                <path fill="green"
                                    d="M11 11V7h2v4h4v2h-4v4h-2v-4H7v-2h4zm1 11C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10 10zm0-2a8 8 0 1 0 0-16 8 8 0 0 0 0 16z" />
                            </svg>

                            <!--Remove Svg Icon-->
                            <svg v-show="skills_required.length > 1" @click="removeField(index, skills_required)"
                                xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24"
                                class="ml-2 cursor-pointer">
                                <path fill="none" d="M0 0h24v24H0z" />
                                <path fill="#EC4899"
                                    d="M12 22C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10 10zm0-2a8 8 0 1 0 0-16 8 8 0 0 0 0 16zm0-9.414l2.828-2.829 1.415 1.415L13.414 12l2.829 2.828-1.415 1.415L12 13.414l-2.828 2.829-1.415-1.415L10.586 12 7.757 9.172l1.415-1.415L12 10.586z" />
                            </svg>
                        </div>
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
            badges: ['Badge 1', 'Badge 2', 'Badge 3', 'Badge 4'] // Your badge data
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
};
</script>
