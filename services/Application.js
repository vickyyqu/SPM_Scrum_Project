import axios from "axios";

const API_URL = "http://localhost:8000/";

class StaffApplicationService {
    getApplicationsByListingID(listing_ID){
        const response = axios.get(API_URL + "getapplicationsbylistingid/" + listing_ID)
        .then((response)=>{
            console.log("Get Staff Applications Successful")
            return response
        })
        .catch((error)=>{
            console.log("Get Staff Applications NOT successful " + error)
            return error
        })

        return response
    }

    getAppliedStatus(listing_ID, staff_ID){
        const response = axios.get(API_URL + "getappliedstatus/" + listing_ID + '&' + staff_ID)
        .then((response)=>{
            console.log(response)
            console.log("Get Application Status Successful")
            return response
        })
        .catch((error)=>{
            console.log("No such applications found" + error)
            return error
        })

        return response
    }
}

export default new StaffApplicationService()
