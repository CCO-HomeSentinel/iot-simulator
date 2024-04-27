DROP SCHEMA IF EXISTS `home_sentinel` ;

CREATE SCHEMA IF NOT EXISTS `home_sentinel` DEFAULT CHARACTER SET utf8 ;
USE `home_sentinel` ;

DROP TABLE IF EXISTS `home_sentinel`.`cliente` ;
CREATE TABLE IF NOT EXISTS `home_sentinel`.`cliente` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(64) NOT NULL,
  `sobrenome` VARCHAR(256) NOT NULL,
  `cpf` CHAR(11) NOT NULL,
  `rg` VARCHAR(24) NOT NULL,
  `email` VARCHAR(256) NOT NULL,
  `senha` VARCHAR(256) NOT NULL,
  `foto_url` VARCHAR(256) NOT NULL,
  `habilitado` TINYINT(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `cpf_UNIQUE` (`cpf` ASC) VISIBLE,
  UNIQUE INDEX `rg_UNIQUE` (`rg` ASC) VISIBLE,
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE)
ENGINE = InnoDB;

DROP TABLE IF EXISTS `home_sentinel`.`residencia` ;
CREATE TABLE IF NOT EXISTS `home_sentinel`.`residencia` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(64) NOT NULL,
  `habilitado` TINYINT(1) NULL,
  `cliente_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_residencia_cliente_idx` (`cliente_id` ASC) VISIBLE,
  CONSTRAINT `fk_residencia_cliente`
    FOREIGN KEY (`cliente_id`)
    REFERENCES `home_sentinel`.`cliente` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

DROP TABLE IF EXISTS `home_sentinel`.`endereco` ;
CREATE TABLE IF NOT EXISTS `home_sentinel`.`endereco` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `latitude` DECIMAL(9,6) NULL,
  `longitude` DECIMAL(9,6) NULL,
  `logradouro` VARCHAR(256) NULL,
  `numero` VARCHAR(16) NULL,
  `bairro` VARCHAR(64) NULL,
  `cidade` VARCHAR(64) NULL,
  `estado` VARCHAR(64) NULL,
  `cep` CHAR(8) NULL,
  `referencia` VARCHAR(64) NULL,
  `habilitado` TINYINT NULL,
  `residencia_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`, `residencia_id`),
  INDEX `fk_endereco_residencia1_idx` (`residencia_id` ASC) VISIBLE,
  CONSTRAINT `fk_endereco_residencia1`
    FOREIGN KEY (`residencia_id`)
    REFERENCES `home_sentinel`.`residencia` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

DROP TABLE IF EXISTS `home_sentinel`.`comodo_monitorado` ;
CREATE TABLE IF NOT EXISTS `home_sentinel`.`comodo_monitorado` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(64) NOT NULL,
  `area` INT NOT NULL,
  `altura` INT NULL,
  `andar` VARCHAR(16) NULL,
  `residencia_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`, `residencia_id`),
  INDEX `fk_comodo_monitorado_residencia1_idx` (`residencia_id` ASC) VISIBLE,
  CONSTRAINT `fk_comodo_monitorado_residencia1`
    FOREIGN KEY (`residencia_id`)
    REFERENCES `home_sentinel`.`residencia` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

DROP TABLE IF EXISTS `home_sentinel`.`modelo_sensor` ;
CREATE TABLE IF NOT EXISTS `home_sentinel`.`modelo_sensor` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(64) NULL,
  `tipo` VARCHAR(64) NULL,
  `fabricante` VARCHAR(45) NULL,
  `funcionalidade` VARCHAR(45) NULL,
  `tipo_medida` VARCHAR(16) NULL,
  `unidade_medida` VARCHAR(16) NULL,
  `min` VARCHAR(16) NULL,
  `max` VARCHAR(16) NULL,
  `regular_min` VARCHAR(16) NULL,
  `regular_max` VARCHAR(16) NULL,
  `is_anomalia` TINYINT(1) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

DROP TABLE IF EXISTS `home_sentinel`.`sensor` ;
CREATE TABLE IF NOT EXISTS `home_sentinel`.`sensor` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `modelo_sensor_id` INT UNSIGNED NOT NULL,
  `comodo_monitorado_id` INT UNSIGNED NOT NULL,
  `comodo_monitorado_residencia_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`, `modelo_sensor_id`),
  INDEX `fk_sensor_modelo_sensor1_idx` (`modelo_sensor_id` ASC) VISIBLE,
  INDEX `fk_sensor_comodo_monitorado1_idx` (`comodo_monitorado_id` ASC, `comodo_monitorado_residencia_id` ASC) VISIBLE,
  CONSTRAINT `fk_sensor_modelo_sensor1`
    FOREIGN KEY (`modelo_sensor_id`)
    REFERENCES `home_sentinel`.`modelo_sensor` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_sensor_comodo_monitorado1`
    FOREIGN KEY (`comodo_monitorado_id` , `comodo_monitorado_residencia_id`)
    REFERENCES `home_sentinel`.`comodo_monitorado` (`id` , `residencia_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

DROP TABLE IF EXISTS `home_sentinel`.`telefone` ;
CREATE TABLE IF NOT EXISTS `home_sentinel`.`telefone` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `cliente_id` INT UNSIGNED NOT NULL,
  `codigo_discagem` VARCHAR(4) NOT NULL,
  `codigo_area` VARCHAR(2) NOT NULL,
  `numero` VARCHAR(9) NOT NULL,
  `habilitado` TINYINT(1) NOT NULL,
  PRIMARY KEY (`id`, `cliente_id`),
  INDEX `fk_telefone_cliente1_idx` (`cliente_id` ASC) VISIBLE,
  UNIQUE INDEX `numero_UNIQUE` (`numero` ASC) VISIBLE,
  CONSTRAINT `fk_telefone_cliente1`
    FOREIGN KEY (`cliente_id`)
    REFERENCES `home_sentinel`.`cliente` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;