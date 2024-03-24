def retornar_sensores_por_cliente(id, sensores_disponiveis):
    query = f"""
        select * from cliente c 
            join residencia r 
	            on r.cliente_id = c.id
            join comodo_monitorado cm 
	            on cm.residencia_id = r.id
            join comodo_monitorado_sensor cms 
	            on cms.comodo_monitorado_id = cm.id 
            join sensor s on 
		        s.id = cms.sensor_id
            where c.id = 1 and s.nome_bruto in ('gas');
