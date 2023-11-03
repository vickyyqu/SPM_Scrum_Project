import axios from "axios";

const API_URL = "http://localhost:8000/";

class RoleSkillMatchService{

    getRoleSkillMatch(listing_id, staff_id){
        const response = axios.get(API_URL + "getroleskillmatch/" + listing_id + "&" + staff_id)
        .then((response)=>{
            console.log("Get Role Skill Match Successful")
            return response
        })
        .catch((error)=>{
            console.log("Get Role Skill Match NOT successful " + error)
            return error
        })

        return response
    }

}
export default new RoleSkillMatchService()