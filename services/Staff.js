import axios from "axios";

const API_URL = "http://localhost:8000/";

class StaffsService{

    getAllStaffs(){
        const response = axios.get(API_URL + "getallstaffs")
        .then((response)=>{
            console.log("Get Staffs Successful")
            return response
        })
        .catch((error)=>{
            console.log("Get Staffs NOT successful " + error)
            return error
        })

        return response
    }

    getAllManagers(){
        const response = axios.get(API_URL + "getallmanagers")
        .then((response)=>{
            console.log("Get Managers Successful")
            return response
        })
        .catch((error)=>{
            console.log("Get Managers NOT successful " + error)
            return error
        })

        return response
    }

}
export default new StaffsService()