<script>
import { ref, onMounted } from 'vue'
import RoleSkillService from '../../services/RoleSkill.js'

export default {
  setup() {
    const roleSkills = ref([])

    RoleSkillService.getAllRoleSkills().then(response => {
      const skillsData = response.data;

      // Create a temporary array to store unique skills
      const uniqueSkills = [];

      console.log(skillsData)

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
  <div class="container-fluid mt-5 pt-5" style="position: absolute;
              top: 0;
              right: 0;
              bottom: 0;
              left: 0;background-color: lightgray; outline: black 1px solid;
              text-align: left;">

    <div class="list-group mx-auto my-2" style="width: 80%">
      <h1>
        List of Skills Available
      </h1>
      <h6>
        note: this is a feature that should be available to only HR, managers and directors <br>
        - to delete this note
      </h6>
    </div>

    <div v-if="roleSkills.length > 0">
      <ul class="list-group mx-auto my-2" style="width: 80%" v-for="(skill, index) in roleSkills" :key="index">
        <li class="list-group-item" >
          <h6 class="my-auto rounded-lg">{{ skill }}</h6>
        </li>
      </ul>
    </div>

    <div v-else>
      <h6>No skill available</h6>
    </div>

  </div>
</template>

<style></style>

