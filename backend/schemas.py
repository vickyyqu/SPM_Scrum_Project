from config import *

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

class SkillTable(db.Model):
    __tablename__ = 'Skill'  # Replace with your table name
    # Define your table columns here
    Skill_Name = db.Column(db.String(255), primary_key=True)
    Skill_Desc = db.Column(db.String(255))
    # Add more columns as needed