from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# SQLAlchemy configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost/sbrp_test'
db = SQLAlchemy(app)

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

@app.route('/all', methods=['GET'])
def get_data():
    try:
        # Fetch data from the database using SQLAlchemy
        data = RoleListingTable.query.all()
        data_dict = [{'id': item.Listing_ID, 'name': item.Role_Name, 'country' : item.Country, 'dept' : item.Department, 'OpenW' : item.Open_Window, 'CloseW': item.Close_Window } for item in data]
        return jsonify(data_dict)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
