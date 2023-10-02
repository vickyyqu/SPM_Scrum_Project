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

    getRoleDesc(role_name){
        const response = axios.get(API_URL + "getroledesc/" + role_name)
        .then((response)=>{
            console.log("Get Role Description Successful")
            return response
        })
        .catch((error)=>{
            console.log("Get Role Description NOT successful " + error)
            return error
        })

        return response
    }

}
export default new RoleService()