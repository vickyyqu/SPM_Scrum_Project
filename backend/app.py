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
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)