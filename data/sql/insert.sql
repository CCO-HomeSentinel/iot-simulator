INSERT INTO home_sentinel.cliente (nome, sobrenome, cpf, rg, email, senha, habilitado)
VALUES
  ('João', 'Silva', '12345678901', '1234567', 'joao.silva@email.com', 'senha123', true),
  ('Maria', 'Santos', '98765432109', '7654321', 'maria.santos@email.com', 'senha456', true);

INSERT INTO home_sentinel.residencia (nome, habilitado, cliente_id)
VALUES
  ('Casa Principal', true, 1),
  ('Apartamento', true, 2);

INSERT INTO home_sentinel.endereco (logradouro, numero, bairro, cidade, estado, cep, referencia, habilitado, residencia_id)
VALUES
  ('Rua Principal', '123', 'Centro', 'São Paulo', 'SP', '01234567', 'Próximo à praça', true, 1),
  ('Avenida Secundária', '456', 'Bela Vista', 'Rio de Janeiro', 'RJ', '98765432', 'Próximo à escola', true, 2);

INSERT INTO home_sentinel.comodo_monitorado (nome, area, altura, residencia_id)
VALUES
  ('Sala de Estar', 30, 3, 1),
  ('Quarto Principal', 20, 2.5, 1),
  ('Sala de Jantar', 25, 2.8, 1),
  ('Cozinha', 15, 2.7, 2),
  ('Quarto de Hóspedes', 18, 2.3, 2);

INSERT INTO home_sentinel.telefone (codigo_discagem, codigo_area, numero, habilitado, cliente_id)
VALUES
  (55, 11, '912345678', 'Celular', 1),
  (55, 21, '998765432', 'Celular', 2);

INSERT INTO home_sentinel.sensor (nome, fabricante, funcionalidade, tipo, unidade_medida, min, max, regular_min, regular_max, is_anomalia)
VALUES
  ('Sensor de Fumaça', 'TechFire', 'Detecta a presença de fumaça no ar', 'float', 'ppm', '0', '100', '0', '0.5', true),
  ('Sensor de Gás', 'SafeGas', 'Detecta a presença de gases tóxicos', 'float', 'ppm', '0', '100', '0', '0.5', true),
  ('Sensor de Inundação', 'AquaSafe', 'Detecta se há água no ambiente', 'boolean', 'bool', 'false', 'true', 'false', 'false', true),
  ('Sensor de Luminosidade', 'BrightTech', 'Mede a intensidade da luz', 'float', 'lux', '0', '100', '0', '80', false),
  ('Sensor de Som', 'AudioSense', 'Registra os níveis de som no ambiente', 'float', 'db', '0', '100', '0', '10', false),
  ('Sensor de Temperatura', 'ThermoTech', 'Mede a temperatura ambiente', 'float', '°C', '0', '100', '17', '30', false),
  ('Sensor de Umidade', 'Humidex', 'Monitora os níveis de umidade no ar', 'float', '%', '0', '100', '5', '20', false);
  
  
INSERT INTO home_sentinel.comodo_monitorado_sensor (comodo_monitorado_id, sensor_id)
VALUES
  (1, 1),
  (1, 2),
  (2, 1),
  (2, 7),
  (3, 1),
  (3, 4),
  (4, 3),
  (4, 5),
  (5, 1),
  (5, 6);