from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import unittest
import json
import flask_testing
from functions import role_skill_match
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
        

        
class TestSkills(TestApp):
    def testGetRoleSkillsDeveloper(self):
        skill = SkillTable(Skill_Name = "Applications Development", Skill_Desc = "Test")
        roleSkill = RoleSkillTable(Role_Name = "Developer", Skill_Name = "Applications Development", Proficiency_Level = 1)
        role = RoleTable(Role_Name = "Developer", Role_Desc = "The Developer leads important projects and possesses capability to make breakthroughs in design, development, testing, debugging and implementing software applications or specialised utility programs in support of end users' needs on platforms. He/She plans and coordinates regular updates and recommends improvements to existing applications. He identifies and resolves issues which have organisation wide and long-term impact. He identifies security risks, creates requirements to capture security issues, and performs initial threat modelling to ensure coding standards meets security requirements. He develops and maintains the software configuration management plan and oversees the building, verification and implementation of software releases. He provides guidance and technical support to the quality testing teams. He works in a team setting and is proficient in programming languages required by the organisation. He is familiar with software development tools and standards, as well as the relevant software platforms on which the solution is deployed on. The Developer is imaginative and creative in exploring a range of application designs and solutions. He is able to engage and support others in the team, readily put forth his ideas in a clear and compelling manner.")
        db.session.add(roleSkill)
        db.session.add(role)
        db.session.add(skill)
        db.session.commit()

        current_role = "Developer"
        getRoleSkills = self.client.get(f"/getskillsforrole/{current_role}")
        getRoleSkillsData = json.loads(getRoleSkills.data)
        self.assertEqual(getRoleSkills.status_code, 200)
        self.assertEqual(len(getRoleSkillsData), 1)

    def testGetRoleSkillsAM(self):
        skill = SkillTable( Skill_Desc = "Test", Skill_Name = "Account Management")
        skill2 = SkillTable( Skill_Desc = "Test", Skill_Name = "Budgeting")
        roleSkill = RoleSkillTable(Role_Name = "Account Manager", Skill_Name = "Budgeting", Proficiency_Level = 1)
        roleSkill2 = RoleSkillTable(Role_Name = "Account Manager", Skill_Name = "Account Management", Proficiency_Level = 1)
        role = RoleTable(Role_Name = "Account Manager", Role_Desc = "Test")
        db.session.add(roleSkill)
        db.session.add(role)
        db.session.add(roleSkill2)
        db.session.add(skill)
        db.session.add(skill2)
        db.session.commit()

        current_role = "Account Manager"
        getRoleSkills = self.client.get(f"/getskillsforrole/{current_role}")
        getRoleSkillsData = json.loads(getRoleSkills.data)
        self.assertEqual(getRoleSkills.status_code, 200)
        self.assertEqual(len(getRoleSkillsData), 2)

            
class TestMatch(TestApp):
    def testRoleSkillMatch(self):
        skill = SkillTable( Skill_Desc = "Test", Skill_Name = "Account Management")
        skill2 = SkillTable( Skill_Desc = "Test", Skill_Name = "Budgeting")
        roleSkill = RoleSkillTable(Role_Name = "Account Manager", Skill_Name = "Budgeting", Proficiency_Level = 1)
        roleSkill2 = RoleSkillTable(Role_Name = "Account Manager", Skill_Name = "Account Management", Proficiency_Level = 1)
        role = RoleTable(Role_Name = "Account Manager", Role_Desc = "Test")
        db.session.add(roleSkill)
        db.session.add(role)
        db.session.add(roleSkill2)
        db.session.add(skill)
        db.session.add(skill2)
        db.session.commit()

        current_role = "Account Manager"
        getRoleSkills = self.client.get(f"/getskillsforrole/{current_role}")
        getRoleSkillsData = json.loads(getRoleSkills.data)
        getProfLevel = self.client.get(f"getrequiredskillsandproficiency/{current_role}")
        getProfLevel = json.loads(getProfLevel.data)
        # print(getProfLevel)
        staffSkill = [
                    {
                        "id": 140002,
                        "isVisible": False,
                        "Proficiency_Level": 0,
                        "Skill_Name": "Accounting and Tax Systems"
                    },
                    {
                        "id": 140002,
                        "isVisible": False,
                        "Proficiency_Level": 0,
                        "Skill_Name": "Business Environment Analysis"
                    },
                    {
                        "id": 140002,
                        "isVisible": False,
                        "Proficiency_Level": 0,
                        "Skill_Name": "Customer Relationship Management"
                    },
                    {
                        "id": 140002,
                        "isVisible": False,
                        "Proficiency_Level": 0,
                        "Skill_Name": "Professional and Business Ethics"
                    }
                ]
        
        self.assertEqual(role_skill_match(staffSkill, getProfLevel)[1], 0)

