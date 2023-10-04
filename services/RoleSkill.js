import axios from "axios";

// testing 

const API_URL = "http://localhost:8000/";

class RoleSkillService{

    getAllRoleSkills(){
        const response = axios.get(API_URL + "getallroleskills")
        .then((response)=>{
            console.log("Get All Role Skills Successful")
            return response
        })
        .catch((error)=>{
            console.log("Get All Role Skills NOT successful " + error)
            return error
        })

        return response
    }

    getRoleSkills(listingId){
        const response = axios.get(API_URL + "getroleskills/" + listingId)
        .then((response)=>{
            console.log("Get Role Skills Successful")
            return response
        })
        .catch((error)=>{
            console.log("Get Role Skills NOT successful " + error)
            return error
        })

        return response
    }

}
export default new RoleSkillService()
