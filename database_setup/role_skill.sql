DROP TABLE IF EXISTS `Role_Skill`;
CREATE TABLE IF NOT EXISTS `Role_Skill` (
  `Role_Name` varchar(20) NOT NULL,
  `Skill_Name` varchar(50),
  CONSTRAINT PK_Role_Skill PRIMARY KEY (`Role_Name`,`Skill_Name`)
)