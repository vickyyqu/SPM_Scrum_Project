<script setup>
import Navbar from '../components/navbar.vue';
// import Dynamic_form from '../components/dynamic_form.vue';
</script>

<template>
    <Navbar />
    <div class="container-fluid pt-5" style="position: absolute;
 top: 0;
 right: 0;
 bottom: 0;
 left: 0;
 background-color: lightgray; 
 outline: black 1px solid;
 min-height: 100vh;
 min-width: 100vw;">

        <div class="container">
            <div class="row">
                <div class="col text-start">
                    <div class="mb-3">
                        <label for="roleTitle" class="form-label">Role Title</label>
                        <input type="text" class="form-control" id="roleTitle">
                    </div>
                </div>
            </div>

            <div class="row">
                <div class="col-8 text-start">
                    <label for="roleRequiredSkills1" class="form-label">Required Skills</label>
                </div>
                <div class="col-3 text-start">
                    <label for="roleRequiredSkills1Proficiency" class="form-label">Proficiency</label>
                </div>
                <div class="col"></div>
            </div>

            <div class="row">
                <div class="form-group">                    
                    <div v-for="(input, index) in skills" :key="`phoneInput-${index}`"
                        class="input wrapper flex items-center">
                        <input v-model="input.skill" type="text" class="form-control" />
                        <!--          Add Svg Icon-->
                        <svg @click="addField(input, skills)" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
                            width="24" height="24" class="ml-2 cursor-pointer">
                            <path fill="none" d="M0 0h24v24H0z" />
                            <path fill="green"
                                d="M11 11V7h2v4h4v2h-4v4h-2v-4H7v-2h4zm1 11C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10 10zm0-2a8 8 0 1 0 0-16 8 8 0 0 0 0 16z" />
                        </svg>

                        <!--          Remove Svg Icon-->
                        <svg v-show="skills.length > 1" @click="removeField(index, skills)"
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
</template>
<style></style>
<script>
export default {
    name: "AddRemove",
    data() {
        return {
            skills: [{ skill: "" }],
        };
    },
    methods: {
        addField(value, fieldType) {
            fieldType.push({ value: "" });
        },
        removeField(index, fieldType) {
            fieldType.splice(index, 1);
        },
    },
};
</script>