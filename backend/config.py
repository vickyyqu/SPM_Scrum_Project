from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv
import os

# Load db variable from .env file into environment
load_dotenv()
database_url = os.getenv("DATABASE_URL")

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# SQLAlchemy configuration
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost/sbrp_test'
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
db = SQLAlchemy(app)

#testing to push to github pls ignore -- will delete