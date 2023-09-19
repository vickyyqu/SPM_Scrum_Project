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
)