import axios from "axios";

const API_URL = "http://localhost:8000/";

class RoleService{

    getAllRoles(){
        const response = axios.get(API_URL + "getallroles")
        .then((response)=>{
            console.log("Get Roles Successful")
            return response
        })
        .catch((error)=>{
            console.log("Get Roles NOT successful " + error)
            return error
        })

        return response
    }

}
export default new RoleService()