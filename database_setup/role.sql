DROP TABLE IF EXISTS `Role`;
CREATE TABLE IF NOT EXISTS `Role` (
  `Role_Name` varchar(20) NOT NULL,
  `Role_Desc` longtext,
  PRIMARY KEY (`Role_Name`)
)