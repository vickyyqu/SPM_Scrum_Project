<script>
import Navbar from '../components/navbar.vue';
import { ref, onMounted } from 'vue'
import RoleSkillService from '../../services/RoleSkill.js'

export default {
  setup() {
    const roleSkills = ref([])

    RoleSkillService.getAllRoleSkills().then(response => {
      const skillsData = response.data;
      
      // Create a temporary array to store unique skills
      const uniqueSkills = [];

      // Iterate through the skills data and add unique skills to the temporary array
      skillsData.forEach(skill => {
        if (!uniqueSkills.includes(skill.skill)) {
          uniqueSkills.push(skill.skill);
        }
      });

      // Assign the temporary array to roleSkills
      roleSkills.value = uniqueSkills;
      
      console.log(roleSkills.value);
    });

    return {
      roleSkills
    }
  },
};
</script>

<template>
  <Navbar />
  <div class="container-fluid mt-5 pt-5"
       style="position: absolute;
              top: 0;
              right: 0;
              bottom: 0;
              left: 0;background-color: lightgray; outline: black 1px solid;">

    <div v-for="(skill, index) in roleSkills" :key="index">
      <div class="row">
        <div class="col-6">
          <div class="card mx-auto rounded" style="width: 25rem;">
            <div class="card-body">
              <h5 class="card-title">{{ skill }}</h5>
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<style>
</style>

