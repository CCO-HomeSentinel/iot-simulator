CREATE SCHEMA IF NOT EXISTS home_sentinel;

-- -----------------------------------------------------
-- Table home_sentinel.cliente
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS home_sentinel.cliente (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(64),
  sobrenome VARCHAR(256),
  cpf CHAR(11),
  rg VARCHAR(24),
  email VARCHAR(256),
  senha VARCHAR(256),
  habilitado BOOLEAN
);


-- -----------------------------------------------------
-- Table home_sentinel.residencia
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS home_sentinel.residencia (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(64),
  habilitado BOOLEAN,
  cliente_id INT NOT NULL,
  CONSTRAINT fk_residencia_cliente1
    FOREIGN KEY (cliente_id)
    REFERENCES home_sentinel.cliente (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);


-- -----------------------------------------------------
-- Table home_sentinel.endereco
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS home_sentinel.endereco (
  id SERIAL PRIMARY KEY,
  logradouro VARCHAR(256),
  numero VARCHAR(16),
  bairro VARCHAR(64),
  cidade VARCHAR(64),
  estado VARCHAR(64),
  cep CHAR(8),
  referencia VARCHAR(64),
  habilitado BOOLEAN,
  residencia_id INT NOT NULL,
  CONSTRAINT fk_endereco_residencia1
    FOREIGN KEY (residencia_id)
    REFERENCES home_sentinel.residencia (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);


-- -----------------------------------------------------
-- Table home_sentinel.comodo_monitorado
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS home_sentinel.comodo_monitorado (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(64),
  area INT,
  altura INT,
  residencia_id INT NOT NULL,
  CONSTRAINT fk_comodo_monitorado_residencia1
    FOREIGN KEY (residencia_id)
    REFERENCES home_sentinel.residencia (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);


-- -----------------------------------------------------
-- Table home_sentinel.telefone
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS home_sentinel.telefone (
  id SERIAL PRIMARY KEY,
  codigo_discagem INT,
  codigo_area INT,
  numero VARCHAR(9),
  habilitado VARCHAR(45),
  cliente_id INT NOT NULL,
  CONSTRAINT fk_telefone_cliente
    FOREIGN KEY (cliente_id)
    REFERENCES home_sentinel.cliente (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);


-- -----------------------------------------------------
-- Table home_sentinel.sensor
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS home_sentinel.sensor (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(64),
  fabricante VARCHAR(64),
  funcionalidade VARCHAR(64)
);


-- -----------------------------------------------------
-- Table home_sentinel.comodo_monitorado_sensor
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS home_sentinel.comodo_monitorado_sensor (
  id SERIAL PRIMARY KEY,
  comodo_monitorado_id INT NOT NULL,
  sensor_id INT NOT NULL,
  CONSTRAINT fk_comodo_monitorado_has_sensor_comodo_monitorado1
    FOREIGN KEY (comodo_monitorado_id)
    REFERENCES home_sentinel.comodo_monitorado (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_comodo_monitorado_has_sensor_sensor1
    FOREIGN KEY (sensor_id)
    REFERENCES home_sentinel.sensor (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);