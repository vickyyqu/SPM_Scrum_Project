<script>
import Navbar from '../components/Navbar.vue';
import StaffsService from '../../services/Staff';
export default {
    components: {
        Navbar
    },
    data() {
        return {
            staffId: "",
            pwd: "",
            roles: ["Staff", "HR", "Manager/Director"],
            myRole: "",
            usersList: {
                "HR": {}, 
                "Manager/Director": {}, 
                "Staff": {}
            },
            errMsg: ""
        }
    },
    mounted() {
        this.getAllStaff()
    },
    methods: {
        async getAllStaff(){
            try { 
                const response = await StaffsService.getAllStaffs()
                var allStaff = response.data
                console.log(allStaff)

                this.usersList =  {
                    "HR": {}, 
                    "Manager/Director": {}, 
                    "Staff": {}
                }

                for (let i=0; i<allStaff.length; i++){
                    if (allStaff[i].staffRole == 1) { // Manager or Director role 
                        var staff = allStaff[i].staffID

                        if (!this.usersList["Manager/Director"].hasOwnProperty(staff)){
                            this.usersList["Manager/Director"][staff] = "smu123"
                        }
                    } else if (allStaff[i].staffRole == 3) { // Staff role 
                        var staff = allStaff[i].staffID

                        if (!this.usersList["HR"].hasOwnProperty(staff)){
                            this.usersList["HR"][staff] = "smu123"
                        }
                    } else { // HR role 
                        var staff = allStaff[i].staffID

                        if (!this.usersList["Staff"].hasOwnProperty(staff)){
                            this.usersList["Staff"][staff] = "smu123"
                        }
                    }
                }
            }
            catch(error){
                console.log(error)
            }
        },
        validateUser(){
            console.log(this.staffId)
            console.log(this.pwd)

            if (this.myRole.length == 0){
                this.errMsg = "Please select a role."
            } else {
                var userExist = false
                var checkUser = this.usersList[this.myRole]

                if (checkUser.hasOwnProperty(this.staffId) && checkUser[this.staffId]==this.pwd) {
                    console.log("Login successful!")
                    userExist = true

                    // set staff id
                    sessionStorage.setItem("staffId", this.staffId)
                    sessionStorage.setItem("myRole", this.myRole)
                    this.$router.push("/rolelistings")

                } else if (checkUser.hasOwnProperty(this.staffId) && checkUser[this.staffId]!=this.pwd){
                    userExist = true
                    this.errMsg = "Password is incorrect."
                    this.pwd = ""
                }

                if (!userExist){
                    this.errMsg = "Staff ID is invalid."
                    this.staffId = ""
                    this.pwd = ""
                }
            }
        },
        changeRole(role){
            console.log(role)
            this.myRole = role
        }
    }
}
</script> 

<template>
    <Navbar />
    <div class="container-fluid d-flex justify-content-center">
        <div class="row my-4 w-50" style="text-align:start;">

            <span style="pb-0 mb-0">I am a {{myRole}}</span>
            <div class="btn-group mb-4 mt-0" role="group">
                <span v-for="each in roles">
                    <button v-if="each==myRole" type="button" class="btn btn-light me-2" @click="changeRole(each)" disabled>{{each}}</button>
                    <button v-else type="button" class="btn btn-light me-2" @click="changeRole(each)">{{each}}</button>
                </span>
            </div>

            <div class="myForm mx-auto">
                <div class="form-group mb-4">
                    <span style="pb-0 mb-0">Staff ID:</span>
                    <input class="form-control input-lg" type="text" v-model="staffId"
                        placeholder="Enter your staff ID" />
                </div>
                <div class="form-group mb-4" style="text-align:start;">
                    <span style="pb-0 mb-0">Password:</span>
                    <input class="form-control input-lg" type="password" placeholder="Enter your password" v-model="pwd"/>
                </div>
                <div v-if="errMsg.length>0" class="alert alert-danger">
                    {{ errMsg }}
                </div>
                <div class="form-group d-flex justify-content-center">
                    <button class="btn btn-success" @click="validateUser()">Login</button>
                </div>
            </div>
        </div>
    </div>
    <div class="container d-flex justify-content-center">
        <table class="table table-striped w-75">
            <thead>
                <tr>
                <th scope="col">Role</th>
                <th scope="col">Staff ID</th>
                <th scope="col">Password</th>
                </tr>
            </thead>
            <tbody>
                <template v-if="myRole.length>0">
                    <tr v-for="(value, key) in usersList[myRole]">
                        <td>{{ myRole }}</td>
                        <td>{{ key }}</td>
                        <td>{{ value }}</td>
                    </tr>
                </template>
            </tbody>
        </table>
    </div>
</template>