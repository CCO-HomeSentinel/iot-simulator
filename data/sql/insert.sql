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

INSERT INTO home_sentinel.sensor (nome, fabricante, funcionalidade)
VALUES
  ('Sensor de Movimento', 'ABC Electronics', 'Detecta movimentos no ambiente'),
  ('Sensor de Temperatura', 'XYZ Corp', 'Mede a temperatura do ambiente'),
  ('Sensor de Fumaça', '123 Sensors', 'Detecta a presença de fumaça no ambiente');

INSERT INTO home_sentinel.comodo_monitorado_sensor (comodo_monitorado_id, sensor_id)
VALUES
  (1, 1),
  (1, 2),
  (2, 1),
  (3, 2),
  (3, 3),
  (4, 2),
  (5, 3);