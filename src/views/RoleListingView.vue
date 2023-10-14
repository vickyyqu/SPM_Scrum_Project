<script>
import { ref, onMounted, watch } from "vue";
import { useRoute } from "vue-router";
import Navbar from "../components/Navbar.vue";
import roleListingService from "../../services/RoleListing.js";
import countryService from "../../services/Country.js";
import departmentService from "../../services/Department.js";
import skillService from "../../services/Skill.js";
import router from "../main";

export default {
    components: {
        Navbar,
    },
    setup() {
        const roleListings = ref([]);
        const route = useRoute();
        var halfway = ref(0);
        const countries = countryService.getAllCountries();
        const skills = ref();
        const departments = departmentService.getAllDepartments();
        const selectedCountries = ref([]);
        const selectedDepartments = ref([]);
        const selectedSkills = ref([]);
        const filteredListings = ref([]);
        const startD = ref();
        const endD = ref();
        const filteredSkills = ref();
        const searchedSkill = ref();

        // retrieve staff id
        console.log(sessionStorage.getItem("staffId"));

        roleListingService.getAllRoleListings().then((response) => {
            roleListings.value = response.data;
            filteredListings.value = roleListings.value;
            console.log(roleListings.value);
            halfway.value = Math.ceil(roleListings.value.length / 2);
            console.log(halfway);
        });
        function viewDetails(id) {
            router.push({
                path: "/rolelistingdetails",
                query: { listingId: id },
            });
        }

        skillService.getAllSkills().then((response) => {
            skills.value = response.data;
            filteredSkills.value = skills.value;
            console.log(skills.value);
        });

        // clear filters
        const clearFilters = () => {
            selectedCountries.value = [];
            selectedDepartments.value = [];
            selectedSkills.value = [];
            startD.value = null;
            endD.value = null;
            filteredListings.value = roleListings.value;
        };

        const filterListings = async () => {
            filteredListings.value = roleListings.value;
            console.log(filteredListings.value);
            if (
                selectedCountries.value.length &&
                selectedDepartments.value.length
            ) {
                filteredListings.value = filteredListings.value.filter(
                    (obj) =>
                        selectedCountries.value.includes(obj.country) &&
                        selectedDepartments.value.includes(obj.dept)
                );
            }
            if (selectedCountries.value.length) {
                filteredListings.value = filteredListings.value.filter((obj) =>
                    selectedCountries.value.includes(obj.country)
                );
            }
            if (selectedDepartments.value.length) {
                filteredListings.value = filteredListings.value.filter((obj) =>
                    selectedDepartments.value.includes(obj.dept)
                );
            }
            if (selectedSkills.value.length) {
                // Fetch skills for each role and then filter based on selected skills
                filteredListings.value = await Promise.all(
                    filteredListings.value.map(async (obj) => {
                        try {
                            const response =
                                await skillService.getSkillsForRole(obj.name);
                            const roleSkills = response.data.map(
                                (skill) => skill.Skill_Name
                            );

                            // Check if at least one of the selected skills is included in the roleSkills
                            if (
                                selectedSkills.value.some((skill) =>
                                    roleSkills.includes(skill)
                                )
                            ) {
                                return obj;
                            }
                        } catch (error) {
                            console.error(
                                `Error fetching skills for role ${obj.role}:`,
                                error
                            );
                        }
                        return null;
                    })
                );

                // Filter out listings with errors during the API request
                filteredListings.value = filteredListings.value.filter(
                    (listing) => listing !== null
                );
            }
            if (startD.value) {
                const start = new Date(startD.value).toISOString().slice(0, 10);
                filteredListings.value = filteredListings.value.filter(
                    (obj) =>
                        new Date(obj.OpenW).toISOString().slice(0, 10) >= start
                );
            }
            if (endD.value) {
                const end = new Date(endD.value).toISOString().slice(0, 10);
                filteredListings.value = filteredListings.value.filter(
                    (obj) =>
                        new Date(obj.CloseW).toISOString().slice(0, 10) <= end
                );
            }
        };

        const filterSkillList = () => {

            filteredSkills.value = skills.value;
            filteredSkills.value = filteredSkills.value.filter((item) =>
                    item.skillName
                        .toLowerCase()
                        .includes(searchedSkill.value.toLowerCase())
            );
        };

        watch(selectedCountries, filterListings);
        watch(selectedDepartments, filterListings);
        watch(selectedSkills, filterListings);
        watch(startD, filterListings);
        watch(endD, filterListings);
        watch(searchedSkill, filterSkillList);

        return {
            roleListings,
            viewDetails,
            halfway,
            countries,
            departments,
            selectedCountries,
            selectedDepartments,
            clearFilters,
            filterListings,
            filteredListings,
            skills,
            selectedSkills,
            startD,
            endD,
            filteredSkills,
            searchedSkill,
        };
    },
};
</script>