class Test50RoleMatch(TestApp):
    def testRoleSkillMatch(self):
        skill = SkillTable( Skill_Desc = "Test", Skill_Name = "Account Management")
        skill2 = SkillTable( Skill_Desc = "Test", Skill_Name = "Budgeting")
        roleSkill = RoleSkillTable(Role_Name = "Account Manager", Skill_Name = "Budgeting", Proficiency_Level = 1)
        roleSkill2 = RoleSkillTable(Role_Name = "Account Manager", Skill_Name = "Account Management", Proficiency_Level = 1)
        role = RoleTable(Role_Name = "Account Manager", Role_Desc = "Test")
        db.session.add(roleSkill)
        db.session.add(role)
        db.session.add(roleSkill2)
        db.session.add(skill)
        db.session.add(skill2)
        db.session.commit()

        current_role = "Account Manager"
        getRoleSkills = self.client.get(f"/getskillsforrole/{current_role}")
        getRoleSkillsData = json.loads(getRoleSkills.data)
        getProfLevel = self.client.get(f"getrequiredskillsandproficiency/{current_role}")
        getProfLevel = json.loads(getProfLevel.data)
        # print(getProfLevel)
        staffSkill = [
                    {
                        "id": 140002,
                        "isVisible": False,
                        "Proficiency_Level": 1,
                        "Skill_Name": "Account Management"
                    },
                    {
                        "id": 140002,
                        "isVisible": False,
                        "Proficiency_Level": 0,
                        "Skill_Name": "Business Environment Analysis"
                    },
                    {
                        "id": 140002,
                        "isVisible": False,
                        "Proficiency_Level": 0,
                        "Skill_Name": "Customer Relationship Management"
                    },
                    {
                        "id": 140002,
                        "isVisible": False,
                        "Proficiency_Level": 0,
                        "Skill_Name": "Professional and Business Ethics"
                    }
                ]

        self.assertEqual(role_skill_match(staffSkill, getProfLevel)[1], 50)

class Test100RoleMatch(TestApp):
    def testRoleSkillMatch(self):
        skill = SkillTable( Skill_Desc = "Test", Skill_Name = "Account Management")
        skill2 = SkillTable( Skill_Desc = "Test", Skill_Name = "Budgeting")
        roleSkill = RoleSkillTable(Role_Name = "Account Manager", Skill_Name = "Budgeting", Proficiency_Level = 1)
        roleSkill2 = RoleSkillTable(Role_Name = "Account Manager", Skill_Name = "Account Management", Proficiency_Level = 1)
        role = RoleTable(Role_Name = "Account Manager", Role_Desc = "Test")
        db.session.add(roleSkill)
        db.session.add(role)
        db.session.add(roleSkill2)
        db.session.add(skill)
        db.session.add(skill2)
        db.session.commit()

        current_role = "Account Manager"
        getRoleSkills = self.client.get(f"/getskillsforrole/{current_role}")
        getRoleSkillsData = json.loads(getRoleSkills.data)
        getProfLevel = self.client.get(f"getrequiredskillsandproficiency/{current_role}")
        getProfLevel = json.loads(getProfLevel.data)
        # print(getProfLevel)
        staffSkill = [
                    {
                        "id": 140002,
                        "isVisible": False,
                        "Proficiency_Level": 1,
                        "Skill_Name": "Account Management"
                    },
                    {
                        "id": 140002,
                        "isVisible": False,
                        "Proficiency_Level": 1,
                        "Skill_Name": "Budgeting"
                    },
                    {
                        "id": 140002,
                        "isVisible": False,
                        "Proficiency_Level": 0,
                        "Skill_Name": "Customer Relationship Management"
                    },
                    {
                        "id": 140002,
                        "isVisible": False,
                        "Proficiency_Level": 0,
                        "Skill_Name": "Professional and Business Ethics"
                    }
                ]

        self.assertEqual(role_skill_match(staffSkill, getProfLevel)[1], 100)

