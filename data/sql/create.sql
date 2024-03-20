CREATE SCHEMA IF NOT EXISTS home_sentinel;

-- -----------------------------------------------------
-- Table home_sentinel.cliente
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS cliente (
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
CREATE TABLE IF NOT EXISTS residencia (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(64),
  habilitado BOOLEAN,
  cliente_id INT NOT NULL,
  CONSTRAINT fk_residencia_cliente1
    FOREIGN KEY (cliente_id)
    REFERENCES cliente (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);


-- -----------------------------------------------------
-- Table home_sentinel.endereco
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS endereco (
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
    REFERENCES residencia (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);


-- -----------------------------------------------------
-- Table home_sentinel.comodo_monitorado
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS comodo_monitorado (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(64),
  area INT,
  altura INT,
  residencia_id INT NOT NULL,
  CONSTRAINT fk_comodo_monitorado_residencia1
    FOREIGN KEY (residencia_id)
    REFERENCES residencia (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);


-- -----------------------------------------------------
-- Table home_sentinel.telefone
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS telefone (
  id SERIAL PRIMARY KEY,
  codigo_discagem INT,
  codigo_area INT,
  numero VARCHAR(9),
  habilitado VARCHAR(45),
  cliente_id INT NOT NULL,
  CONSTRAINT fk_telefone_cliente
    FOREIGN KEY (cliente_id)
    REFERENCES cliente (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);


-- -----------------------------------------------------
-- Table home_sentinel.sensor
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS sensor (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(64),
  nome_bruto VARCHAR(64),
  fabricante VARCHAR(64),
  funcionalidade VARCHAR(64),
  tipo VARCHAR(64),
  unidade_medida VARCHAR(16),
  min VARCHAR(8),
  max VARCHAR(8),
  regular_min VARCHAR(8),
  regular_max VARCHAR(8),
  is_anomalia BOOLEAN,
  CONSTRAINT tipo_check CHECK (tipo IN ('float', 'boolean'))
);


-- -----------------------------------------------------
-- Table home_sentinel.comodo_monitorado_sensor
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS comodo_monitorado_sensor (
  id SERIAL PRIMARY KEY,
  comodo_monitorado_id INT NOT NULL,
  sensor_id INT NOT NULL,
  CONSTRAINT fk_comodo_monitorado_has_sensor_comodo_monitorado1
    FOREIGN KEY (comodo_monitorado_id)
    REFERENCES comodo_monitorado (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_comodo_monitorado_has_sensor_sensor1
    FOREIGN KEY (sensor_id)
    REFERENCES sensor (id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);