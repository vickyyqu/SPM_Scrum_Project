DROP TABLE IF EXISTS `Skill`;
CREATE TABLE IF NOT EXISTS `Skill` (
  `Skill_Name` varchar(50) NOT NULL,
  `Skill_Desc` longtext,
  PRIMARY KEY (`Skill_Name`)
)