class TestRoleSkillBackend0(TestApp):
    def testRoleSkillMatchBackend(self):
        skill = SkillTable( Skill_Desc = "Test", Skill_Name = "Account Management")
        skill2 = SkillTable( Skill_Desc = "Test", Skill_Name = "Budgeting")
        roleSkill = RoleSkillTable(Role_Name = "Account Manager", Skill_Name = "Budgeting", Proficiency_Level = 1)
        roleSkill2 = RoleSkillTable(Role_Name = "Account Manager", Skill_Name = "Account Management", Proficiency_Level = 1)
        role = RoleTable(Role_Name = "Account Manager", Role_Desc = "Test")

        staff = StaffTable(
            Staff_ID = 140002,
            Staff_FName = "Test",
            Staff_LName = "Test",
            Dept = "Engineering",
            Country = "Singapore",
            Email = "test@gmail.com",
            Role = "Developer")
        

        staffSkill = StaffSkillTable(
            Staff_ID = 140002,
            Skill_Name = "Business Acumen",
            isVisible = True,
            Proficiency_Level = 1)
        
        db.session.add(staff)
        db.session.add(staffSkill)
        db.session.add(roleSkill)
        db.session.add(role)
        db.session.add(roleSkill2)
        db.session.add(skill)
        db.session.add(skill2)
        db.session.commit()

        
        current_role = "Account Manager"
        currentStaff = 140002
        getProfLevel = self.client.get(f"getrequiredskillsandproficiency/{current_role}")
        getProfLevel = json.loads(getProfLevel.data)
        staffSkills = self.client.get(f"/getstaffskills/{currentStaff}")
        staffSkills = json.loads(staffSkills.data)

        self.assertEqual(role_skill_match(staffSkills, getProfLevel)[1], 0)


class TestRoleSkillBackend50(TestApp):
    def testRoleSkillMatchBackend(self):
        skill = SkillTable( Skill_Desc = "Test", Skill_Name = "Account Management")
        skill2 = SkillTable( Skill_Desc = "Test", Skill_Name = "Budgeting")
        roleSkill = RoleSkillTable(Role_Name = "Account Manager", Skill_Name = "Budgeting", Proficiency_Level = 1)
        roleSkill2 = RoleSkillTable(Role_Name = "Account Manager", Skill_Name = "Account Management", Proficiency_Level = 1)
        role = RoleTable(Role_Name = "Account Manager", Role_Desc = "Test")

        staff = StaffTable(
            Staff_ID = 140002,
            Staff_FName = "Test",
            Staff_LName = "Test",
            Dept = "Engineering",
            Country = "Singapore",
            Email = "test@gmail.com",
            Role = "Developer")
        

        staffSkill = StaffSkillTable(
            Staff_ID = 140002,
            Skill_Name = "Budgeting",
            isVisible = True,
            Proficiency_Level = 1)
        
        db.session.add(staff)
        db.session.add(staffSkill)
        db.session.add(roleSkill)
        db.session.add(role)
        db.session.add(roleSkill2)
        db.session.add(skill)
        db.session.add(skill2)
        db.session.commit()

        
        current_role = "Account Manager"
        currentStaff = 140002
        getProfLevel = self.client.get(f"getrequiredskillsandproficiency/{current_role}")
        getProfLevel = json.loads(getProfLevel.data)
        staffSkills = self.client.get(f"/getstaffskills/{currentStaff}")
        staffSkills = json.loads(staffSkills.data)

        self.assertEqual(role_skill_match(staffSkills, getProfLevel)[1], 50)


class TestRoleSkillBackend100(TestApp):
    def testRoleSkillMatchBackend(self):
        skill = SkillTable( Skill_Desc = "Test", Skill_Name = "Account Management")
        skill2 = SkillTable( Skill_Desc = "Test", Skill_Name = "Budgeting")
        roleSkill = RoleSkillTable(Role_Name = "Account Manager", Skill_Name = "Budgeting", Proficiency_Level = 1)
        roleSkill2 = RoleSkillTable(Role_Name = "Account Manager", Skill_Name = "Account Management", Proficiency_Level = 1)
        role = RoleTable(Role_Name = "Account Manager", Role_Desc = "Test")

        staff = StaffTable(
            Staff_ID = 140002,
            Staff_FName = "Test",
            Staff_LName = "Test",
            Dept = "Engineering",
            Country = "Singapore",
            Email = "test@gmail.com",
            Role = "Developer")
        

        staffSkill = StaffSkillTable(
            Staff_ID = 140002,
            Skill_Name = "Budgeting",
            isVisible = True,
            Proficiency_Level = 1)
        
        staffSkill2 = StaffSkillTable(
            Staff_ID = 140002,
            Skill_Name = "Account Management",
            isVisible = True,
            Proficiency_Level = 1)
        
        db.session.add(staff)
        db.session.add(staffSkill)
        db.session.add(staffSkill2)
        db.session.add(roleSkill)
        db.session.add(role)
        db.session.add(roleSkill2)
        db.session.add(skill)
        db.session.add(skill2)
        db.session.commit()

        
        current_role = "Account Manager"
        currentStaff = 140002
        getProfLevel = self.client.get(f"getrequiredskillsandproficiency/{current_role}")
        getProfLevel = json.loads(getProfLevel.data)
        staffSkills = self.client.get(f"/getstaffskills/{currentStaff}")
        staffSkills = json.loads(staffSkills.data)

        self.assertEqual(role_skill_match(staffSkills, getProfLevel)[1], 100)


        







if __name__ == '__main__':
    unittest.main()