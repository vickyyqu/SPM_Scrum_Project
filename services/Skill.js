import axios from "axios";

const API_URL = "http://localhost:8000/";

class SkillsService{

    getAllSkills(){
        const response = axios.get(API_URL + "getallskills")
        .then((response)=>{
            console.log("Get Skills Successful")
            return response
        })
        .catch((error)=>{
            console.log("Get Skills NOT successful " + error)
            return error
        })

        return response
    }

    getSkillsForRole(role_name){
        const response = axios.get(API_URL + "getskillsforrole/" + role_name)
        .then((response)=>{
            console.log("Get Skills Successful")
            return response
        })
        .catch((error)=>{
            console.log("Get Skills NOT successful " + error)
            return error
        })

        return response
    }

    getSkillsAndProficiencyLevelForRole(role_name){ 
        const response = axios.get(API_URL + "getrequiredskillsandproficiency/" + role_name)
        .then((response)=>{ 
            console.log("Get Skills and Proficiency Levels Successful")
            return response
        })
        .catch((error)=>{
            console.log("Get Skills and Proficiency Levels NOT successful " + error)
            return error
        })

        return response
    }

}
export default new SkillsService()