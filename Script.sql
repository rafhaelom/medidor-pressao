----- Criacao da tabela medida -----
CREATE TABLE IF NOT EXISTS medida (
	data_hora text, 
	peso real, 
	sistolica interger, 
	diastolica interger, 
	pulsacao interger
);

----- Consulta da tabela medida -----
select * from medida;