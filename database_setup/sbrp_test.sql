DROP DATABASE IF EXISTS `SBRP_TEST`;
CREATE DATABASE `SBRP_TEST`;
USE `SBRP_TEST`;

DROP TABLE IF EXISTS `Access_Control`;
CREATE TABLE IF NOT EXISTS `Access_Control` (
  `Access_ID` int NOT NULL,
  `Access_Control_Name` varchar(20) NOT NULL,
  PRIMARY KEY (`Access_ID`)
);

DROP TABLE IF EXISTS `staff`;
CREATE TABLE IF NOT EXISTS `staff` (
  `Staff_ID` int NOT NULL,
  `Staff_FName` varchar(50) NOT NULL,
  `Staff_LName` varchar(50) NOT NULL,
  `Dept` varchar(50) NOT NULL,
  `Country` varchar(50) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Role` int NOT NULL,
  PRIMARY KEY (`Staff_ID`),
  FOREIGN KEY (`Role`) REFERENCES Access_Control(`Access_ID`)
);

DROP TABLE IF EXISTS `Skill`;
CREATE TABLE IF NOT EXISTS `Skill` (
  `Skill_Name` varchar(50) NOT NULL,
  `Skill_Desc` longtext NOT NULL,
  PRIMARY KEY (`Skill_Name`)
);

DROP TABLE IF EXISTS `Role`;
CREATE TABLE IF NOT EXISTS `Role` (
  `Role_Name` varchar(20) NOT NULL,
  `Role_Desc` longtext NOT NULL,
  PRIMARY KEY (`Role_Name`)
);

DROP TABLE IF EXISTS `Staff_Skill`;
CREATE TABLE IF NOT EXISTS `Staff_Skill` (
  `Staff_ID` int NOT NULL,
  `Skill_Name` varchar(50) NOT NULL,
  `isVisible` boolean NOT NULL,
  `Proficiency_Level` int NOT NULL,
  CONSTRAINT PK_Staff_Skill PRIMARY KEY (`Staff_ID`,`Skill_Name`),
  CONSTRAINT FK_Staff_Skill1 FOREIGN KEY (`Staff_ID`) REFERENCES Staff(`Staff_ID`),
  CONSTRAINT FK_Staff_Skill2 FOREIGN KEY (`Skill_Name`) REFERENCES Skill(`Skill_Name`)
);

DROP TABLE IF EXISTS `Role_Skill`;
CREATE TABLE IF NOT EXISTS `Role_Skill` (
  `Role_Name` varchar(20) NOT NULL,
  `Skill_Name` varchar(50) NOT NULL,
  `Proficiency_Level` int NOT NULL,
  CONSTRAINT PK_Role_Skill PRIMARY KEY (`Role_Name`,`Skill_Name`),
  CONSTRAINT FK_Role_Skill1 FOREIGN KEY (`Role_Name`) REFERENCES Role(`Role_Name`),
  CONSTRAINT FK_Role_Skill2 FOREIGN KEY (`Skill_Name`) REFERENCES Skill(`Skill_Name`)
);

DROP TABLE IF EXISTS `Role_Listing`;
CREATE TABLE IF NOT EXISTS `Role_Listing` (
  `Listing_ID` int NOT NULL AUTO_INCREMENT,
  `Role_Name` varchar(20) NOT NULL,
  `Country` varchar(20) NOT NULL,
  `Department` varchar(50) NOT NULL,
  `Reporting_Manager` int NOT NULL,
  `Open_Window` datetime NOT NULL,
  `Close_Window` datetime NOT NULL,
PRIMARY KEY (`Listing_ID`),
FOREIGN KEY (`Reporting_Manager`) REFERENCES Staff(`Staff_ID`),
FOREIGN KEY (`Role_Name`) REFERENCES Role_Skill(`Role_Name`)
);

DROP TABLE IF EXISTS `Application`;
CREATE TABLE IF NOT EXISTS `Application` (
  `Application_ID` int NOT NULL AUTO_INCREMENT,
  `Listing_ID` int NOT NULL,
  `Staff_ID` int NOT NULL,
  `Brief_Description` longtext,
  PRIMARY KEY (`Application_ID`),
  FOREIGN KEY (`Listing_ID`) REFERENCES Role_Listing(`Listing_ID`),
  FOREIGN KEY (`Staff_ID`) REFERENCES Staff(`Staff_ID`)
);

/*Insert Mockup Values*/

LOAD DATA INFILE "c:/wamp64/tmp/SBRP/Access_Control.csv"
INTO TABLE Access_Control
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

LOAD DATA INFILE "c:/wamp64/tmp/SBRP/role.csv"
INTO TABLE Role
CHARACTER SET latin1
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

LOAD DATA INFILE "c:/wamp64/tmp/SBRP/skill.csv"
INTO TABLE Skill
CHARACTER SET latin1
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

LOAD DATA INFILE "c:/wamp64/tmp/SBRP/role_skill.csv"
INTO TABLE Role_Skill
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

LOAD DATA INFILE "c:/wamp64/tmp/SBRP/staff.csv"
INTO TABLE Staff
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

LOAD DATA INFILE "c:/wamp64/tmp/SBRP/staff_skill.csv"
INTO TABLE Staff_Skill
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;