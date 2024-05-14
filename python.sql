  CREATE DATABASE SMARTHOME

  USE SMARTHOME

  CREATE TABLE User (
    idUser int PRIMARY KEY AUTO_INCREMENT,
    nameUser varchar(50),
    dateUser DATETIME DEFAULT CURRENT_TIMESTAMP(),
    phoneUser varchar(10) UNIQUE,
    Username varchar(100) UNIQUE,
    Password varchar(100)
  );

  CREATE TABLE Command (
    idCommand int PRIMARY KEY AUTO_INCREMENT,
    nameCommand varchar(200)
  );

  CREATE TABLE Device (
    idDevice int PRIMARY KEY AUTO_INCREMENT,
    nameDevice varchar(200),
    typeDevice varchar(50),
    status int,
    position varchar(50)

  );

  CREATE TABLE PortDevice (
    idPort int PRIMARY KEY AUTO_INCREMENT,
    portNum int,
    idDevice int
  );

  CREATE TABLE Functions (
    idFunction int PRIMARY KEY AUTO_INCREMENT,
    nameFunction varchar(200),
    idCommand int
  );

  CREATE TABLE ParticularFunction (
    idFunction int,
    idDevice int
  );

  CREATE TABLE LISTTIME (
    idDevice INT,
    time DATETIME
  );

  ALTER TABLE PortDevice add  FOREIGN KEY (idDevice) REFERENCES Device (idDevice) on DELETE CASCADE;
  ALTER TABLE Functions add FOREIGN KEY ( idCommand ) REFERENCES Command (idCommand) on DELETE CASCADE;
  ALTER TABLE ParticularFunction add FOREIGN KEY ( idDevice ) REFERENCES Device (idDevice) on DELETE CASCADE;
  ALTER TABLE ParticularFunction add FOREIGN KEY ( idFunction ) REFERENCES Functions(idFunction) on DELETE CASCADE;
  ALTER TABLE LISTTIME ADD FOREIGN KEY (idDevice) REFERENCES DEVICE (idDevice) ON DELETE CASCADE;
