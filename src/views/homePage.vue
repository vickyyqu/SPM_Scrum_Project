<script>
import { useRoute } from "vue-router";
import router from '../main';

export default {
    data() {
        return {
            staffId: "",
            pwd: "",
            roles: ["Staff", "Manager/Director", "HR"],
            myRole: "",
            checkuser: {
                "HR": {
                    "userId" : 1,
                    "pwd": "smu@1234"
                }, 
                "Manager/Director": {
                    "userId" : 2,
                    "pwd": "smu@1234"
                }, 
                "Staff": {
                    "userId" : 3,
                    "pwd": "smu@1234"
                }
            }
        }
    },
    methods: {
        validate(){
            // console.log(this.staffId)
            // console.log(this.pwd)

            // sessionStorage.setItem("staffId", this.staffId)
            this.$router.push("/rolelistings")
        },
        changeRole(role){
            console.log(role)
            this.myRole = role
        }
    }
}
</script> 

<template>
    <div class="container-fluid d-flex justify-content-center">
        <div class="row mt-5 w-50" style="text-align:start;">

            <span style="pb-0 mb-0">I am a {{myRole}}</span>
            <div class="btn-group mb-4 mt-0" role="group">
                <span v-for="each in roles">
                    <button v-if="each==myRole" type="button" class="btn btn-light me-2" @click="changeRole(each)" disabled>{{each}}</button>
                    <button v-else type="button" class="btn btn-light me-2" @click="changeRole(each)">{{each}}</button>
                </span>
            </div>

            <form class="myForm mx-auto">
                <div class="form-group mb-4">
                    <span style="pb-0 mb-0">Staff ID:</span>
                    <input class="form-control input-lg" type="text" v-model="staffId"
                        placeholder="Enter your staff ID" />
                </div>
                <div class="form-group mb-4" style="text-align:start;">
                    <span style="pb-0 mb-0">Password:</span>
                    <input class="form-control input-lg" type="password" placeholder="Enter your password" v-model="pwd"/>
                </div>
                <div class="form-group d-flex justify-content-center">
                    <button class="btn btn-success" @click="validate()">Login</button>
                </div>
            </form>
        </div>
    </div>
</template>