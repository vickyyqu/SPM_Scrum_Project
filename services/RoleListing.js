import axios from "axios";

const API_URL = "http://localhost:8000/";

class RoleListingService{

    getAllRoleListings(){
        const response = axios.get(API_URL + "getAllRoleListings")
        .then((response)=>{
            console.log("Get Role Listings Successful")
            return response
        })
        .catch((error)=>{
            console.log("Get Role Listings NOT successful " + error)
            return error
        })

        return response
    }

}
export default new RoleListingService()