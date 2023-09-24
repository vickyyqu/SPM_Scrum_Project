from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# SQLAlchemy configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost/sbrp_test'
db = SQLAlchemy(app)

##### DB Tables ######

class RoleListingTable(db.Model):
    __tablename__ = 'Role_Listing'  # Replace with your table name
    # Define your table columns here
    Listing_ID = db.Column(db.Integer, primary_key=True)
    Role_Name = db.Column(db.String(255))
    Country = db.Column(db.String(255))
    Department =db.Column(db.String(255))
    Open_Window = db.Column(db.DateTime)
    Close_Window = db.Column(db.DateTime)
    # Add more columns as needed

class RoleSkillTable(db.Model):
    __tablename__ = "Role_Skill"
    Role_Name = db.Column(db.String(255), primary_key=True)
    Skill_Name = db.Column(db.String(255), primary_key=True)
    Proficiency_Level = db.Column(db.Integer)

class StaffSkillTable(db.Model):
    __tablename__ = "Staff_Skill"
    Staff_ID = db.Column(db.String(255), primary_key=True)
    Skill_Name = db.Column(db.String(255), primary_key=True)
    isVisible = db.Column(db.Boolean)
    Proficiency_Level = db.Column(db.Integer)


##### API Endpoints ######

@app.route('/all', methods=['GET'])
def get_data():
    try:
        # Fetch data from the database using SQLAlchemy
        data = RoleListingTable.query.all()
        data_dict = [{'id': item.Listing_ID, 'name': item.Role_Name, 'country' : item.Country, 'dept' : item.Department, 'OpenW' : item.Open_Window, 'CloseW': item.Close_Window } for item in data]
        return jsonify(data_dict)
    except Exception as e:
        return jsonify({'error': str(e)})
    

@app.route('/allskills', methods=['GET'])
def get_allskills():
    try:
        # Fetch data from the database using SQLAlchemy
        data = RoleSkillTable.query.all()
        data_dict = [{'name': item.Role_Name, 'skill' : item.Skill_Name, 'proficiency' : item.Proficiency_Level } for item in data]
        return jsonify(data_dict)
    except Exception as e:
        return jsonify({'error': str(e)})
    
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
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)