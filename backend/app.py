from config import *
from schemas import *
from datetime import datetime

##### API Endpoints ######

# Role_Listing


@app.route('/getallrolelistings', methods=['GET'])
def get_allrolelistings():
    try:
        # Fetch data from the database using SQLAlchemy
        data = RoleListingTable.query.all()
        data_dict = [{'id': item.Listing_ID, 'name': item.Role_Name, 'country': item.Country,
                      'dept': item.Department, 'OpenW': item.Open_Window, 'CloseW': item.Close_Window} for item in data]
        return jsonify(data_dict)
    except Exception as e:
        return jsonify({'error': str(e)})
    

@app.route('/getstaffrolelistings', methods=['GET'])
def get_all_role_listings():
    try:
        # Get today's date
        today_date = datetime.now().date()

        # Fetch data from the database using SQLAlchemy
        data = RoleListingTable.query.filter(RoleListingTable.Close_Window >= today_date).all()

        data_dict = [{'id': item.Listing_ID, 'name': item.Role_Name, 'country': item.Country,
                      'dept': item.Department, 'OpenW': item.Open_Window, 'CloseW': item.Close_Window} for item in data]

        return jsonify(data_dict)
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/addrolelisting', methods=['POST'])
def add_rolelisting():
    try:
        data = request.get_json()
        print(data)
        new_role_listing = RoleListingTable(
            Role_Name = data['roleName']['roleName'],
            Country = data['country'],
            Department = data['dept'],
            Reporting_Manager = data['reportingManager'],
            Open_Window = data['openWindow'],
            Close_Window = data['closeWindow'])
        db.session.add(new_role_listing)
        db.session.commit()
        return jsonify({'message': 'Data added successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to add data.', 'details': str(e)}), 500


# Role_Skill
@app.route('/getallroleskills', methods=['GET'])
def get_allroleskills():
    try:
        # Fetch data from the database using SQLAlchemy
        data = RoleSkillTable.query.all()
        data_dict = [{'name': item.Role_Name, 'skill': item.Skill_Name,
                      'proficiency': item.Proficiency_Level} for item in data]
        return jsonify(data_dict)
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/getroleskills/<string:listing_id>', methods=['GET'])
def get_roleskills(listing_id):
    try:
        # Fetch data from the database using SQLAlchemy
        listing = RoleListingTable.query.filter_by(
            Listing_ID=listing_id).first()
        if not listing:
            return jsonify(
                {
                    "code": 404,
                    "error": "Listing does not exist."
                }), 501
        
        role = listing.Role_Name
        data = RoleSkillTable.query.filter_by(Role_Name=role)
        data_dict = [{'skill' : item.Skill_Name, 'proficiency' : item.Proficiency_Level } for item in data]
        
        return jsonify(data_dict), 201
    
    except Exception as e:
        return jsonify({'error': str(e)}), 501
    
# Staff_Skill


@app.route('/getstaffskills/<string:staff_id>', methods=['GET'])
def get_staffskills(staff_id):
    try:
        # Fetch data from the database using SQLAlchemy
        data = StaffSkillTable.query.filter_by(Staff_ID=staff_id)
        data_dict = [{'id': item.Staff_ID, 'skill': item.Skill_Name,
                      'isVisible': item.isVisible, 'proficiency': item.Proficiency_Level} for item in data]

        if data_dict == []:
            return jsonify(
                {
                    "code": 404,
                    "error": "Staff is invalid or staff has no skills registered."
                }), 501
        
        return jsonify(data_dict), 201
    
    except Exception as e:
        return jsonify({'error': str(e)}), 501

# Skill


@app.route('/getallskills', methods=['GET'])
def get_allskills():
    try:
        # Fetch data from the database using SQLAlchemy
        data = SkillTable.query.all()
        data_dict = [{'skillName': item.Skill_Name,
                      'skillDesc': item.Skill_Desc} for item in data]
        return jsonify(data_dict)
    except Exception as e:
        return jsonify({'error': str(e)})


# Role
@app.route('/getallroles', methods=['GET'])
def get_allroles():
    try:
        # Fetch data from the database using SQLAlchemy
        data = RoleTable.query.all()
        data_dict = [{'roleName': item.Role_Name,
                      'roleDesc': item.Role_Desc} for item in data]
        return jsonify(data_dict)
    except Exception as e:
        return jsonify({'error': str(e)})

