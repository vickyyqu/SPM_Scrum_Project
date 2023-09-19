DROP TABLE IF EXISTS `Staff_Skill`;
CREATE TABLE IF NOT EXISTS `Staff_Skill` (
  `Staff_ID` int NOT NULL,
  `Skill_Name` varchar(20),
  CONSTRAINT PK_Staff_Skill PRIMARY KEY (`Staff_ID`,`Skill_Name`)
)