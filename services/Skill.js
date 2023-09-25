import axios from "axios";

const API_URL = "http://localhost:8000/";

class SkillsService{

    getAllSkills(){
        const response = axios.get(API_URL + "getAllSkills")
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

}
export default new SkillsService()