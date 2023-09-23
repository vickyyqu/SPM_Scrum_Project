DROP DATABASE IF EXISTS `SBRP`;
CREATE DATABASE `SBRP`;
USE `SBRP`;

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

DROP TABLE IF EXISTS `Staff_Skill`;
CREATE TABLE IF NOT EXISTS `Staff_Skill` (
  `Staff_ID` int NOT NULL,
  `Skill_Name` varchar(50) NOT NULL,
  `isVisible` boolean NOT NULL,
  CONSTRAINT PK_Staff_Skill PRIMARY KEY (`Staff_ID`,`Skill_Name`)
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

DROP TABLE IF EXISTS `Role_Skill`;
CREATE TABLE IF NOT EXISTS `Role_Skill` (
  `Role_Name` varchar(20) NOT NULL,
  `Skill_Name` varchar(50) NOT NULL,
  CONSTRAINT PK_Role_Skill PRIMARY KEY (`Role_Name`,`Skill_Name`)
);

DROP TABLE IF EXISTS `Role_Listing`;
CREATE TABLE IF NOT EXISTS `Role_Listing` (
  `Listing_ID` int NOT NULL,
  `Role_Name` varchar(20) NOT NULL,
  `Country` varchar(20) NOT NULL,
  `Department` varchar(50) NOT NULL,
  `Reporting Manager` int NOT NULL,
  `Open_Window` datetime NOT NULL,
  `Close_Window` datetime NOT NULL,
PRIMARY KEY (`Listing_ID`),
FOREIGN KEY (`Reporting Manager`) REFERENCES Staff(`Staff_ID`),
FOREIGN KEY (`Role_Name`) REFERENCES Role_Skill(`Role_Name`)
);

DROP TABLE IF EXISTS `Application`;
CREATE TABLE IF NOT EXISTS `Application` (
  `Application_ID` int NOT NULL,
  `Listing_ID` int NOT NULL,
  `Staff_ID` int NOT NULL,
  `Brief_Description` longtext,
  PRIMARY KEY (`Application_ID`),
  FOREIGN KEY (`Listing_ID`) REFERENCES Role_Listing(`Listing_ID`),
  FOREIGN KEY (`Staff_ID`) REFERENCES Staff(`Staff_ID`)
);

/*Insert Mockup Values*/

INSERT INTO access_control VALUES
(1, "Staff"),
(2, "HR"),
(3, "Manager"),
(4, "Director");

INSERT INTO staff VALUES
(1, "David", "Beckham", "IT", "Singapore", "davidbeckham@gmail.com", 1),
(2, "Huisoo", "Jang", "Finance", "Singapore", "janghuisoo@gmail.com", 1),
(3, "Joseph", "Lim", "Finance", "Singapore", "josephlim@gmail.com", 2),
(4, "Christina", "Frye", "IT", "Singapore", "chrisfrye@gmail.com", 3);

INSERT INTO staff_skill VALUES
(1, "Programming and Coding", true),
(1, "Product Design and Development", true),
(2, "Pricing Strategy", true),
(3, "Pricing Strategy", true),
(3, "Billing and Data Risk Management", true),
(4, "Programming and Coding", true),
(4, "Product Design and Development", true);

INSERT INTO skill VALUES
("Programming and Coding", "Apply macros, programming and coding to meet business needs"),
("Robotics and Automation Application", "Apply procedural knowledge of robotic systems and automation technologies to execute operational activities"),
("Pricing Strategy", "Analyse market environment and trends to identify and assess impact of internal and external factors on product and solutions pricing and the effectiveness of pricing policies against competitors"),
("Product Design and Development", "Establish new product development strategies and plans to manage new product design and development "),
("Billing and Data Risk Management", "Identify potential risks for customer billing and data");

INSERT INTO role VALUES
("Audit Manager", "The Audit Senior Manager/Audit Manager manages a portfolio of engagements to deliver high quality audit services. He/she also provides leadership on audit engagements which includes client acceptance process, engagement planning, execution and finalisation of an audit engagement. He is fully accountable for the audit engagement and ensures that the engagement progress against budget and timeline is closely monitored. He also serves to develop and maintain long-term client relationships and value-add to the audit firm by identifying new business development opportunities. The Audit Senior Manager/Audit Manager reviews and provides key technical expertise to ensure the quality of audit work performed is in compliance with professional standards and requirements. He contributes towards continuous improvement in audit methodology and process. He will also assume a greater role in professional development activities such as training, staff recruitment and resource planning"),
("Accountant", "The Accountant/Senior Accounts Executive is involved in most, if not all, aspects of accounting and oversees the day-to-day activities of the accounting team. He/she ensures that the organisation's finance function is well organised as well as produces timely and accurate financial statements and management accounts, thus achieving compliance with corporate policies and statutory requirements. He must also analyse data and understand the financial performance and position of the organisation in order to develop suitable accounting policies to meet reporting requirements and to produce any special reports required by the management team. The Accountant/Senior Accounts Executive often leads a team of finance and accounting specialists and works closely with the internal and external auditors, bankers, and regulators. He must keep current with changing statutory requirements and tax laws and determine the implications of such changes to financial reporting. He may also work with the leadership team to help define the organisations overall finance strategy."),
("Back End Developer", "The Back End Developer codes and develops server-side systems to support core product functionality and offering. He/She identifies security risks and ensures coding standards meet security requirements. He executes specifications and features for the next iteration of the product based on user needs and feedback, and continuously integrates code changes. He provides support to the quality testing teams."),
("Full Stack Developer", "The Full Stack Developer codes and develops both front-end and back-end systems that balance product functionality with user experience and needs. He/She gathers user feedback to develop an intuitive and responsive experience for end users. He identifies security risks and ensures coding standards meet security requirements. He supports usability testing to validate user interfaces. He executes specifications and features for the next iteration of the product based on user needs and feedback, and continuously integrates code changes. He provides support to the quality testing teams.");

INSERT INTO role_skill VALUES
("Audit Manager", "Billing and Data Risk Management"),
("Audit Manager", "Product Design and Development"),
("Accountant", "Billing and Data Risk Management"),
("Accountant", "Product Design and Development"),
("Back End Developer", "Programming and Coding"),
("Back End Developer", "Product Design and Development"),
("Full Stack Developer", "Programming and Coding"),
("Full Stack Developer", "Product Design and Development");

INSERT INTO role_listing VALUES
(1, "Full Stack Developer", "Singapore", "IT", 4, "2023-09-22", "2023-10-29"),
(2, "Back End Developer", "Singapore", "IT", 4, "2023-09-22", "2023-10-29");

INSERT INTO application VALUES
(1, 1, 2, "I am interested"),
(2, 2, 1, "I am interested");