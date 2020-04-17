-- sql tables

-- table data inventory aci - fabric - test se va modificar los campos ahora que se revise la estructura de lo que envia el apic
CREATE table `aci_inventory` (
    `unique` INT NOT NULL AUTO_INCREMENT,
    `adSt` VARCHAR(20) DEFAULT NULL,
    `address` VARCHAR(15) DEFAULT NULL,
    `annotation` VARCHAR(255) DEFAULT NULL,
    `apicType` VARCHAR(20) DEFAULT NULL,
    `childAction` VARCHAR(20) DEFAULT NULL,
    `delayedHeartbeat` VARCHAR(10) DEFAULT NULL,
    `dn` VARCHAR(255) DEFAULT NULL,
    `extMngdBy` VARCHAR(50) DEFAULT NULL,
    `fabricSt` VARCHAR(50) DEFAULT NULL,
    `id` INT NOT NULL DEFAULT 0,
    `lastStateModTs` VARCHAR(255) DEFAULT NULL,
    `lcOwn` VARCHAR(30) DEFAULT NULL,
    `modTs` VARCHAR(255) DEFAULT NULL,
    `model` VARCHAR(30) DEFAULT NULL,
    `monPolDn` VARCHAR(255) DEFAULT NULL,
    `name` VARCHAR(50) DEFAULT NULL,
    `nameAlias` VARCHAR(50) DEFAULT NULL,
    `nodeType` VARCHAR(50) DEFAULT NULL, 
    `role` VARCHAR(50) DEFAULT NULL, 
    `serial` VARCHAR(50) DEFAULT NULL, 
    `status` VARCHAR(50) DEFAULT NULL, 
    `uid` INT NOT NULL DEFAULT 0, 
    `vendor` VARCHAR(50) DEFAULT NULL, 
    `version` VARCHAR(50) DEFAULT NULL,
    PRIMARY KEY(`unique`)
)ENGINE=InnoDB;
