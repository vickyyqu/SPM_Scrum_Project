from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# SQLAlchemy configuration
# change accordingly whether you have "root" or "" as DB password
# method naming: get, put, post, delete
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/sbrp_test'
db = SQLAlchemy(app)


class RoleListingTable(db.Model):
    __tablename__ = 'Role_Listing'  # Replace with your table name
    # Define your table columns here
    Listing_ID = db.Column(db.Integer, primary_key=True)
    Role_Name = db.Column(db.String(255))
    Country = db.Column(db.String(255))
    Department = db.Column(db.String(255))
    Open_Window = db.Column(db.DateTime)
    Close_Window = db.Column(db.DateTime)
    # Add more columns as needed


@app.route('/getAllRoleListings', methods=['GET'])
def get_all_role_listings():
    try:
        # Fetch data from the database using SQLAlchemy
        data = RoleListingTable.query.all()
        data_dict = [{'id': item.Listing_ID, 'name': item.Role_Name, 'country': item.Country,
            'dept': item.Department, 'OpenW': item.Open_Window, 'CloseW': item.Close_Window} for item in data]
        return jsonify(data_dict)
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/postRoleListings', methods=['POST'])
def post_role_listings():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')

    if title and content:
        new_post = Post(title=title, content=content)
        db.session.add(new_post)
        db.session.commit()
        return jsonify({'message': 'Post created successfully'})
    else:
        return jsonify({'error': 'Invalid data'}), 400


    try:
        # Fetch data from the database using SQLAlchemy
        data = RoleListingTable.query.all()
        data_dict = [{'id': item.Listing_ID, 'name': item.Role_Name, 'country' : item.Country, 'dept' : item.Department, 'OpenW' : item.Open_Window, 'CloseW': item.Close_Window } for item in data]
        return jsonify(data_dict)
    except Exception as e:
        return jsonify({'error': str(e)})


class SkillTable(db.Model):
    __tablename__ = 'Skill'  # Replace with your table name
    # Define your table columns here
    Skill_Name = db.Column(db.String(255), primary_key=True)
    Skill_Desc = db.Column(db.String(255))
    # Add more columns as needed


@app.route('/getAllSkills', methods=['GET'])
def get_all_skills():
    try:
        # Fetch data from the database using SQLAlchemy
        data = SkillTable.query.all()
        data_dict = [{ 'skillName': item.Skill_Name, 'skillDesc': item.Skill_Desc } for item in data]
        return jsonify(data_dict)
    except Exception as e:
        return jsonify({'error': str(e)})




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
