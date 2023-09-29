import axios from "axios";

const API_URL = "http://localhost:8000/";

class RoleSkillService{

    getAllRoleSkills(){
        const response = axios.get(API_URL + "getallroleskills")
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
