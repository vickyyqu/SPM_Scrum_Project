
<script >
import Navbar from '../components/navbar.vue';
import { ref, onMounted } from 'vue'
import roleListingService from '../../services/RoleListing.js'

export default {
    setup() {
    },


};

</script>


<template>
    <div class="container rounded" style="outline: black 2px solid; height: 80vh; width: 150vh; background-color: lightgray;">

    <div class="pt-5 row justify-content-between" style="width: 100%;">
        <div class="col" style="display: flex;">
            <svg class = "ms-4 me-3" style="fill: black; align-items: left;" xmlns="http://www.w3.org/2000/svg" height="1.5em" viewBox="0 0 448 512">
                <path d="M9.4 233.4c-12.5 12.5-12.5 32.8 0 45.3l160 160c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3L109.2 288 416 288c17.7 0 32-14.3 32-32s-14.3-32-32-32l-306.7 0L214.6 118.6c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0l-160 160z"/>
            </svg>
            <h5>Back</h5>
        </div>
        <div class="col-8"></div>
        <div class="col" style="display: flex;">
            <h5>Edit</h5>
            <svg class="mx-3 mt-1" xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 512 512">
                <path d="M471.6 21.7c-21.9-21.9-57.3-21.9-79.2 0L362.3 51.7l97.9 97.9 30.1-30.1c21.9-21.9 21.9-57.3 0-79.2L471.6 21.7zm-299.2 220c-6.1 6.1-10.8 13.6-13.5 21.9l-29.6 88.8c-2.9 8.6-.6 18.1 5.8 24.6s15.9 8.7 24.6 5.8l88.8-29.6c8.2-2.7 15.7-7.4 21.9-13.5L437.7 172.3 339.7 74.3 172.4 241.7zM96 64C43 64 0 107 0 160V416c0 53 43 96 96 96H352c53 0 96-43 96-96V320c0-17.7-14.3-32-32-32s-32 14.3-32 32v96c0 17.7-14.3 32-32 32H96c-17.7 0-32-14.3-32-32V160c0-17.7 14.3-32 32-32h96c17.7 0 32-14.3 32-32s-14.3-32-32-32H96z"/>
            </svg>
        </div>
    </div>



     <h2 class="mt-3 p-3" style="text-align: left;">Role Listing Title</h2>
     <br>
    
     <div class="container" style="width: 100%; height: 25%;">
        <h1 style="text-align: left;">SKILL MATCH HERE</h1>
     </div>
     <div class="container" style="width: 100%; height: 25%;">
        <p style="text-align: left;">Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus, modi dignissimos. Dicta nobis officiis, magni qui quasi voluptate. Magni, culpa unde eos adipisci autem tempora eius harum repudiandae cumque cupiditate?</p>
     </div>
        
    </div>
</template>

<style></style>