# Staff


@app.route('/getallstaffs', methods=['GET'])
def get_allstaff():
    try:
        # Fetch data from the database using SQLAlchemy
        data = StaffTable.query.all()
        data_dict = [{'staffID': item.Staff_ID, 'staffFName': item.Staff_FName, 'staffLName': item.Staff_LName,
                      'staffDept': item.Dept, 'staffCountry': item.Country, 'staffEmail': item.Email, 'staffRole': item.Role} for item in data]
        return jsonify(data_dict)
    except Exception as e:
        return jsonify({'error': str(e)})

# Managers


@app.route('/getallmanagers', methods=['GET'])
def get_allmanagers():
    try:
        # Fetch data from the database using SQLAlchemy
        data = StaffTable.query.filter_by(Role=3).all()
        data_dict = [{'staffID': item.Staff_ID, 'staffFName': item.Staff_FName, 'staffLName': item.Staff_LName,
                      'staffDept': item.Dept, 'staffCountry': item.Country, 'staffEmail': item.Email, 'staffRole': item.Role} for item in data]
        return jsonify(data_dict)
    except Exception as e:
        return jsonify({'error': str(e)})

# Role_Listing by Listing_ID


@app.route('/getrolelisting/<int:listing_id>', methods=['GET'])
def get_rolelisting(listing_id):
    try:
        # Fetch data from the database using SQLAlchemy
        data = RoleListingTable.query.filter_by(Listing_ID=listing_id).all()
        data_dict = [{'id': item.Listing_ID, 'name': item.Role_Name, 'country': item.Country, 'dept': item.Department,
                      'reportingManager': item.Reporting_Manager, 'OpenW': item.Open_Window, 'CloseW': item.Close_Window} for item in data]

        if data_dict == []:
            return jsonify(
                {
                    "code": 404,
                    "error": "Listing does not exist."
                })

        return jsonify(data_dict)

    except Exception as e:
        return jsonify({'error': str(e)})

# Update Role_Listing


@app.route('/updaterolelisting/<int:listing_id>', methods=['POST'])
def put_rolelisting(listing_id):
    try:
        data = request.get_json()
        listing = RoleListingTable.query.filter_by(
            Listing_ID=listing_id).first()

        if listing is not None:
            listing.Role_Name = data['roleName']
            listing.Country = data['country']
            listing.Department = data['dept']
            listing.Reporting_Manager = data['reportingManager']
            listing.Open_Window = data['openWindow']
            listing.Close_Window = data['closeWindow']

            db.session.commit()
            return jsonify({"message": "Listing updated successfully"}), 200
        else:
            return jsonify({"message": "Listing does not exist"}), 404

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to update listing.', 'details': str(e)}), 500

# get all skills for a role


@app.route('/getskillsforrole/<string:role_name>', methods=['GET'])
def get_skills_for_role(role_name):
    try:
        print(role_name)
        # Perform a join query to retrieve Skill_Name and Skill_Desc based on Role_Name
        skills_for_role = (
            db.session.query(SkillTable.Skill_Name, SkillTable.Skill_Desc)
            .join(RoleSkillTable, RoleSkillTable.Skill_Name == SkillTable.Skill_Name)
            .filter(RoleSkillTable.Role_Name == role_name)
            .all()
        )

        result = [{'Skill_Name': skill_name, 'Skill_Desc': skill_desc}
                  for skill_name, skill_desc in skills_for_role]

        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': 'Failed to retrieve skills for role.', 'details': str(e)}), 500

# get role desc from role name


@app.route('/getroledesc/<string:role_name>', methods=['GET'])
def get_roledesc(role_name):
    try:
        print(role_name)
        # Perform a join query to retrieve Skill_Name and Skill_Desc based on Role_Name
        skills_for_role = (
            db.session.query(RoleTable.Role_Name, RoleTable.Role_Desc)
            .join(RoleSkillTable, RoleSkillTable.Role_Name == RoleTable.Role_Name)
            .filter(RoleSkillTable.Role_Name == role_name)
            .first()
        )

        result = {'Role_Desc': skills_for_role[1]}

        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': 'Failed to retrieve role desc for role.', 'details': str(e)}), 500


