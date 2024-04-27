INSERT INTO home_sentinel.cliente (nome, sobrenome, cpf, rg, email, senha, foto_url, habilitado)
VALUES
  ('João', 'Silva', '12345678901', '1234567', 'joao.silva@email.com', sha2('123456', 256), 'https://upload.wikimedia.org/wikipedia/commons/4/43/Foto_Perfil.jpg', true);
  
INSERT INTO home_sentinel.telefone (cliente_id, codigo_discagem, codigo_area, numero, habilitado) 
VALUES
  (1, '+55', '11', '912345678', true);

INSERT INTO home_sentinel.residencia (nome, habilitado, cliente_id)
VALUES
  ('Casa Principal', true, 1);
  
INSERT INTO home_sentinel.endereco (latitude, longitude, logradouro, numero, bairro, cidade, estado, cep, referencia, habilitado, residencia_id)
VALUES
  (-23.558137, -46.661798, 'Rua Haddock Lobo', '4', 'Cerqueira César', 'São Paulo', 'SP', '01234567', 'Próximo ao Starbucks', true, 1);

-- Simulando casal sem filhos
INSERT INTO home_sentinel.comodo_monitorado (nome, area, altura, andar, residencia_id)
VALUES
  ('Sala de Estar', 30, 2.5, 1, 1),
  ('Sala de Jantar', 18, 2.5, 1, 1),
  ('Cozinha', 18, 2.5, 1, 1),
  ('Quarto suíte I', 30, 2.5, 1, 1),
  ('Quintal', 21, NULL, 1, 1);

INSERT INTO home_sentinel.modelo_sensor (nome, tipo, fabricante, funcionalidade, tipo_medida, unidade_medida, min, max, regular_min, regular_max, is_anomalia)
VALUES
  ('DFE02A/B', 'fumaca', 'Tecnohold', 'Detecta a presença de fumaça no ar', 'float', 'ppm', '0', '1000000', '0', '500', true),
  ('HISSGL', 'gas', 'Geonav', 'Detecta a presença de gases tóxicos', 'float', 'ppm', '0', '1000000', '0', '60', true),
  ('Water Level Alarm', 'inundacao', 'Homesen', 'Detecta se há água no ambiente', 'boolean', 'bool', 'false', 'true', 'false', 'false', true),
  ('TSL2561', 'luminosidade', 'Austria Microsystems', 'Mede a intensidade da luz', 'float', 'lux', '0', '100', '0', '90', false),
  ('HISSMV', 'movimento', 'Geonav', 'Detecta ações de movimento no espaço', 'boolean', 'bool', 'false', 'true', 'false', 'true', false), 
  ('KY-038', 'som', 'EletroGate', 'Registra os níveis de som no ambiente', 'float', 'db', '0', '400', '0', '200', true),
  ('EM THW 100', 'temperatura', 'Khomp', 'Mede a temperatura ambiente', 'float', '°C', '0', '100', '3', '44', true),
  ('EM THW 100', 'umidade', 'Khomp', 'Monitora os níveis de umidade no ar', 'float', '%', '0', '100', '20', '65', true);

INSERT INTO home_sentinel.sensor (modelo_sensor_id, comodo_monitorado_id, comodo_monitorado_residencia_id)
VALUES
  (1, 3, 1),
  (2, 3, 1),
  (3, 5, 1),
  (4, 1, 1),
  (5, 4, 1),
  (6, 1, 1),
  (7, 1, 1);