<template>
    <Navbar />
    <div class="container-fluid">
        <div class="row">
            <div class="col-2 sidebar">
                <div class="row">
                    <label for="startD" class="form-check-label fw-semibold"
                        ><h6>Open Window</h6></label
                    >
                    <input
                        type="date"
                        class="form-control"
                        id="startD"
                        name="startD"
                        v-model="startD"
                    />
                </div>
                {{ startD }}
                <div class="row mt-3">
                    <label for="endD" class="form-check-label fw-semibold"
                        ><h6>Close Window</h6></label
                    >
                    <input
                        type="date"
                        class="form-control"
                        id="endD"
                        name="endD"
                        v-model="endD"
                    />
                </div>
                {{ endD }}
                <div class="row mt-3">
                    <h6>Country</h6>
                    <div class="form-check" v-for="country in countries">
                        <input
                            class="form-check-input"
                            type="checkbox"
                            :value="country"
                            :id="country"
                            v-model="selectedCountries"
                        />
                        <label class="form-check-label" :for="country">
                            {{ country }}
                        </label>
                    </div>
                </div>
                <div class="row mt-2">
                    <h6>Departments</h6>
                    <div class="form-check" v-for="department in departments">
                        <input
                            class="form-check-input"
                            type="checkbox"
                            :value="department"
                            :id="department"
                            v-model="selectedDepartments"
                        />
                        <label class="form-check-label" :for="department">
                            {{ department }}
                        </label>
                    </div>
                </div>
                <div class="row mt-2">
                    <h6>Skills</h6>
                    <div class="form-check">
                        <div>
                            <input
                                class="form-check-input"
                                type="checkbox"
                                :value="skills[0].skillName"
                                :id="skills[0].skillName"
                                v-model="selectedSkills"
                            />
                            <label
                                class="form-check-label"
                                :for="skills[0].skillName"
                            >
                                {{ skills[0].skillName }}
                            </label>
                        </div>
                    </div>
                    <div class="form-check">
                        <div>
                            <input
                                class="form-check-input"
                                type="checkbox"
                                :value="skills[1].skillName"
                                :id="skills[1].skillName"
                                v-model="selectedSkills"
                            />
                            <label
                                class="form-check-label"
                                :for="skills[1].skillName"
                            >
                                {{ skills[1].skillName }}
                            </label>
                        </div>
                    </div>
                    <div class="form-check">
                        <div>
                            <input
                                class="form-check-input"
                                type="checkbox"
                                :value="skills[2].skillName"
                                :id="skills[2].skillName"
                                v-model="selectedSkills"
                            />
                            <label
                                class="form-check-label"
                                :for="skills[2].skillName"
                            >
                                {{ skills[2].skillName }}
                            </label>
                        </div>
                    </div>
                    <!-- Button trigger modal -->
                    <a
                        href=""
                        class="underline"
                        data-bs-toggle="modal"
                        data-bs-target="#exampleModal"
                    >
                        See more...
                    </a>

                    <!-- Modal -->
                    <div
                        class="modal fade"
                        id="exampleModal"
                        tabindex="-1"
                        aria-labelledby="exampleModalLabel"
                        aria-hidden="true"
                    >
                        <div class="modal-dialog">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <h1
                                        class="modal-title fs-5"
                                        id="exampleModalLabel"
                                    >
                                        Skills
                                    </h1>
                                    <button
                                        type="button"
                                        class="btn-close"
                                        data-bs-dismiss="modal"
                                        aria-label="Close"
                                    ></button>
                                </div>
                                <div class="modal-body">
                                    <div class="input-group mb-3">
                                        <input
                                            type="text"
                                            class="form-control"
                                            placeholder="Search skills..."
                                            aria-label="Username"
                                            aria-describedby="basic-addon1"
                                            v-model="searchedSkill"
                                        />
                                    </div>
                                    <div
                                        v-if="filteredSkills.length > 0"
                                        class="form-check"
                                        v-for="skill in filteredSkills"
                                    >
                                        <input
                                            class="form-check-input"
                                            type="checkbox"
                                            :value="skill.skillName"
                                            :id="skill.skillName"
                                            v-model="selectedSkills"
                                        />
                                        <label
                                            class="form-check-label"
                                            :for="skill.skillName"
                                        >
                                            {{ skill.skillName }}
                                        </label>
                                    </div>
                                    <div v-else>
                                        <h6>No matching results.</h6>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row mt-3">
                    <div class="col p-0 d-grid gap-2 col-6 mx-auto w-100">
                        <button class="btn btn-danger" @click="clearFilters">
                            Clear Filters
                        </button>
                    </div>
                </div>
                <!-- {{ selectedCountries }}
                {{ selectedDepartments }}
                {{ selectedSkills }} -->
            </div>
            <div class="col-10">
                <div class="row">
                    <div
                        v-if="filteredListings.length > 0"
                        class="col-6 g-3"
                        v-for="listing in filteredListings"
                    >
                        <div
                            class="card mx-auto rounded"
                            style="width: 25rem"
                            @click="viewDetails(listing['id'])"
                        >
                            <div class="card-body">
                                <h5 class="card-title">
                                    {{ listing["name"] }}
                                </h5>
                                <h6
                                    class="card-subtitle mb-2 text-body-secondary"
                                >
                                    {{ listing["dept"] }}
                                </h6>
                                <h6
                                    class="card-subtitle mb-2 text-body-secondary"
                                >
                                    {{ listing["country"] }}
                                </h6>
                                <h6 href="#" class="subtitle">
                                    {{ listing["OpenW"] }}
                                </h6>
                                <h6 href="#" class="subtitle">
                                    {{ listing["CloseW"] }}
                                </h6>
                            </div>
                        </div>
                    </div>
                    <div v-else class="mt-5">
                        <h3>No matching results.</h3>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style>
.sidebar {
    font-size: small;
    text-align: left;
}
</style>