# get all roles that matches role name search
@app.route('/getroles/<string:role_name_search>', methods=['GET'])
def get_roles_matching_role(role_name_search):
    try:
        # Perform a join query to retrieve Skill_Name and Skill_Desc based on Role_Name
        roles_matching_search = (
            db.session.query(RoleTable.Role_Name)
            .filter(RoleTable.Role_Name.like(f"%{role_name_search}%"))
            .all()
        )

        print(roles_matching_search)

        result = [role_name._asdict()
                  for role_name in roles_matching_search]

        return jsonify(result), 200
    
    except Exception as e:
        return jsonify({'error': 'Failed to retrieve roles matching role name.', 'details': str(e)}), 500
    

# get required skills and proficiency by role name
@app.route('/getrequiredskillsandproficiency/<string:role_name>', methods=['GET'])
def get_skill_and_proficiency_for_role(role_name):
    try:
        #Perform a join query to retrieve Skill_Name and Proficiency_Level based on Role_Name
        skills_and_proficiency_for_role = (
            db.session.query(RoleSkillTable.Skill_Name, RoleSkillTable.Proficiency_Level)
            .filter(RoleSkillTable.Role_Name == role_name)
            .all()
        )

        result = [{'Skill_Name': skill_name, 'Proficiency_Level': proficiency_level }
                  for skill_name, proficiency_level in skills_and_proficiency_for_role]

        return jsonify(result), 200

    
    except Exception as e:
        return jsonify({'error': 'Failed to retrieve skills for role.', 'details': str(e)}), 500


    try:
        data = request.get_json()
        listing = RoleListingTable.query.filter_by(
            Listing_ID=listing_id).first()

        if listing is not None:
            listing.Role_Name = data['roleName']
            listing.Country = data['country']
            listing.Department = data['dept']
            listing.Reporting_Manager = data['reportingManager']
            listing.Open_Window = data['openWindow']
            listing.Close_Window = data['closeWindow']

            db.session.commit()
            return jsonify({"message": "Listing updated successfully"}), 200
        else:
            return jsonify({"message": "Listing does not exist"}), 404

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to update listing.', 'details': str(e)}), 500
    
@app.route('/getappliedstatus/<int:listing_id>&<int:staff_id>', methods=['GET'])
def getappliedstatus(listing_id, staff_id):
    try:
        # Fetch data from the database using SQLAlchemy
        application = (db.session.query(ApplicationTable.Application_ID)
            .filter(ApplicationTable.Listing_ID == listing_id, ApplicationTable.Staff_ID == staff_id)
            .first()
        )
        
        if application != None:
            application_dict = {"Application_ID": application[0]}
            return jsonify(application_dict)
    
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/getapplicationsbylistingid/<int:listing_id>', methods=['GET'])
def getapplicationsbylistingid(listing_id):
    try:
        # Fetch data from the database using SQLAlchemy
        data = ApplicationTable.query.filter_by(Listing_ID=listing_id).all()
        data_dict = []
        for i in range(len(data)):
            staff_name = db.session.query(StaffTable.Staff_FName, StaffTable.Staff_LName).filter_by(Staff_ID=data[i].Staff_ID).first()
            data_dict.append({'application_id': data[i].Application_ID, 'listing_id': data[i].Listing_ID, 'staff_id': data[i].Staff_ID, 'staff_fname': staff_name.Staff_FName, 'staff_lname': staff_name.Staff_LName, 'brief_description': data[i].Brief_Description})

        if data_dict == []:
            return jsonify(
                {
                    "code": 404,
                    "error": "Applications do not exist."
                })

        return jsonify(data_dict)

    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/delete_application/<int:listing_id>&<int:staff_id>', methods=['DELETE'])
def delete_application(listing_id, staff_id):
    try:
        data = ApplicationTable.query.filter_by(Listing_ID=listing_id, Staff_ID = staff_id).first()
        db.session.delete(data)
        db.session.commit()
        return jsonify({'message': 'Data deleted successfully!'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to delete data.', 'details': str(e)}), 500
    

@app.route('/apply_role', methods=['POST'])
def apply_role():
    try:
        data = request.get_json()
        new_data = ApplicationTable(
            Listing_ID = data['listing_ID'], 
            Staff_ID = data['staff_ID'], 
            Brief_Description = data['brief_description']
        )
        db.session.add(new_data)
        db.session.commit()
        return jsonify({'message': 'Data added successfully!'}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to add data.', 'details': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
