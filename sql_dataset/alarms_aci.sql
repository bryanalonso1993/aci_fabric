-- create table alarms aci modify variable
CREATE table `aci_alarms_topology` (
    `unique` INT NOT NULL AUTO_INCREMENT,
    `cause` VARCHAR(50) DEFAULT NULL,
    `childAction` VARCHAR(15) DEFAULT NULL,
    `code` VARCHAR(255) DEFAULT NULL,
    `count` VARCHAR(50) DEFAULT NULL,
    `descr` VARCHAR(255) DEFAULT NULL,
    `dn` VARCHAR(50) DEFAULT NULL,
    `domain` VARCHAR(255) DEFAULT NULL,
    `nonAcked` VARCHAR(255) DEFAULT NULL,
    `nonDelegated` VARCHAR(50) DEFAULT NULL,
    `nonDelegatedAndNonAcked` VARCHAR(50) DEFAULT NULL,
    `rule` VARCHAR(255) DEFAULT NULL ,
    `severity` VARCHAR(30) DEFAULT NULL,
    `status` VARCHAR(30) DEFAULT NULL,
    `subject` VARCHAR(255) DEFAULT NULL,
    `type` VARCHAR(50) DEFAULT NULL,
    PRIMARY KEY(`unique`)
)ENGINE=InnoDB;