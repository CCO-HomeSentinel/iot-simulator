def retornar_sensores_por_cliente(id, sensores_disponiveis):
    sensores_formatados = [f"'{sensor}'" for sensor in sensores_disponiveis]
    sensores = ", ".join(sensores_formatados)

    query = f"""
        SELECT * FROM cliente c 
            JOIN residencia r 
	            ON r.cliente_id = c.id
            JOIN comodo_monitorado cm 
	            ON cm.residencia_id = r.id
            JOIN comodo_monitorado_sensor cms 
	            ON cms.comodo_monitorado_id = cm.id 
            JOIN sensor s 
                ON s.id = cms.sensor_id
            WHERE c.id = {id} AND s.nome_bruto IN ({sensores});"""
    
    return query
