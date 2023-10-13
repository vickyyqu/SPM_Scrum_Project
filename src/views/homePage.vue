<script>
import Navbar from '../components/Navbar.vue';
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
                "HR": [
                    {
                        "userId" : "140002",
                        "pwd": "smu123"
                    }, 
                    {
                        "userId" : "140003",
                        "pwd": "smu123"
                    }
                ], 
                "Manager/Director": [
                    {
                        "userId" : "130001",
                        "pwd": "smu123"
                    }
                ], 
                "Staff": [
                    {
                        "userId" : "140001",
                        "pwd": "smu123"
                    },
                    {
                        "userId" : "140008",
                        "pwd": "smu123"
                    }
                ]
            },
            errMsg: ""
        }
    },
    methods: {
        validateUser(){
            console.log(this.staffId)
            console.log(this.pwd)

            if (this.myRole.length == 0){
                this.errMsg = "Please select a role."
            } else {
                var userExist = false
                var checkUser = this.usersList[this.myRole]

                for (let i=0; i<checkUser.length; i++){
                    if (checkUser[i]["userId"]==this.staffId && checkUser[i]["pwd"]==this.pwd) {
                        console.log("Login successful!")
                        userExist = true

                        // set staff id
                        sessionStorage.setItem("staffId", this.staffId)
                        sessionStorage.setItem("myRole", this.myRole)
                        this.$router.push("/rolelistings")

                    } else if (checkUser[i]["userId"]==this.staffId && checkUser[i]["pwd"]!=this.pwd){
                        userExist = true
                        this.errMsg = "Password is incorrect."
                        this.pwd = ""
                    }
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
                <template v-for="role in roles">
                    <tr v-for="each in usersList[role]">
                        <td>{{ role }}</td>
                        <td>{{each['userId']}}</td>
                        <td>{{each['pwd']}}</td>
                    </tr>
                </template>
            </tbody>
        </table>
    </div>
</template>