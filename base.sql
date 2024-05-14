CREATE DATABASE SMARTHOME CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;

USE SMARTHOME

CREATE TABLE User (
  idUser int PRIMARY KEY AUTO_INCREMENT,
  nameUser varchar(50),
  dateUser DATETIME DEFAULT CURRENT_TIMESTAMP(),
  phoneUser varchar(10) UNIQUE
 
);

CREATE TABLE Account (
  idAccount int PRIMARY KEY,
  idUser int,
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
  namePort varchar(50),
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

ALTER TABLE PortDevice add  FOREIGN KEY (idDevice) REFERENCES Device (idDevice) on DELETE CASCADE;
ALTER table Account add FOREIGN KEY (idUser) REFERENCES User (idUser) on DELETE CASCADE;
ALTER TABLE Functions add FOREIGN KEY ( idCommand ) REFERENCES Command (idCommand) on DELETE CASCADE;
ALTER TABLE ParticularFunction add FOREIGN KEY ( idDevice ) REFERENCES Device (idDevice) on DELETE CASCADE;
ALTER TABLE ParticularFunction add FOREIGN KEY ( idFunction ) REFERENCES Functions(idFunction) on DELETE CASCADE;

INSERT INTO portdevice (idPort,portNum,idDevice) VALUES 
(
	idPort,
	13,
	1
);
INSERT INTO portdevice (idPort,portNum,idDevice) VALUES 
(
	idPort,
	8,
	2
);
INSERT INTO portdevice (idPort,portNum,idDevice) VALUES 
(
	idPort,
	9,
	2
);
INSERT INTO portdevice (idPort,portNum,idDevice) VALUES 
(
	idPort,
	3,
	2
);
INSERT INTO portdevice (idPort,portNum,idDevice) VALUES 
(
	idPort,
	5,
	2
);


INSERT INTO device (idDevice,nameDevice,typeDevice,status,POSITION) VALUES
(
	idDevice ,
	'led13',
	'led',
	0,
	'kitten'
);
INSERT INTO device (idDevice,nameDevice,typeDevice,status,POSITION) VALUES
(
	idDevice ,
	'door',
	'motor device',
	0,
	'in door'
);

INSERT INTO device (idDevice,nameDevice,typeDevice,status,POSITION) VALUES
(
	idDevice ,
	'fan',
	'motor device',
	0,
	'kitten'
);

