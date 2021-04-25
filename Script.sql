----- Criacao da tabela registro -----
CREATE TABLE public.registro (
	id int not null,
	data_reg date not null,
	hora_reg time not null,
	peso float8 not null,
	sistolica int4 not null,
	diastolica int4 not null,
	pulsacao int4 not null,
	PRIMARY KEY (id),
	foreign key (id) references usuarios(id)
);

----- Consulta da tabela registro -----
select * from registro;

--- Criacao da tabela usuarios -----
CREATE TABLE public.usuarios (
	id serial NOT NULL,
	nome varchar(30) NOT null unique,
	email varchar(35) NOT null unique,
	usuario varchar(20) NOT null unique,
	senha varchar(8) NOT NULL,
	altura float8,
	PRIMARY KEY (id)
);

--- Consulta da tabela usuarios ---
select * from usuarios;