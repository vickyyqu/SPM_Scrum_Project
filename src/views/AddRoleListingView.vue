<script setup>
import Navbar from '../components/navbar.vue';
</script>

<template>
    <Navbar />
    <div class="container-fluid mt-5 pt-5" style="position: absolute;
 top: 0;
 right: 0;
 bottom: 0;
 left: 0;background-color: lightgray; outline: black 1px solid;">

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
                <div class="col-8 text-start">
                    <div class="mb-3">
                        <input type="text" class="form-control" id="roleRequiredSkills1">
                    </div>
                </div>
                <div class="col-3 text-start">
                    <div class="mb-3">
                        <input type="number" class="form-control" id="roleRequiredSkills1Proficiency" min="1" max="">
                    </div>
                </div>
                <div class="col-1">
                    <div class="mb-3">
                        <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor"
                            class="bi bi-plus-circle" viewBox="0 0 16 16">
                            <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z" />
                            <path
                                d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z" />
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
