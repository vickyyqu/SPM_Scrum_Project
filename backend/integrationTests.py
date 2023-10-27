from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import unittest
import json
import flask_testing
from app import *

class TestApp(flask_testing.TestCase):
    
    # app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
    # app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}
    # app.config['TESTING'] = True
    app = Flask(__name__)
   
    # SQLAlchemy configuration
    
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}
    app.config['TESTING'] = True

    db = SQLAlchemy(app)
    CORS(app)


    def create_app(self):
        return app
        

    def setUp(self):
        db.create_all()


    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestApplication(TestApp):
    def test_submit_role_application(self):
        #None as SQLite has troubles dealing with date
        request_body = {
            "closeWindow": None,
            "openWindow": None,
            "country": "Singapore",
            "dept": "Engineering",
            "roleName": {"roleName":"Call Centre"},
            "reportingManager": 130002
        }  

        rolelistingResponse = self.client.post("/addrolelisting",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        
    
        request_body = {
                    "listing_ID": 1,
                    "staff_ID": 140003,
                    "brief_description": "Testing Application"
                }
        
        addAppResponse = self.client.post("/apply_role",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        
        # print("AppResp", end='')
        # print(addAppResponse)
        
        listing_id = 1 
        staff_id = 140003
        getAppResponse = self.client.get(f"/getapplicationsbylistingid/{listing_id}")
        self.assertEqual(getAppResponse.status_code, 200)
        self.client.delete(f"/delete_application/{listing_id}&{staff_id}")


    def test_submit_role_application_invalid(self):

        request_body = {
            "closeWindow": None,
            "openWindow": None,
            "country": "Singapore",
            "dept": "Engineering",
            "roleName": {"roleName":"Call Centre"},
            "reportingManager": 130002
        }  

        rolelistingResponse = self.client.post("/addrolelisting",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        # print("RoleListingResp: ", end='')
        # print(rolelistingResponse.data)
        
        request_body = {
                    "listing_ID": 1,
                    "staff_ID": 1,
                    "brief_description": "Testing Application"
                }
        
        addAppResponse = self.client.post("/apply_role",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        # print("ADD APP HERE")
        # print(request_body)
        # print(addAppResponse)
        ##SINCE Data not loaded onto SQLite, Foreign key does not prevent adding of this application
        self.assertEqual(addAppResponse.status_code, 201)
        

    def test_withdraw_application(self):
    # First, submit an application (assuming you have already tested the submission)
        request_body = {
            "closeWindow": None,
            "openWindow": None,
            "country": "Singapore",
            "dept": "Engineering",
            "roleName": {"roleName": "Call Centre"},
            "reportingManager": 130002
        }
        
        role_listing_response = self.client.post("/addrolelisting",
                                                data=json.dumps(request_body),
                                                content_type='application/json')
        
        # Extract the listing ID and staff ID from the response or get them from the database
        listing_id = 1  # Replace with the actual listing ID
        staff_id = 140002  # Replace with the actual staff ID
        
        # Submit an application for testing purposes
        application_request_body = {
            "listing_ID": listing_id,
            "staff_ID": staff_id,
            "brief_description": "Testing Application"
        }
        
        application_response = self.client.post("/apply_role",
                                                data=json.dumps(application_request_body),
                                                content_type='application/json')
        
        # Now, withdraw the application
        withdraw_response = self.client.delete(f"/delete_application/{listing_id}&{staff_id}")
        
        # Assert that the withdrawal was successful (assuming a 200 status code is returned upon successful withdrawal)
        self.assertEqual(withdraw_response.status_code, 200)
        
        get_application_response = self.client.get(f"/getapplicationsbylistingid/{listing_id}")
        response_data = json.loads(get_application_response.data)
        # print("RESP DATA HERE")
        # print(response_data['error'])
        self.assertEqual(response_data["code"], 404)

    def test_withdraw_application_invalid(self):
    # First, submit an application (assuming you have already tested the submission)
        request_body = {
            "closeWindow": None,
            "openWindow": None,
            "country": "Singapore",
            "dept": "Engineering",
            "roleName": {"roleName": "Call Centre"},
            "reportingManager": 130002
        }
        
        role_listing_response = self.client.post("/addrolelisting",
                                                data=json.dumps(request_body),
                                                content_type='application/json')

        
        # Extract the listing ID and staff ID from the response or get them from the database
        listing_id = 1  # Replace with the actual listing ID
        staff_id = 140002  # Replace with the actual staff ID
        
        # Submit an application for testing purposes
        application_request_body = {
            "listing_ID": listing_id,
            "staff_ID": staff_id,
            "brief_description": "Testing Application"
        }
        
        application_response = self.client.post("/apply_role",
                                                data=json.dumps(application_request_body),
                                                content_type='application/json')
        
        # Now, withdraw the application

        staff_id = 0
        withdraw_response = self.client.delete(f"/delete_application/{listing_id}&{staff_id}")
        
        # Assert that the withdrawal was successful (assuming a 200 status code is returned upon successful withdrawal)
        self.assertEqual(withdraw_response.status_code, 500)
        
        staff_id = 140002
        withdraw_response = self.client.delete(f"/delete_application/{listing_id}&{staff_id}")


class TestRoles(TestApp):
    def testGetRoleListing(self):
        
        new_role_listing = {
            "closeWindow": None,
            "openWindow": None,
            "country": "Singapore",
            "dept": "Engineering",
            "roleName": {"roleName":"Call Centre"},
            "reportingManager": 140002
        }  

        addRoleResp = self.client.post("/addrolelisting",
                                    data=json.dumps(new_role_listing),
                                    content_type='application/json') 
        
        # print(addRoleResp.data)

        getRoleResp = self.client.get("/getallrolelistings")
        
        # print("GET ROLE RESP HERE")
       
        getRoleResp = json.loads(getRoleResp.data)
        self.assertEqual(len(getRoleResp), 1)
        

        


            

if __name__ == '__main__':
    unittest.main()