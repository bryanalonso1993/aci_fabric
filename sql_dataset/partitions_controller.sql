-- table partitions controller APIC

CREATE TABLE `aci_partitions_controller` (
    `unique` INT NOT NULL AUTO_INCREMENT,
    `available` VARCHAR(50) DEFAULT NULL,
    `blocks` VARCHAR(50) DEFAULT NULL,
    `capUtilized` VARCHAR(20) DEFAULT NULL,
    `childAction` VARCHAR(50) DEFAULT NULL,
    `device` VARCHAR(50) DEFAULT NULL,
    `dn` VARCHAR(255) DEFAULT NULL,
    `failReason` VARCHAR(50) DEFAULT NULL,
    `fileSystem` VARCHAR(50) DEFAULT NULL,
    `firmwareVersion` VARCHAR(50) DEFAULT NULL,
    `lcOwn` VARCHAR(50) DEFAULT NULL,
    `mediaWearout` VARCHAR(10) DEFAULT NULL,
    `modTs` VARCHAR(255) DEFAULT NULL,
    `model` VARCHAR(50) DEFAULT NULL,
    `monPolDn` VARCHAR(255) DEFAULT NULL,
    `mount` VARCHAR(255) DEFAULT NULL,
    `name` VARCHAR(50) DEFAULT NULL,
    `nameAlias` VARCHAR(20) DEFAULT NULL,
    `operSt` VARCHAR(20) DEFAULT NULL,
    `serial` VARCHAR(20) DEFAULT NULL,
    `status` VARCHAR(20) DEFAULT NULL,
    `used` VARCHAR(30) DEFAULT NULL,
    PRIMARY KEY(`unique`)
)ENGINE='InnoDB'