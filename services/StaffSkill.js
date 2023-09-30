import axios from "axios";

const API_URL = "http://localhost:8000/";

class StaffSkillsService{

    getStaffSkills(staffId){
        const response = axios.get(API_URL + "getstaffskills/" + staffId)
        .then((response)=>{
            console.log("Get Staff Skills Successful")
            return response
        })
        .catch((error)=>{
            console.log("Get Staff Skills NOT successful " + error)
            return error
        })

        return response
    }

}
export default new StaffSkillsService()