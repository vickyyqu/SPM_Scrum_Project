<script setup>
import Navbar from '../components/navbar.vue';
</script>

<template>
    <Navbar />
    <div class="container-fluid mt-5 pt-5" 
    style="position: absolute;
 top: 0;
 right: 0;
 bottom: 0;
 left: 0;background-color: lightgray; outline: black 1px solid;">
        <div class="row">
            <div class="col-6">
                <div class="card mx-auto" style="width: 25rem;">
                    <div class="card-body">
                        <h5 class="card-title">Test Role Listing</h5>
                        <h6 class="card-subtitle mb-2 text-body-secondary">Test Dept</h6>
                        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                        <a href="#" class="card-link">Card link</a>
                        <a href="#" class="card-link">Another link</a>
                    </div>
                </div>
            </div>

            <div class="col-6">
                <div class="card mx-auto" style="width: 25rem;">
                    <div class="card-body">
                        <h5 class="card-title">Card title</h5>
                        <h6 class="card-subtitle mb-2 text-body-secondary">Card subtitle</h6>
                        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                        <a href="#" class="card-link">Card link</a>
                        <a href="#" class="card-link">Another link</a>
                    </div>
                </div>
            </div>

        </div>
    </div>
</template>
<style>
</style>