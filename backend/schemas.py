from config import *

##### DB Tables ######

class RoleListingTable(db.Model):
    __tablename__ = 'Role_Listing'  # Replace with your table name
    # Define your table columns here
    Listing_ID = db.Column(db.Integer, primary_key=True)
    Role_Name = db.Column(db.String(255), db.ForeignKey('Role_Skill.Role_Name'))
    Country = db.Column(db.String(255))
    Department =db.Column(db.String(255))
    Reporting_Manager = db.Column(db.String(255))
    Open_Window = db.Column(db.DateTime)
    Close_Window = db.Column(db.DateTime)
    # Add more columns as needed

class RoleSkillTable(db.Model):
    __tablename__ = "Role_Skill"
    Role_Name = db.Column(db.String(255), db.ForeignKey('Role.Role_Name'), primary_key=True)
    Skill_Name = db.Column(db.String(255), db.ForeignKey('Skill.Skill_Name'), primary_key=True)
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

class RoleTable(db.Model):
    __tablename__ = 'Role'  # Replace with your table name
    # Define your table columns here
    Role_Name = db.Column(db.String(255), primary_key=True)
    Role_Desc = db.Column(db.String(255))
    # Add more columns as needed

class StaffTable(db.Model):
    __tablename__ = 'Staff'  # Replace with your table name
    # Define your table columns here
    Staff_ID = db.Column(db.Integer, primary_key=True)
    Staff_FName = db.Column(db.String(50))
    Staff_LName = db.Column(db.String(50))
    Dept = db.Column(db.String(50))
    Country = db.Column(db.String(50))
    Email = db.Column(db.String(50))
    Role = db.Column(db.Integer)

class ApplicationTable(db.Model):
    __tablename__ = 'Application'  # Replace with your table name
    # Define your table columns here
    Application_ID = db.Column(db.Integer, primary_key = True)
    Listing_ID = db.Column(db.Integer)
    Staff_ID = db.Column(db.Integer)
    Brief_Description = db.Column(db.String(255))