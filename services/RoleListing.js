import axios from "axios";

const API_URL = "http://localhost:8000/";

class RoleListingService{

    getAllRoleListings(){
        const response = axios.get(API_URL + "getallrolelistings")
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

    getRoleListingById(listing_id){
        const response = axios.get(API_URL + "getrolelisting/" + listing_id)
        .then((response)=>{
            console.log("Get Role Listing Successful")
            return response
        })
        .catch((error)=>{
            console.log("Get Role Listing NOT successful " + error)
            return error
        })

        return response
    }

    updateRoleListing(listing_id, requestBody){
        const response = axios.post(API_URL + "updaterolelisting/" + listing_id, requestBody)
        .then((response)=>{
            console.log("Role Listing successfully updated")
            return response
        })
        .catch((error)=>{
            console.log("Failed to update role listing" + error)
            return error
        })

        return response
    }


    addRoleListing(requestBody){
        const response = axios.post(API_URL + "addrolelisting", requestBody)
        .then((response)=>{ 
            console.log("Role Listing successfully added")
            return response
        })
        .catch((error)=>{
            console.log("Failed to add role listing" + error)
            return error
        })

        return response
    }
}
export default new RoleListingService()