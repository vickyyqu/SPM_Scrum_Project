from config import *
from schemas import *

##### API Endpoints ######

#Role_Listing
@app.route('/getallrolelistings', methods=['GET'])
def get_allrolelistings():
    try:
        # Fetch data from the database using SQLAlchemy
        data = RoleListingTable.query.all()
        data_dict = [{'id': item.Listing_ID, 'name': item.Role_Name, 'country' : item.Country, 'dept' : item.Department, 'OpenW' : item.Open_Window, 'CloseW': item.Close_Window } for item in data]
        return jsonify(data_dict)
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/postrolelisting', methods=['POST'])
def post_rolelisting():
    try:
        data = request.get_json()
        new_data = RoleListingTable(Role_Name=data['roleName'], Country=data['country'], Department=data['dept'], Reporting_Manager=data['reportingManager'], Open_Window=data['openWindow'], Close_Window=data['closeWindow'])
        db.session.add(new_data)
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
        data_dict = [{'name': item.Role_Name, 'skill' : item.Skill_Name, 'proficiency' : item.Proficiency_Level } for item in data]
        return jsonify(data_dict)
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/getroleskills/<string:listing_id>', methods=['GET'])
def get_roleskills(listing_id):
    try:
        # Fetch data from the database using SQLAlchemy
        listing = RoleListingTable.query.filter_by(Listing_ID=listing_id).first()
        if not listing:
            return jsonify(
                {
                    "code": 404,
                    "error": "Listing does not exist."
                })
        
        role = listing.Role_Name
        data = RoleSkillTable.query.filter_by(Role_Name=role)
        data_dict = [{'skill' : item.Skill_Name, 'proficiency' : item.Proficiency_Level } for item in data]
        
        return jsonify(data_dict)
    
    except Exception as e:
        return jsonify({'error': str(e)})
    
# Staff_Skill
@app.route('/getstaffskills/<string:staff_id>', methods=['GET'])
def get_staffskills(staff_id):
    try:
        # Fetch data from the database using SQLAlchemy
        data = StaffSkillTable.query.filter_by(Staff_ID=staff_id)
        data_dict = [{'id': item.Staff_ID, 'skill' : item.Skill_Name, 'isVisible' : item.isVisible, 'proficiency' : item.Proficiency_Level } for item in data]

        if data_dict == []:
            return jsonify(
                {
                    "code": 404,
                    "error": "Staff is invalid or staff has no skills registered."
                })
        
        return jsonify(data_dict)
    
    except Exception as e:
        return jsonify({'error': str(e)})

# Skill
@app.route('/getallskills', methods=['GET'])
def get_allskills():
    try:
        # Fetch data from the database using SQLAlchemy
        data = SkillTable.query.all()
        data_dict = [{ 'skillName': item.Skill_Name, 'skillDesc': item.Skill_Desc } for item in data]
        return jsonify(data_dict)
    except Exception as e:
        return jsonify({'error': str(e)})
    

# Role
@app.route('/getallroles', methods=['GET'])
def get_allroles():
    try:
        # Fetch data from the database using SQLAlchemy
        data = RoleTable.query.all()
        data_dict = [{'roleName': item.Role_Name, 'roleDesc': item.Role_Desc } for item in data]
        return jsonify(data_dict)
    except Exception as e:
        return jsonify({'error': str(e)})

# Staff
@app.route('/getallstaffs', methods=['GET'])
def get_allstaff():
    try:
        # Fetch data from the database using SQLAlchemy
        data = StaffTable.query.all()
        data_dict = [{'staffID': item.Staff_ID, 'staffFName': item.Staff_FName, 'staffLName': item.Staff_LName, 'staffDept': item.Dept, 'staffCountry': item.Country, 'staffEmail': item.Email, 'staffRole': item.Role } for item in data]
        return jsonify(data_dict)
    except Exception as e:
        return jsonify({'error': str(e)})

# Managers
@app.route('/getallmanagers', methods=['GET'])
def get_allmanagers():
    try:
        # Fetch data from the database using SQLAlchemy
        data = StaffTable.query.filter_by(Role=3).all()
        data_dict = [{'staffID': item.Staff_ID, 'staffFName': item.Staff_FName, 'staffLName': item.Staff_LName, 'staffDept': item.Dept, 'staffCountry': item.Country, 'staffEmail': item.Email, 'staffRole': item.Role } for item in data]
        return jsonify(data_dict)
    except Exception as e:
        return jsonify({'error': str(e)})
    
# Role_Listing by Listing_ID
@app.route('/getrolelisting/<int:listing_id>', methods=['GET'])
def get_rolelisting(listing_id):
    try:
        # Fetch data from the database using SQLAlchemy
        data = RoleListingTable.query.filter_by(Listing_ID=listing_id).all()
        data_dict = [{'id': item.Listing_ID, 'name': item.Role_Name, 'country' : item.Country, 'dept' : item.Department, 'OpenW' : item.Open_Window, 'CloseW': item.Close_Window } for item in data]

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
        listing = RoleListingTable.query.filter_by(Listing_ID=listing_id).first()
        
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

        result = [{'Skill_Name': skill_name, 'Skill_Desc': skill_desc} for skill_name, skill_desc in skills_for_role]

        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': 'Failed to retrieve skills for role.', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)