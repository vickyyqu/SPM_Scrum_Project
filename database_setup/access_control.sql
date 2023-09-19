DROP TABLE IF EXISTS `Access_Control`;
CREATE TABLE IF NOT EXISTS `Access_Control` (
  `Access_ID` int NOT NULL,
  `Access_Control_Name` varchar(20),
  PRIMARY KEY (`Access_ID`)
)