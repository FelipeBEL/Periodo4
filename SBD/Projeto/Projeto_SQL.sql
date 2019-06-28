DROP SCHEMA pizzaria_entretenimento CASCADE;
CREATE SCHEMA pizzaria_entretenimento;
SET search_path TO pizzaria_entretenimento;
SET datestyle TO 'DMY';

CREATE TABLE USUARIO(
	cpf BIGINT NOT NULL,
	nome_usuario VARCHAR(50) NOT NULL,
	endereco VARCHAR(50) NOT NULL,
	data_nasc DATE,
	
	CONSTRAINT PK_USUARIO PRIMARY KEY (cpf)
);

CREATE TABLE ANIMADOR(
	cpf BIGINT NOT NULL,
	nome_art VARCHAR(50) NOT NULL,
	preco REAL NOT NULL,
	bio VARCHAR(150),
	
	CONSTRAINT PK_ANIMADOR PRIMARY KEY (cpf),
	CONSTRAINT FK_ANIMADOR FOREIGN KEY (cpf) REFERENCES USUARIO(cpf)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

CREATE TABLE CONSUMIDOR_FAMINTO(
	cpf BIGINT NOT NULL,
	end_entrega VARCHAR(50) NOT NULL,
	
	CONSTRAINT PK_CONSUMIDOR PRIMARY KEY (cpf),
	CONSTRAINT FK_CONSUMIDOR FOREIGN KEY (cpf) REFERENCES USUARIO(cpf)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

CREATE TABLE DONO_DE_NEGOCIO(
	cpf BIGINT NOT NULL,
	linkedin VARCHAR(50),
	
	CONSTRAINT PK_DONO PRIMARY KEY (cpf),
	CONSTRAINT FK_DONO FOREIGN KEY (cpf) REFERENCES USUARIO(cpf)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

CREATE TABLE PEDIDO(
	id_pedido INTEGER NOT NULL,
	cpf_consumidor BIGINT NOT NULL,
	horario_entrega TIME,
	horario_realizado TIME,
	qnt_pessoas INTEGER,
	data_realizado DATE,
	tipo VARCHAR(50) NOT NULL,
        total REAL,
	
	CONSTRAINT PK_PEDIDO PRIMARY KEY (id_pedido),
	CONSTRAINT FK_PEDIDO FOREIGN KEY (cpf_consumidor) REFERENCES CONSUMIDOR_FAMINTO(cpf)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

CREATE TABLE PEDIDO_ENTRETENIMENTO(
	id_pedido INTEGER NOT NULL,
	cpf_animador BIGINT NOT NULL,
	duracao TIME NOT NULL,
	gorjeta REAL,
	tipo VARCHAR(50) NOT NULL,
	
	CONSTRAINT PK_PEDIDO_ENT PRIMARY KEY (id_pedido),
	CONSTRAINT FK_PEDIDO_ENT FOREIGN KEY (id_pedido) REFERENCES PEDIDO(id_pedido)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

CREATE TABLE PIZZARIA(
	nome_pizzaria VARCHAR(50) NOT NULL,
	cpf_dono BIGINT NOT NULL,
	horario_fechamento TIME NOT NULL,
	horario_abertura TIME NOT NULL,
	telefone VARCHAR(50) NOT NULL,
	site VARCHAR(50),
	endereco VARCHAR(50) NOT NULL,
	cep VARCHAR(50),
	
	CONSTRAINT PK_PIZZARIA PRIMARY KEY (nome_pizzaria),
	CONSTRAINT FK_PIZZARIA FOREIGN KEY (cpf_dono) REFERENCES DONO_DE_NEGOCIO(cpf)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

CREATE TABLE CATEGORIA(
	codigo INTEGER NOT NULL,
	descricao VARCHAR(150),
	subcategoria VARCHAR(50) NOT NULL,
	
	CONSTRAINT PK_CATEGORIA PRIMARY KEY (codigo)
);

CREATE TABLE PIZZA(
	nome_pizza VARCHAR(150) NOT NULL,
	nome_pizzaria VARCHAR(50) NOT NULL,
	preco REAL NOT NULL,
	codigo INTEGER NOT NULL,
	
	CONSTRAINT PK_PIZZA PRIMARY KEY (nome_pizza,nome_pizzaria),
	CONSTRAINT FK_PIZZA FOREIGN KEY (nome_pizzaria) REFERENCES PIZZARIA(nome_pizzaria)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
		FOREIGN KEY (codigo) REFERENCES CATEGORIA(codigo)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

CREATE TABLE ACOMPANHAMENTOS(
	codigo_acomp INTEGER NOT NULL,
	nome_pizzaria VARCHAR(50) NOT NULL,
	nome_acompanhamento VARCHAR(50) NOT NULL,
	preco REAL NOT NULL,
	tipo VARCHAR(50),
	descricao VARCHAR(150),
	
	CONSTRAINT PK_ACOMPANHAMENTOS PRIMARY KEY (codigo_acomp,nome_pizzaria),
	CONSTRAINT FK_ACOMPANHAMENTOS FOREIGN KEY (nome_pizzaria) REFERENCES PIZZARIA(nome_pizzaria)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

CREATE TABLE INGREDIENTE_EXTRA(
	cod_id INTEGER NOT NULL,
	nome_ingrediente VARCHAR(50) NOT NULL,
	preco REAL NOT NULL,

	CONSTRAINT PK_INGREDIENTE PRIMARY KEY (cod_id)

);

CREATE TABLE TRABALHA(
	nome_pizzaria VARCHAR(50) NOT NULL,
	cpf_animador BIGINT NOT NULL,
	disponibilidade VARCHAR(50) NOT NULL,

	CONSTRAINT PK_TRABALHA PRIMARY KEY (nome_pizzaria,cpf_animador),
	CONSTRAINT FK_TRABALHA FOREIGN KEY (nome_pizzaria) REFERENCES PIZZARIA
		ON UPDATE CASCADE
		ON DELETE CASCADE,
		FOREIGN KEY (cpf_animador) REFERENCES ANIMADOR(cpf)
		ON UPDATE CASCADE
		ON DELETE CASCADE

);

CREATE TABLE POSSUI_PEDIDO_ACOMP(
	id_pedido INTEGER NOT NULL,
	codigo_acomp INTEGER NOT NULL,
	nome_pizzaria VARCHAR(50) NOT NULL,
	quantidade INTEGER NOT NULL,

	CONSTRAINT PK_POSSUI_PEDIDO_ACOMP PRIMARY KEY (nome_pizzaria,id_pedido,codigo_acomp),
	CONSTRAINT FK_POSSUI_PEDIDO_ACOMP FOREIGN KEY (codigo_acomp, nome_pizzaria) REFERENCES ACOMPANHAMENTOS(codigo_acomp, nome_pizzaria)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
		FOREIGN KEY (id_pedido) REFERENCES PEDIDO(id_pedido)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

CREATE TABLE POSSUI_PEDIDO_PIZZA(
	id_pedido INTEGER NOT NULL,
	nome_pizza VARCHAR(50) NOT NULL,
	nome_pizzaria VARCHAR(50) NOT NULL,
	massa VARCHAR(50) NOT NULL,
	qnt_molho VARCHAR(50) NOT NULL,
	borda VARCHAR(50) NOT NULL,
	
	CONSTRAINT PK_POSSUI_PEDIDO_PIZZA PRIMARY KEY (nome_pizzaria,id_pedido,nome_pizza),
	CONSTRAINT FK_POSSUI_PEDIDO_PIZZA FOREIGN KEY (nome_pizza, nome_pizzaria) REFERENCES PIZZA(nome_pizza, nome_pizzaria)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
		FOREIGN KEY (id_pedido) REFERENCES PEDIDO(id_pedido)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

CREATE TABLE PIZZA_PEDIDO(
	id_pedido INTEGER NOT NULL,
	nome_pizza VARCHAR(50) NOT NULL,
	nome_pizzaria VARCHAR(50) NOT NULL,
	
	CONSTRAINT PK_PIZZA_PEDIDO PRIMARY KEY (nome_pizzaria,id_pedido,nome_pizza),
	CONSTRAINT FK_PIZZA_PEDIDO FOREIGN KEY (nome_pizza, nome_pizzaria) REFERENCES PIZZA(nome_pizza, nome_pizzaria)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
		FOREIGN KEY (id_pedido) REFERENCES PEDIDO
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

CREATE TABLE CONTEM(
	cod_id INTEGER NOT NULL,
	id_pedido INTEGER NOT NULL,
	nome_pizza VARCHAR(50) NOT NULL,
	nome_pizzaria VARCHAR(50) NOT NULL,
	
	CONSTRAINT PK_CONTEM PRIMARY KEY (cod_id,nome_pizzaria,id_pedido,nome_pizza),
	CONSTRAINT FK_CONTEM FOREIGN KEY (nome_pizza, nome_pizzaria) REFERENCES PIZZA(nome_pizza, nome_pizzaria)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
		FOREIGN KEY (id_pedido) REFERENCES PEDIDO(id_pedido)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
		FOREIGN KEY (cod_id) REFERENCES INGREDIENTE_EXTRA(cod_id)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

-- Insercao de 30 usuarios (10 para cada disjuncao):

INSERT INTO USUARIO VALUES (94464441106, 'Ricardo Carlos Eduardo Felipe Rodrigues', 'Quadra 102 Sul Rua NS B, 692', '20/03/1979');
INSERT INTO USUARIO VALUES (73656183880, 'Fabiana Bruna Araújo', 'Rua Mário Pimentel Filho, 242', '09/09/1943');
INSERT INTO USUARIO VALUES (65012215605, 'Valentina Laís Rayssa da Rosa', 'Rua 13, 386', '09/04/1958');
INSERT INTO USUARIO VALUES (28347809275, 'Isabela Alice da Rocha', 'Rua Cecília Brasil, 629', '04/05/1976');
INSERT INTO USUARIO VALUES (54218768960, 'Luana Marcela da Paz', 'Quadra 804 Sul Alameda 6, 644', '11/06/1997');
INSERT INTO USUARIO VALUES (72713598931, 'Lucas Francisco da Conceição', 'Avenida Quinze de Novembro, 876', '15/09/1979');
INSERT INTO USUARIO VALUES (85473162649, 'Filipe Emanuel Mateus da Costa', 'Caminho 38, 681', '25/02/1990');
INSERT INTO USUARIO VALUES (93728648701, 'Mateus Diego Henrique da Cunha', 'Rua Valmar Meira, 492', '14/05/1993');
INSERT INTO USUARIO VALUES (40661291880, 'Lorenzo Hugo Bento Drumond', 'Rua Ana Nery, 202', '22/09/1962');
INSERT INTO USUARIO VALUES (73940085332, 'Vitor Lorenzo Samuel Rezende', 'Rua Alércio Dias, 279', '24/04/1969');
INSERT INTO USUARIO VALUES (41446985059, 'Camila Ayla Nascimento', 'Estrada da Floresta, 400', '14/01/1969');
INSERT INTO USUARIO VALUES (86401631112, 'João André Bernardes', 'Rua Inácio Fernandes Nóbrega, 307', '10/03/1969');
INSERT INTO USUARIO VALUES (69106375189, 'André Antonio Geraldo Fogaça', 'Rua 1, 309', '20/04/1995');
INSERT INTO USUARIO VALUES (34323830378, 'Luan Gustavo Aragão', 'Rua Jairo Andrade Macedo, 992', '23/11/1941');
INSERT INTO USUARIO VALUES (73426313707, 'Giovana Renata da Luz', 'Beco José Henrique, 405', '14/09/1992');
INSERT INTO USUARIO VALUES (00490899943, 'Rosângela Tânia Bernardes', 'Rua Bartolomeu Bueno, 723', '19/10/1989');
INSERT INTO USUARIO VALUES (43018033191, 'Renato Leonardo Otávio das Neves', 'Rua das Gaivotas, 539', '15/07/1977');
INSERT INTO USUARIO VALUES (78323539618, 'Raul Lucas Pereira', 'Rua Raul Bopp, 455', '22/04/1939');
INSERT INTO USUARIO VALUES (97476788613, 'Mariana Rayssa Caldeira', 'Rua 17, 624', '08/09/1967');
INSERT INTO USUARIO VALUES (76995152263, 'Lavínia Malu Vieira', 'Rua Armando Fonseca, 284', '27/02/1992');
INSERT INTO USUARIO VALUES (92968140060, 'Maya Aparecida Santos', 'Rua Mondal, 876', '14/05/1986');
INSERT INTO USUARIO VALUES (31489751971, 'Oliver Anthony Tomás Silveira', 'Travessa Vale do Sol, 923', '02/01/1969');
INSERT INTO USUARIO VALUES (87030682858, 'Luciana Antonella Mariah Oliveira', 'Rua José Soares Abreu, 865', '17/11/1988');
INSERT INTO USUARIO VALUES (04126266917, 'Ayla Marlene Manuela Nunes', 'Rodovia BR-101, 224', '09/12/1962');
INSERT INTO USUARIO VALUES (03322425606, 'Carolina Luana da Mata', 'Quadra 143, 609', '27/04/1939');
INSERT INTO USUARIO VALUES (43825425533, 'Sebastião Mário Murilo Aragão', 'Rua Desembargador Hugo Simas, 149', '13/01/1959');
INSERT INTO USUARIO VALUES (46481595355, 'Benedito Joaquim da Rocha', 'Rua Minas Gerais, 542', '02/01/1950');
INSERT INTO USUARIO VALUES (27301137460, 'Enrico Matheus Ruan Almada', 'Quadra QN 5C, 683', '22/02/1975');
INSERT INTO USUARIO VALUES (90082806470, 'Beatriz Marina das Neves', 'Rua Vinte e Cinco de Dezembro, 743', '10/10/1973');
INSERT INTO USUARIO VALUES (79032320106, 'Isabelly Sophia da Luz', 'Rua Três, 367', '17/04/1965');

-- Dos 30 usuarios, 10 sao animadores:

INSERT INTO ANIMADOR VALUES (94464441106, 'Ricardinho Milos', 30.00, 'Amo fazer as pessoas se divertirem!');
INSERT INTO ANIMADOR VALUES (73656183880, 'Fabi HI-5', 25.00, 'Desde pequena gosto de fazer piadas e ver as pessoas alegres');
INSERT INTO ANIMADOR VALUES (65012215605, 'Val The Funny One', 60.00, 'Preço salgado, mas eu compenso ele te fazendo gargalhar');
INSERT INTO ANIMADOR VALUES (28347809275, 'Arrocha da Felicidade', 30.00);
INSERT INTO ANIMADOR VALUES (54218768960, 'Lulu Happy', 29.99, 'Preço quebrado que nem você depois de tanto rir');
INSERT INTO ANIMADOR VALUES (72713598931, 'Luquinhas', 40.50, 'Meus pais eram contra mas eu segui meu caminho como um bom animador');
INSERT INTO ANIMADOR VALUES (85473162649, 'Filipe Happiness', 24.20, 'Estagiando para me tornar um excelente profissional');
INSERT INTO ANIMADOR VALUES (93728648701, 'Dieguim Engra', 45.30);
INSERT INTO ANIMADOR VALUES (40661291880, 'Lmator', 50.00, 'Sim, meu nome é um trocadilho');
INSERT INTO ANIMADOR VALUES (73940085332, 'Samuquinha', 23.50, 'Chama o samu que você ri pra sempre');

-- Dos 30 usuarios, 10 sao dono de negocio:

INSERT INTO DONO_DE_NEGOCIO VALUES (41446985059, 'Camila Nascimento');
INSERT INTO DONO_DE_NEGOCIO VALUES (86401631112, 'João Bernardes');
INSERT INTO DONO_DE_NEGOCIO VALUES (69106375189, 'André Fogaça');
INSERT INTO DONO_DE_NEGOCIO VALUES (34323830378, 'Luan Gustavo');
INSERT INTO DONO_DE_NEGOCIO VALUES (73426313707, 'Giovana Renata');
INSERT INTO DONO_DE_NEGOCIO VALUES (00490899943, 'Rosângela Bernardes');
INSERT INTO DONO_DE_NEGOCIO VALUES (43018033191, 'Renato Otávio');
INSERT INTO DONO_DE_NEGOCIO VALUES (78323539618, 'Raul Pereira');
INSERT INTO DONO_DE_NEGOCIO VALUES (97476788613, 'Mariana Caldeira');
INSERT INTO DONO_DE_NEGOCIO VALUES (76995152263, 'Lavínia Vieira');

-- Dos 30 usuarios, 10 sao consumidores famintos:

INSERT INTO CONSUMIDOR_FAMINTO VALUES (92968140060, 'Rua Mondal, 876');
INSERT INTO CONSUMIDOR_FAMINTO VALUES (31489751971, 'Travessa Vale do Sol, 923');
INSERT INTO CONSUMIDOR_FAMINTO VALUES (87030682858, 'Rua José Soares Abreu, 865');
INSERT INTO CONSUMIDOR_FAMINTO VALUES (04126266917, 'Rodovia BR-101, 224');
INSERT INTO CONSUMIDOR_FAMINTO VALUES (03322425606, 'Quadra 143, 609');
INSERT INTO CONSUMIDOR_FAMINTO VALUES (43825425533, 'Rua Desembargador Hugo Simas, 149');
INSERT INTO CONSUMIDOR_FAMINTO VALUES (46481595355, 'Rua Minas Gerais, 542');
INSERT INTO CONSUMIDOR_FAMINTO VALUES (27301137460, 'Quadra QN 5C, 683');
INSERT INTO CONSUMIDOR_FAMINTO VALUES (90082806470, 'Rua Vinte e Cinco de Dezembro, 743');
INSERT INTO CONSUMIDOR_FAMINTO VALUES (79032320106, 'Rua Três, 367');

-- 10 pizarias:

INSERT INTO PIZZARIA VALUES ('Pizzaria Pizza Ria', 41446985059, '23:00:00', '18:30:00', '3136342245', 'www.pizzariapizzaria.com.br','Rua Yvon Magalhães Pinto, 596','30350560');
INSERT INTO PIZZARIA VALUES ('Cheiro Bom Pizzaria', 86401631112, '00:00:00', '19:00:00', '8235451618', 'www.cheirobompizzaria.com.br','Rua A-25, 414','57084025');
INSERT INTO PIZZARIA VALUES ('Pizzaria Anima Tudo', 69106375189, '22:30:00', '19:30:00', '1228187340', 'www.panimatudo.com.br','Avenida Elisio Galdino Sobrinho, 360','12236742');
INSERT INTO PIZZARIA VALUES ('Pizzaria Sabor dos Sonhos', 34323830378, '22:30:00', '18:00:00', '7935821598', 'www.sabordossonhos.com.br','Rua Altamira, 606','49069168');
INSERT INTO PIZZARIA VALUES ('Que Delicia Pizzaria', 73426313707, '00:00:00', '20:00:00', '6327426833', NULL ,'Rua K, 399','77818580');
INSERT INTO PIZZARIA VALUES ('Happy Pizza', 00490899943, '00:30:00', '20:00:00', '9526734398', 'www.happypizza.com.br' ,'Avenida Carlos Pereira de Melo, 161','69312212');
INSERT INTO PIZZARIA VALUES ('Pizzaria Felicidade', 43018033191, '23:30:00', '19:00:00', '1126363372', 'www.pizzariafelicidade.com.br' ,'Rua São Tomé, 585','09410670');
INSERT INTO PIZZARIA VALUES ('Pizzaria da Alegria', 78323539618, '22:00:00', '18:00:00', '9436310018', 'www.alegrepizza.com.br' ,'Quadra Onze, 661','68505290');
INSERT INTO PIZZARIA VALUES ('Clown Pizzas', 97476788613, '22:00:00', '19:30:00', '7136601609', 'www.clownpizzas.com.br' ,'Praça Geraldo Walter, 140','41950355');
INSERT INTO PIZZARIA VALUES ('Big Pizza Pizzaria', 76995152263, '22:00:00', '19:30:00', '7136601609', 'www.pbigpizza.com.br' ,'Rua 25 de Agosto, 312','69915230');

-- 10 categorias:

INSERT INTO CATEGORIA VALUES (1, 'Salgado', 'Tradicional');
INSERT INTO CATEGORIA VALUES (2, 'Salgado', 'Especial');
INSERT INTO CATEGORIA VALUES (3, 'Salgado', 'Premium');
INSERT INTO CATEGORIA VALUES (4, 'Salgado', 'VIP');
INSERT INTO CATEGORIA VALUES (5, 'Salgado', 'Gold');
INSERT INTO CATEGORIA VALUES (6, 'Doce', 'Tradicional');
INSERT INTO CATEGORIA VALUES (7, 'Doce', 'Especial');
INSERT INTO CATEGORIA VALUES (8, 'Doce', 'Premium');
INSERT INTO CATEGORIA VALUES (9, 'Doce', 'VIP');
INSERT INTO CATEGORIA VALUES (10, 'Doce', 'Gold');

-- 10 pizzas para cada pizzaria:

INSERT INTO PIZZA VALUES ('Mussarela', 'Pizzaria Pizza Ria', 45.50, 1);
INSERT INTO PIZZA VALUES ('Mussarela', 'Cheiro Bom Pizzaria', 49.50, 2);
INSERT INTO PIZZA VALUES ('Mussarela', 'Pizzaria Anima Tudo', 50.00, 3);
INSERT INTO PIZZA VALUES ('Mussarela', 'Pizzaria Sabor dos Sonhos', 45.99, 2);
INSERT INTO PIZZA VALUES ('Mussarela', 'Que Delicia Pizzaria', 45.50, 2);
INSERT INTO PIZZA VALUES ('Mussarela', 'Happy Pizza', 45.00, 1);
INSERT INTO PIZZA VALUES ('Mussarela', 'Pizzaria Felicidade', 44.90, 1);
INSERT INTO PIZZA VALUES ('Mussarela', 'Pizzaria da Alegria', 43.00, 2);
INSERT INTO PIZZA VALUES ('Mussarela', 'Clown Pizzas', 46.00, 3);
INSERT INTO PIZZA VALUES ('Mussarela', 'Big Pizza Pizzaria', 45.99, 1);

INSERT INTO PIZZA VALUES ('Portuguesa', 'Pizzaria Pizza Ria', 47.50, 4);
INSERT INTO PIZZA VALUES ('Portuguesa', 'Cheiro Bom Pizzaria', 48.00, 2);
INSERT INTO PIZZA VALUES ('Portuguesa', 'Pizzaria Anima Tudo', 40.50, 3);
INSERT INTO PIZZA VALUES ('Portuguesa', 'Pizzaria Sabor dos Sonhos', 41.50, 1);
INSERT INTO PIZZA VALUES ('Portuguesa', 'Que Delicia Pizzaria', 35.00, 4);
INSERT INTO PIZZA VALUES ('Portuguesa', 'Happy Pizza', 59.99, 2);
INSERT INTO PIZZA VALUES ('Portuguesa', 'Pizzaria Felicidade', 40.50, 1);
INSERT INTO PIZZA VALUES ('Portuguesa', 'Pizzaria da Alegria', 48.00, 3);
INSERT INTO PIZZA VALUES ('Portuguesa', 'Clown Pizzas', 45.50, 2);
INSERT INTO PIZZA VALUES ('Portuguesa', 'Big Pizza Pizzaria', 51.50, 2);

INSERT INTO PIZZA VALUES ('Chocolate', 'Pizzaria Pizza Ria', 48.50, 6);
INSERT INTO PIZZA VALUES ('Chocolate', 'Cheiro Bom Pizzaria', 55.00, 7);
INSERT INTO PIZZA VALUES ('Chocolate', 'Pizzaria Anima Tudo', 44.50, 6);
INSERT INTO PIZZA VALUES ('Chocolate', 'Pizzaria Sabor dos Sonhos', 40.50, 7);
INSERT INTO PIZZA VALUES ('Chocolate', 'Que Delicia Pizzaria', 65.00, 7);
INSERT INTO PIZZA VALUES ('Chocolate', 'Happy Pizza', 52.99, 8);
INSERT INTO PIZZA VALUES ('Chocolate', 'Pizzaria Felicidade', 40.50, 8);
INSERT INTO PIZZA VALUES ('Chocolate', 'Pizzaria da Alegria', 48.50, 7);
INSERT INTO PIZZA VALUES ('Chocolate', 'Clown Pizzas', 46.50, 6);
INSERT INTO PIZZA VALUES ('Chocolate', 'Big Pizza Pizzaria', 49.99, 6);

INSERT INTO PIZZA VALUES ('Peperone', 'Pizzaria Pizza Ria', 60.00, 4);
INSERT INTO PIZZA VALUES ('Peperone', 'Cheiro Bom Pizzaria', 56.00, 5);
INSERT INTO PIZZA VALUES ('Peperone', 'Pizzaria Anima Tudo', 50.50, 3);
INSERT INTO PIZZA VALUES ('Peperone', 'Pizzaria Sabor dos Sonhos', 65.50, 3);
INSERT INTO PIZZA VALUES ('Peperone', 'Que Delicia Pizzaria', 48.00, 2);
INSERT INTO PIZZA VALUES ('Peperone', 'Happy Pizza', 52.99, 4);
INSERT INTO PIZZA VALUES ('Peperone', 'Pizzaria Felicidade', 47.50, 2);
INSERT INTO PIZZA VALUES ('Peperone', 'Pizzaria da Alegria', 50.50, 2);
INSERT INTO PIZZA VALUES ('Peperone', 'Clown Pizzas', 55.99, 3);
INSERT INTO PIZZA VALUES ('Peperone', 'Big Pizza Pizzaria', 59.99, 3);

INSERT INTO PIZZA VALUES ('Banana com canela', 'Pizzaria Pizza Ria', 55.99, 6);
INSERT INTO PIZZA VALUES ('Banana com canela', 'Cheiro Bom Pizzaria', 50.00, 8);
INSERT INTO PIZZA VALUES ('Banana com canela', 'Pizzaria Anima Tudo', 54.50, 7);
INSERT INTO PIZZA VALUES ('Banana com canela', 'Pizzaria Sabor dos Sonhos', 60.50, 7);
INSERT INTO PIZZA VALUES ('Banana com canela', 'Que Delicia Pizzaria', 49.00, 8);
INSERT INTO PIZZA VALUES ('Banana com canela', 'Happy Pizza', 57.99, 9);
INSERT INTO PIZZA VALUES ('Banana com canela', 'Pizzaria Felicidade', 44.50, 6);
INSERT INTO PIZZA VALUES ('Banana com canela', 'Pizzaria da Alegria', 58.00, 7);
INSERT INTO PIZZA VALUES ('Banana com canela', 'Clown Pizzas', 60.99, 7);
INSERT INTO PIZZA VALUES ('Banana com canela', 'Big Pizza Pizzaria', 39.99, 8);

INSERT INTO PIZZA VALUES ('Calabresa', 'Pizzaria Pizza Ria', 45.99, 3);
INSERT INTO PIZZA VALUES ('Calabresa', 'Cheiro Bom Pizzaria', 40.00, 2);
INSERT INTO PIZZA VALUES ('Calabresa', 'Pizzaria Anima Tudo', 35.50, 1);
INSERT INTO PIZZA VALUES ('Calabresa', 'Pizzaria Sabor dos Sonhos', 38.55, 1);
INSERT INTO PIZZA VALUES ('Calabresa', 'Que Delicia Pizzaria', 47.00, 3);
INSERT INTO PIZZA VALUES ('Calabresa', 'Happy Pizza', 45.99, 2);
INSERT INTO PIZZA VALUES ('Calabresa', 'Pizzaria Felicidade', 42.50, 2);
INSERT INTO PIZZA VALUES ('Calabresa', 'Pizzaria da Alegria', 50.00, 3);
INSERT INTO PIZZA VALUES ('Calabresa', 'Clown Pizzas', 52.99, 3);
INSERT INTO PIZZA VALUES ('Calabresa', 'Big Pizza Pizzaria', 37.99, 1);

INSERT INTO PIZZA VALUES ('Frango com Catupiry', 'Pizzaria Pizza Ria', 46.50, 4);
INSERT INTO PIZZA VALUES ('Frango com Catupiry', 'Cheiro Bom Pizzaria', 37.50, 1);
INSERT INTO PIZZA VALUES ('Frango com Catupiry', 'Pizzaria Anima Tudo', 44.50, 2);
INSERT INTO PIZZA VALUES ('Frango com Catupiry', 'Pizzaria Sabor dos Sonhos', 39.50, 3);
INSERT INTO PIZZA VALUES ('Frango com Catupiry', 'Que Delicia Pizzaria', 40.99, 1);
INSERT INTO PIZZA VALUES ('Frango com Catupiry', 'Happy Pizza', 39.99, 3);
INSERT INTO PIZZA VALUES ('Frango com Catupiry', 'Pizzaria Felicidade', 36.50, 1);
INSERT INTO PIZZA VALUES ('Frango com Catupiry', 'Pizzaria da Alegria', 55.00, 2);
INSERT INTO PIZZA VALUES ('Frango com Catupiry', 'Clown Pizzas', 54.00, 1);
INSERT INTO PIZZA VALUES ('Frango com Catupiry', 'Big Pizza Pizzaria', 50.00, 4);

INSERT INTO PIZZA VALUES ('Brigadeiro', 'Pizzaria Pizza Ria', 40.50, 7);
INSERT INTO PIZZA VALUES ('Brigadeiro', 'Cheiro Bom Pizzaria', 38.90, 6);
INSERT INTO PIZZA VALUES ('Brigadeiro', 'Pizzaria Anima Tudo', 41.50, 6);
INSERT INTO PIZZA VALUES ('Brigadeiro', 'Pizzaria Sabor dos Sonhos', 46.50, 8);
INSERT INTO PIZZA VALUES ('Brigadeiro', 'Que Delicia Pizzaria', 44.99, 7);
INSERT INTO PIZZA VALUES ('Brigadeiro', 'Happy Pizza', 35.99, 6);
INSERT INTO PIZZA VALUES ('Brigadeiro', 'Pizzaria Felicidade', 50.50, 8);
INSERT INTO PIZZA VALUES ('Brigadeiro', 'Pizzaria da Alegria', 57.60, 9);
INSERT INTO PIZZA VALUES ('Brigadeiro', 'Clown Pizzas', 54.99, 7);
INSERT INTO PIZZA VALUES ('Brigadeiro', 'Big Pizza Pizzaria', 55.00, 10);

INSERT INTO PIZZA VALUES ('Franbacon', 'Pizzaria Pizza Ria', 65.50, 5);
INSERT INTO PIZZA VALUES ('Franbacon', 'Cheiro Bom Pizzaria', 34.00, 1);
INSERT INTO PIZZA VALUES ('Franbacon', 'Pizzaria Anima Tudo', 44.00, 2);
INSERT INTO PIZZA VALUES ('Franbacon', 'Pizzaria Sabor dos Sonhos', 39.50, 2);
INSERT INTO PIZZA VALUES ('Franbacon', 'Que Delicia Pizzaria', 55.00, 3);
INSERT INTO PIZZA VALUES ('Franbacon', 'Happy Pizza', 35.90, 1);
INSERT INTO PIZZA VALUES ('Franbacon', 'Pizzaria Felicidade', 56.99, 2);
INSERT INTO PIZZA VALUES ('Franbacon', 'Pizzaria da Alegria', 49.40, 2);
INSERT INTO PIZZA VALUES ('Franbacon', 'Clown Pizzas', 59.30, 4);
INSERT INTO PIZZA VALUES ('Franbacon', 'Big Pizza Pizzaria', 60.20, 1);

INSERT INTO PIZZA VALUES ('Prestígio', 'Pizzaria Pizza Ria', 68.50, 10);
INSERT INTO PIZZA VALUES ('Prestígio', 'Cheiro Bom Pizzaria', 50.00, 7);
INSERT INTO PIZZA VALUES ('Prestígio', 'Pizzaria Anima Tudo', 49.90, 8);
INSERT INTO PIZZA VALUES ('Prestígio', 'Pizzaria Sabor dos Sonhos', 35.50, 6);
INSERT INTO PIZZA VALUES ('Prestígio', 'Que Delicia Pizzaria', 51.90, 7);
INSERT INTO PIZZA VALUES ('Prestígio', 'Happy Pizza', 40.90, 8);
INSERT INTO PIZZA VALUES ('Prestígio', 'Pizzaria Felicidade', 53.60, 8);
INSERT INTO PIZZA VALUES ('Prestígio', 'Pizzaria da Alegria', 37.30, 9);
INSERT INTO PIZZA VALUES ('Prestígio', 'Clown Pizzas', 46.99, 7);
INSERT INTO PIZZA VALUES ('Prestígio', 'Big Pizza Pizzaria', 32.80, 6);

-- 10 acompanhamentos pra cada pizzaria:

INSERT INTO ACOMPANHAMENTOS VALUES (1, 'Pizzaria Pizza Ria', 'Suco natural 1L', 15.50, 'Bebida', 'Laranja ou abacaxi');
INSERT INTO ACOMPANHAMENTOS VALUES (1, 'Cheiro Bom Pizzaria', 'Suco natural 1L', 18.90, 'Bebida', 'Laranja ou abacaxi');
INSERT INTO ACOMPANHAMENTOS VALUES (1, 'Pizzaria Anima Tudo', 'Suco natural 1L', 15.90, 'Bebida', 'Laranja ou abacaxi');
INSERT INTO ACOMPANHAMENTOS VALUES (1, 'Pizzaria Sabor dos Sonhos', 'Suco natural 1L', 20.00, 'Bebida', 'Laranja ou abacaxi');
INSERT INTO ACOMPANHAMENTOS VALUES (1, 'Que Delicia Pizzaria','Suco natural 1L', 16.99, 'Bebida', 'Laranja ou abacaxi');
INSERT INTO ACOMPANHAMENTOS VALUES (1, 'Happy Pizza', 'Suco natural 1L', 15.50, 'Bebida', 'Laranja ou abacaxi');
INSERT INTO ACOMPANHAMENTOS VALUES (1, 'Pizzaria Felicidade', 'Suco natural 1L', 19.90, 'Bebida', 'Laranja ou abacaxi');
INSERT INTO ACOMPANHAMENTOS VALUES (1, 'Pizzaria da Alegria', 'Suco natural 1L', 20.00, 'Bebida', 'Laranja ou abacaxi');
INSERT INTO ACOMPANHAMENTOS VALUES (1, 'Clown Pizzas', 'Suco natural 1L', 18.90, 'Bebida', 'Laranja ou abacaxi');
INSERT INTO ACOMPANHAMENTOS VALUES (1, 'Big Pizza Pizzaria', 'Suco natural 1L', 17.50, 'Bebida', 'Laranja ou abacaxi');

INSERT INTO ACOMPANHAMENTOS VALUES (2, 'Pizzaria Pizza Ria', 'Refrigerante 2L', 20.50, 'Bebida', 'Coca, Fanta ou Sprite');
INSERT INTO ACOMPANHAMENTOS VALUES (2, 'Cheiro Bom Pizzaria', 'Refrigerante 2L', 12.00, 'Bebida', 'Coca, Fanta ou Sprite');
INSERT INTO ACOMPANHAMENTOS VALUES (2, 'Pizzaria Anima Tudo', 'Refrigerante 2L', 14.50, 'Bebida', 'Coca, Fanta ou Sprite');
INSERT INTO ACOMPANHAMENTOS VALUES (2, 'Pizzaria Sabor dos Sonhos', 'Refrigerante 2L', 19.90, 'Bebida', 'Coca, Fanta ou Sprite');
INSERT INTO ACOMPANHAMENTOS VALUES (2, 'Que Delicia Pizzaria','Refrigerante 2L', 17.80, 'Bebida', 'Coca, Fanta ou Sprite');
INSERT INTO ACOMPANHAMENTOS VALUES (2, 'Happy Pizza', 'Refrigerante 2L', 15.50, 'Bebida', 'Coca, Fanta ou Sprite');
INSERT INTO ACOMPANHAMENTOS VALUES (2, 'Pizzaria Felicidade', 'Refrigerante 2L', 21.00, 'Bebida', 'Coca, Fanta ou Sprite');
INSERT INTO ACOMPANHAMENTOS VALUES (2, 'Pizzaria da Alegria', 'Refrigerante 2L', 13.90, 'Bebida', 'Coca, Fanta ou Sprite');
INSERT INTO ACOMPANHAMENTOS VALUES (2, 'Clown Pizzas', 'Refrigerante 2L', 22.60, 'Bebida', 'Coca, Fanta ou Sprite');
INSERT INTO ACOMPANHAMENTOS VALUES (2, 'Big Pizza Pizzaria', 'Refrigerante 2L', 11.00, 'Bebida', 'Coca, Fanta ou Sprite');

INSERT INTO ACOMPANHAMENTOS VALUES (3, 'Pizzaria Pizza Ria', 'Cerveja Lata', 10.50, 'Bebida');
INSERT INTO ACOMPANHAMENTOS VALUES (3, 'Cheiro Bom Pizzaria', 'Cerveja Lata', 7.00, 'Bebida');
INSERT INTO ACOMPANHAMENTOS VALUES (3, 'Pizzaria Anima Tudo', 'Cerveja Lata', 7.50, 'Bebida');
INSERT INTO ACOMPANHAMENTOS VALUES (3, 'Pizzaria Sabor dos Sonhos', 'Cerveja Lata', 8.90, 'Bebida');
INSERT INTO ACOMPANHAMENTOS VALUES (3, 'Que Delicia Pizzaria','Cerveja Lata', 3.99, 'Bebida');
INSERT INTO ACOMPANHAMENTOS VALUES (3, 'Happy Pizza', 'Cerveja Lata', 9.50, 'Bebida');
INSERT INTO ACOMPANHAMENTOS VALUES (3, 'Pizzaria Felicidade', 'Cerveja Lata', 12.00, 'Bebida');
INSERT INTO ACOMPANHAMENTOS VALUES (3, 'Pizzaria da Alegria', 'Cerveja Lata', 5.00, 'Bebida');
INSERT INTO ACOMPANHAMENTOS VALUES (3, 'Clown Pizzas', 'Cerveja Lata', 4.99, 'Bebida');
INSERT INTO ACOMPANHAMENTOS VALUES (3, 'Big Pizza Pizzaria', 'Cerveja Lata', 6.00, 'Bebida');

INSERT INTO ACOMPANHAMENTOS VALUES (4, 'Pizzaria Pizza Ria', 'Refrigerante Lata', 10.60, 'Bebida', 'Coca ou Guaraná');
INSERT INTO ACOMPANHAMENTOS VALUES (4, 'Cheiro Bom Pizzaria', 'Refrigerante Lata', 8.60, 'Bebida', 'Coca ou Guaraná');
INSERT INTO ACOMPANHAMENTOS VALUES (4, 'Pizzaria Anima Tudo', 'Refrigerante Lata', 6.90, 'Bebida', 'Coca ou Guaraná');
INSERT INTO ACOMPANHAMENTOS VALUES (4, 'Pizzaria Sabor dos Sonhos', 'Refrigerante Lata', 9.99, 'Bebida', 'Coca ou Guaraná');
INSERT INTO ACOMPANHAMENTOS VALUES (4, 'Que Delicia Pizzaria','Refrigerante Lata', 11.80, 'Bebida', 'Coca ou Guaraná');
INSERT INTO ACOMPANHAMENTOS VALUES (4, 'Happy Pizza', 'Refrigerante Lata', 12.55, 'Bebida', 'Coca ou Guaraná');
INSERT INTO ACOMPANHAMENTOS VALUES (4, 'Pizzaria Felicidade', 'Refrigerante Lata', 12.00, 'Bebida', 'Coca ou Guaraná');
INSERT INTO ACOMPANHAMENTOS VALUES (4, 'Pizzaria da Alegria', 'Refrigerante Lata', 5.50, 'Bebida', 'Coca ou Guaraná');
INSERT INTO ACOMPANHAMENTOS VALUES (4, 'Clown Pizzas', 'Refrigerante Lata', 7.90, 'Bebida', 'Coca ou Guaraná');
INSERT INTO ACOMPANHAMENTOS VALUES (4, 'Big Pizza Pizzaria', 'Refrigerante Lata', 6.60, 'Bebida', 'Coca ou Guaraná');

INSERT INTO ACOMPANHAMENTOS VALUES (5, 'Pizzaria Pizza Ria', 'Bombom', 2.60, 'Doce', 'Sonho de valsa ou ouro branco');
INSERT INTO ACOMPANHAMENTOS VALUES (5, 'Cheiro Bom Pizzaria', 'Bombom', 1.50, 'Doce', 'Sonho de valsa ou ouro branco');
INSERT INTO ACOMPANHAMENTOS VALUES (5, 'Pizzaria Anima Tudo', 'Bombom', 3.00, 'Doce', 'Sonho de valsa ou ouro branco');
INSERT INTO ACOMPANHAMENTOS VALUES (5, 'Pizzaria Sabor dos Sonhos', 'Bombom', 3.00, 'Doce', 'Sonho de valsa ou ouro branco');
INSERT INTO ACOMPANHAMENTOS VALUES (5, 'Que Delicia Pizzaria','Bombom', 2.50, 'Doce', 'Sonho de valsa ou ouro branco');
INSERT INTO ACOMPANHAMENTOS VALUES (5, 'Happy Pizza', 'Bombom', 1.40, 'Doce', 'Sonho de valsa ou ouro branco');
INSERT INTO ACOMPANHAMENTOS VALUES (5, 'Pizzaria Felicidade', 'Bombom', 1.50, 'Doce', 'Sonho de valsa ou ouro branco');
INSERT INTO ACOMPANHAMENTOS VALUES (5, 'Pizzaria da Alegria', 'Bombom', 2.50, 'Doce', 'Sonho de valsa ou ouro branco');
INSERT INTO ACOMPANHAMENTOS VALUES (5, 'Clown Pizzas', 'Bombom', 3.50, 'Doce', 'Sonho de valsa ou ouro branco');
INSERT INTO ACOMPANHAMENTOS VALUES (5, 'Big Pizza Pizzaria', 'Bombom', 1.99, 'Doce', 'Sonho de valsa ou ouro branco');

INSERT INTO ACOMPANHAMENTOS VALUES (6, 'Pizzaria Pizza Ria', 'Água de Côco Caixinha', 14.00, 'Bebida');
INSERT INTO ACOMPANHAMENTOS VALUES (6, 'Cheiro Bom Pizzaria', 'Água de Côco Caixinha', 12.20, 'Bebida');
INSERT INTO ACOMPANHAMENTOS VALUES (6, 'Pizzaria Anima Tudo', 'Água de Côco Caixinha', 11.50, 'Bebida');
INSERT INTO ACOMPANHAMENTOS VALUES (6, 'Pizzaria Sabor dos Sonhos', 'Água de Côco Caixinha', 10.00, 'Bebida');
INSERT INTO ACOMPANHAMENTOS VALUES (6, 'Que Delicia Pizzaria','Água de Côco Caixinha', 9.99, 'Bebida');
INSERT INTO ACOMPANHAMENTOS VALUES (6, 'Happy Pizza', 'Água de Côco Caixinha', 11.80, 'Bebida');
INSERT INTO ACOMPANHAMENTOS VALUES (6, 'Pizzaria Felicidade', 'Água de Côco Caixinha', 13.90, 'Bebida');
INSERT INTO ACOMPANHAMENTOS VALUES (6, 'Pizzaria da Alegria', 'Água de Côco Caixinha', 14.70, 'Bebida');
INSERT INTO ACOMPANHAMENTOS VALUES (6, 'Clown Pizzas', 'Água de Côco Caixinha', 16.30, 'Bebida');
INSERT INTO ACOMPANHAMENTOS VALUES (6, 'Big Pizza Pizzaria', 'Água de Côco Caixinha', 17.99, 'Bebida');

INSERT INTO ACOMPANHAMENTOS VALUES (7, 'Pizzaria Pizza Ria', 'Refrigerante 1,5L', 17.00, 'Bebida', 'Coca, Fanta ou Sprite');
INSERT INTO ACOMPANHAMENTOS VALUES (7, 'Cheiro Bom Pizzaria', 'Refrigerante 1,5L', 19.90, 'Bebida', 'Coca, Fanta ou Sprite');
INSERT INTO ACOMPANHAMENTOS VALUES (7, 'Pizzaria Anima Tudo', 'Refrigerante 1,5L', 16.99, 'Bebida', 'Coca, Fanta ou Sprite');
INSERT INTO ACOMPANHAMENTOS VALUES (7, 'Pizzaria Sabor dos Sonhos', 'Refrigerante 1,5L', 18.60, 'Bebida', 'Coca, Fanta ou Sprite');
INSERT INTO ACOMPANHAMENTOS VALUES (7, 'Que Delicia Pizzaria','Refrigerante 1,5L', 21.80, 'Bebida', 'Coca, Fanta ou Sprite');
INSERT INTO ACOMPANHAMENTOS VALUES (7, 'Happy Pizza', 'Refrigerante 1,5L', 14.90, 'Bebida', 'Coca, Fanta ou Sprite');
INSERT INTO ACOMPANHAMENTOS VALUES (7, 'Pizzaria Felicidade', 'Refrigerante 1,5L', 18.10, 'Bebida', 'Coca, Fanta ou Sprite');
INSERT INTO ACOMPANHAMENTOS VALUES (7, 'Pizzaria da Alegria', 'Refrigerante 1,5L', 19.90, 'Bebida', 'Coca, Fanta ou Sprite');
INSERT INTO ACOMPANHAMENTOS VALUES (7, 'Clown Pizzas', 'Refrigerante 1,5L', 16.80, 'Bebida', 'Coca, Fanta ou Sprite');
INSERT INTO ACOMPANHAMENTOS VALUES (7, 'Big Pizza Pizzaria', 'Refrigerante 1,5L', 20.00, 'Bebida', 'Coca, Fanta ou Sprite');

INSERT INTO ACOMPANHAMENTOS VALUES (8, 'Pizzaria Pizza Ria', 'Suco Caixinha', 10.50, 'Bebida', 'Laranja ou uva');
INSERT INTO ACOMPANHAMENTOS VALUES (8, 'Cheiro Bom Pizzaria', 'Suco Caixinha', 12.90, 'Bebida', 'Laranja ou uva');
INSERT INTO ACOMPANHAMENTOS VALUES (8, 'Pizzaria Anima Tudo', 'Suco Caixinha', 11.90, 'Bebida', 'Laranja ou uva');
INSERT INTO ACOMPANHAMENTOS VALUES (8, 'Pizzaria Sabor dos Sonhos', 'Suco Caixinha', 13.50, 'Bebida', 'Laranja ou uva');
INSERT INTO ACOMPANHAMENTOS VALUES (8, 'Que Delicia Pizzaria','Suco Caixinha', 8.00, 'Bebida', 'Laranja ou uva');
INSERT INTO ACOMPANHAMENTOS VALUES (8, 'Happy Pizza', 'Suco Caixinha', 14.00, 'Bebida', 'Laranja ou uva');
INSERT INTO ACOMPANHAMENTOS VALUES (8, 'Pizzaria Felicidade', 'Suco Caixinha', 13.60, 'Bebida', 'Laranja ou uva');
INSERT INTO ACOMPANHAMENTOS VALUES (8, 'Pizzaria da Alegria', 'Suco Caixinha', 11.90, 'Bebida', 'Laranja ou uva');
INSERT INTO ACOMPANHAMENTOS VALUES (8, 'Clown Pizzas', 'Suco Caixinha', 15.80, 'Bebida', 'Laranja ou uva');
INSERT INTO ACOMPANHAMENTOS VALUES (8, 'Big Pizza Pizzaria', 'Suco Caixinha', 15.00, 'Bebida', 'Laranja ou uva');

INSERT INTO ACOMPANHAMENTOS VALUES (9, 'Pizzaria Pizza Ria', 'Brigadeiro', 1.50, 'Doce');
INSERT INTO ACOMPANHAMENTOS VALUES (9, 'Cheiro Bom Pizzaria', 'Brigadeiro', 3.00, 'Doce');
INSERT INTO ACOMPANHAMENTOS VALUES (9, 'Pizzaria Anima Tudo', 'Brigadeiro', 2.10, 'Doce');
INSERT INTO ACOMPANHAMENTOS VALUES (9, 'Pizzaria Sabor dos Sonhos', 'Brigadeiro', 0.99, 'Doce');
INSERT INTO ACOMPANHAMENTOS VALUES (9, 'Que Delicia Pizzaria','Brigadeiro', 2.00, 'Doce');
INSERT INTO ACOMPANHAMENTOS VALUES (9, 'Happy Pizza', 'Brigadeiro', 3.50, 'Doce');
INSERT INTO ACOMPANHAMENTOS VALUES (9, 'Pizzaria Felicidade', 'Brigadeiro', 1.50, 'Doce');
INSERT INTO ACOMPANHAMENTOS VALUES (9, 'Pizzaria da Alegria', 'Brigadeiro', 2.50, 'Doce');
INSERT INTO ACOMPANHAMENTOS VALUES (9, 'Clown Pizzas', 'Brigadeiro', 2.00, 'Doce');
INSERT INTO ACOMPANHAMENTOS VALUES (9, 'Big Pizza Pizzaria', 'Brigadeiro', 1.00, 'Doce');

INSERT INTO ACOMPANHAMENTOS VALUES (10, 'Pizzaria Pizza Ria', 'Doce Leite Ninho', 1.50, 'Doce');
INSERT INTO ACOMPANHAMENTOS VALUES (10, 'Cheiro Bom Pizzaria', 'Doce Leite Ninho', 3.50, 'Doce');
INSERT INTO ACOMPANHAMENTOS VALUES (10, 'Pizzaria Anima Tudo', 'Doce Leite Ninho', 1.90, 'Doce');
INSERT INTO ACOMPANHAMENTOS VALUES (10, 'Pizzaria Sabor dos Sonhos', 'Doce Leite Ninho', 1.99, 'Doce');
INSERT INTO ACOMPANHAMENTOS VALUES (10, 'Que Delicia Pizzaria','Doce Leite Ninho', 3.00, 'Doce');
INSERT INTO ACOMPANHAMENTOS VALUES (10, 'Happy Pizza', 'Doce Leite Ninho', 4.20, 'Doce');
INSERT INTO ACOMPANHAMENTOS VALUES (10, 'Pizzaria Felicidade', 'Doce Leite Ninho', 2.00, 'Doce');
INSERT INTO ACOMPANHAMENTOS VALUES (10, 'Pizzaria da Alegria', 'Doce Leite Ninho', 1.90, 'Doce');
INSERT INTO ACOMPANHAMENTOS VALUES (10, 'Clown Pizzas', 'Doce Leite Ninho', 1.00, 'Doce');
INSERT INTO ACOMPANHAMENTOS VALUES (10, 'Big Pizza Pizzaria', 'Doce Leite Ninho', 2.00, 'Doce');

INSERT INTO PEDIDO VALUES (19, 92968140060, '16:20:45', '15:30:56', 3, '12/05/2017', 'Entretenimento', 0);
INSERT INTO PEDIDO VALUES (20, 31489751971, '17:30:00', '17:00:00', 4, '24/06/2019', 'Entretenimento', 0);
INSERT INTO PEDIDO VALUES (21, 87030682858, '20:00:00', '19:25:00', 2, '25/07/2019', 'Entretenimento', 0);
INSERT INTO PEDIDO VALUES (30, 04126266917, '19:30:00', '18:30:00', 5, '30/05/2019', 'Entretenimento', 0);
INSERT INTO PEDIDO VALUES (42, 03322425606, '18:40:00', '18:00:00', 2, '25/04/2018', 'Entretenimento', 0);
INSERT INTO PEDIDO VALUES (45, 43825425533, '19:00:20', '17:00:55', 5, '14/09/2017', 'Entretenimento', 0);
INSERT INTO PEDIDO VALUES (67, 46481595355, '22:40:10', '21:23:30', 2, '22/11/2017', 'Entretenimento', 0);
INSERT INTO PEDIDO VALUES (90, 27301137460, '03:50:24', '02:40:30', 1, '01/01/2018', 'Entretenimento', 0);
INSERT INTO PEDIDO VALUES (80, 90082806470, '23:30:00', '22:30:00', 2, '02/03/2017', 'Entretenimento', 0);
INSERT INTO PEDIDO VALUES (32, 79032320106, '09:30:26', '08:10:20', 5, '09/04/2018', 'Entretenimento', 0);

INSERT INTO INGREDIENTE_EXTRA VALUES (1, 'Bacon', 3.00);
INSERT INTO INGREDIENTE_EXTRA VALUES (2, 'Queijo', 2.50);
INSERT INTO INGREDIENTE_EXTRA VALUES (3, 'Pimentão', 2.50);
INSERT INTO INGREDIENTE_EXTRA VALUES (4, 'Frango', 3.00);
INSERT INTO INGREDIENTE_EXTRA VALUES (5, 'Milho', 3.00);
INSERT INTO INGREDIENTE_EXTRA VALUES (6, 'Calabresa', 2.80);
INSERT INTO INGREDIENTE_EXTRA VALUES (7, 'Cebola', 3.00);
INSERT INTO INGREDIENTE_EXTRA VALUES (8, 'Calabresa', 2.80);
INSERT INTO INGREDIENTE_EXTRA VALUES (9, 'Batata Palha', 2.80);
INSERT INTO INGREDIENTE_EXTRA VALUES (10, 'Ervilha', 2.00);

INSERT INTO TRABALHA VALUES('Happy Pizza', 94464441106, 'Segunda,Terça,Quarta,Quinta,Sexta,Sabado,Domingo');
INSERT INTO TRABALHA VALUES('Pizzaria Pizza Ria', 73656183880, 'Segunda,Quarta,Sexta');
INSERT INTO TRABALHA VALUES('Cheiro Bom Pizzaria', 65012215605, 'Segunda,Sexta');
INSERT INTO TRABALHA VALUES('Pizzaria da Alegria', 28347809275, 'Segunda,Quarta,Sexta,Sabado,Domingo');
INSERT INTO TRABALHA VALUES('Big Pizza Pizzaria', 54218768960, 'Segunda,Terça,Quinta,Sexta');
INSERT INTO TRABALHA VALUES('Clown Pizzas', 72713598931, 'Segunda,Quinta,Sexta');
INSERT INTO TRABALHA VALUES('Que Delicia Pizzaria', 85473162649, 'Terça,Quinta,Sexta,Sabado');
INSERT INTO TRABALHA VALUES('Pizzaria Felicidade', 93728648701, 'Quinta,Sexta,Sabado');
INSERT INTO TRABALHA VALUES('Pizzaria Anima Tudo', 40661291880, 'Quinta,Sexta,Sabado');
INSERT INTO TRABALHA VALUES('Pizzaria Sabor dos Sonhos', 73940085332, 'Quinta,Sexta,Sabado');

-- OBS: O procedimento armazenado e um dos triggers estão no meio das inserções devido à necessidade dos mesmos
-- serem executados antes dessas inserções para se tornarem válidos (INSERÇÕES DE POSSUI_PEDIDO_PIZZA,
-- POSSUI_PEDIDO_ACOMP, CONTEM E PEDIDO_ENTRETENIMENTO DEVEM VIR APÓS ESSES TRIGGERS):

-- Função que converte tipo TIME para INTEGER (segundos):

CREATE OR REPLACE FUNCTION to_seconds(tempo TIME)
  RETURNS REAL AS $$ 
DECLARE 
    hs INTEGER;
    ms INTEGER;
    s INTEGER;
	resultado REAL;
BEGIN
    SELECT (EXTRACT (HOUR FROM tempo) * 60*60) INTO hs; 
    SELECT (EXTRACT (MINUTES FROM tempo) * 60) INTO ms;
    SELECT (EXTRACT (SECONDS FROM tempo)) INTO s;
    SELECT (hs + ms + s)::real INTO resultado;
    RETURN resultado;
END $$ LANGUAGE 'plpgsql';

-- Função que dado o nome do animador calcula o total que o mesmo recebeu dentre todos os pedidos que participou:

CREATE OR REPLACE FUNCTION calcula_dinheiro_animador(
IN nome_animador ANIMADOR.nome_art%TYPE,
OUT valor_recebido ANIMADOR.preco%TYPE
) AS $$
DECLARE tempo_duracao TIME;
DECLARE gorjeta_animador REAL;
BEGIN

		SELECT SUM(pe.duracao), SUM(pe.gorjeta)
		INTO  tempo_duracao, gorjeta_animador
		FROM ANIMADOR ani, PEDIDO_ENTRETENIMENTO pe
		WHERE nome_art = nome_animador and ani.cpf = pe.cpf_animador
		GROUP BY pe.cpf_animador;
		
		SELECT preco
		INTO  valor_recebido
		FROM ANIMADOR
		WHERE nome_art = nome_animador;
		
		valor_recebido := (((to_seconds(tempo_duracao) * valor_recebido) / to_seconds('00:30:00')) + gorjeta_animador);
		
		
END $$ LANGUAGE 'plpgsql';


-- Testes para as funções:

SELECT to_seconds('01:40:50');
SELECT calcula_dinheiro_animador('Ricardinho Milos');

-- Conjunto de triggers para calcular preço total de cada pedido:

-- Trigger responsavel pelo preço total das pizzas:

CREATE OR REPLACE FUNCTION calcula_total_pizzas()
RETURNS TRIGGER AS $$
BEGIN
		
		UPDATE PEDIDO
		SET total = total + (	SELECT preco
								FROM POSSUI_PEDIDO_PIZZA pp, PIZZA pi
								WHERE pp.nome_pizza = new.nome_pizza and pp.nome_pizzaria = pi.nome_pizzaria 
									and pp.nome_pizzaria = new.nome_pizzaria
							 		and pp.id_pedido = new.id_pedido and pi.nome_pizza = pp.nome_pizza
							)
		WHERE id_pedido = new.id_pedido;
		
		RETURN NULL;
		
END $$ LANGUAGE 'plpgsql';

CREATE TRIGGER calcula_total_pizzas_t
AFTER INSERT ON POSSUI_PEDIDO_PIZZA
FOR EACH ROW
EXECUTE PROCEDURE calcula_total_pizzas();

-- Trigger responsavel pelo preço total dos acompanhamentos:

CREATE OR REPLACE FUNCTION calcula_total_acomp()
RETURNS TRIGGER AS $$
BEGIN
		
		UPDATE PEDIDO
		SET total = total + (	SELECT preco
								FROM POSSUI_PEDIDO_ACOMP pa, ACOMPANHAMENTOS ac
								WHERE pa.codigo_acomp = new.codigo_acomp and pa.codigo_acomp = ac.codigo_acomp 
							 		and pa.id_pedido = new.id_pedido and pa.nome_pizzaria = new.nome_pizzaria
									and pa.nome_pizzaria = ac.nome_pizzaria
							) * new.quantidade
		WHERE id_pedido = new.id_pedido;
		
		RETURN NULL;
		
END $$ LANGUAGE 'plpgsql';

CREATE TRIGGER calcula_total_acomp_t
AFTER INSERT ON POSSUI_PEDIDO_ACOMP
FOR EACH ROW
EXECUTE PROCEDURE calcula_total_acomp();

-- Trigger responsavel pelo preço total dos ingredientes extras:

CREATE OR REPLACE FUNCTION calcula_total_ingr_extra()
RETURNS TRIGGER AS $$
DECLARE add_preco REAL;
BEGIN

		SELECT preco
		INTO add_preco
		FROM CONTEM cn, INGREDIENTE_EXTRA ie, POSSUI_PEDIDO_PIZZA pe
		WHERE cn.cod_id = ie.cod_id and cn.cod_id = new.cod_id
		and pe.id_pedido = cn.id_pedido and pe.id_pedido = new.id_pedido;
		
		UPDATE PEDIDO
		SET total = total + add_preco
		WHERE id_pedido = new.id_pedido;
		
		RETURN NULL;
		
END $$ LANGUAGE 'plpgsql';

CREATE TRIGGER calcula_total_ingr_extra_t
AFTER INSERT ON CONTEM
FOR EACH ROW
EXECUTE PROCEDURE calcula_total_ingr_extra();

-- Trigger responsavel pelo preço total pago para o animador:

CREATE OR REPLACE FUNCTION calcula_total_animador_preco()
RETURNS TRIGGER AS $$
DECLARE nome VARCHAR(50);
BEGIN

		SELECT nome_art
		INTO nome
		FROM ANIMADOR ani, PEDIDO_ENTRETENIMENTO pe, PEDIDO ped
		WHERE pe.id_pedido = ped.id_pedido and pe.id_pedido = new.id_pedido
			and pe.cpf_animador = ani.cpf and pe.cpf_animador = new.cpf_animador;
		
		
		UPDATE PEDIDO
		SET total = total + calcula_dinheiro_animador(nome)
		WHERE id_pedido = new.id_pedido;
		
		
		RETURN NULL;
		
END $$ LANGUAGE 'plpgsql';

CREATE TRIGGER calcula_total_animador_preco_t
AFTER INSERT ON PEDIDO_ENTRETENIMENTO
FOR EACH ROW
EXECUTE PROCEDURE calcula_total_animador_preco();

-- Continua as inserções agora com os triggers ativos:

INSERT INTO PEDIDO_ENTRETENIMENTO VALUES (19, 94464441106, '02:00:00', 20.00, 'Entretenimento');
INSERT INTO PEDIDO_ENTRETENIMENTO VALUES (20, 73656183880, '01:40:50', 12.00, 'Entretenimento');
INSERT INTO PEDIDO_ENTRETENIMENTO VALUES (21, 28347809275, '00:40:00', 15.00, 'Entretenimento');
INSERT INTO PEDIDO_ENTRETENIMENTO VALUES (30, 65012215605, '03:10:00', 15.00, 'Entretenimento');
INSERT INTO PEDIDO_ENTRETENIMENTO VALUES (42, 73940085332, '02:30:00', 14.50, 'Entretenimento');
INSERT INTO PEDIDO_ENTRETENIMENTO VALUES (45, 40661291880, '00:30:00', 30.00, 'Entretenimento');
INSERT INTO PEDIDO_ENTRETENIMENTO VALUES (67, 93728648701, '01:25:30', 10.00, 'Entretenimento');
INSERT INTO PEDIDO_ENTRETENIMENTO VALUES (90, 85473162649, '01:00:30', 5.00, 'Entretenimento');
INSERT INTO PEDIDO_ENTRETENIMENTO VALUES (80, 72713598931, '01:00:00', 2.00, 'Entretenimento');
INSERT INTO PEDIDO_ENTRETENIMENTO VALUES (32, 54218768960, '03:00:25', 5.00, 'Entretenimento');

INSERT INTO POSSUI_PEDIDO_ACOMP VALUES(19, 7, 'Happy Pizza', 1);
INSERT INTO POSSUI_PEDIDO_ACOMP VALUES(20, 8, 'Cheiro Bom Pizzaria', 1);
INSERT INTO POSSUI_PEDIDO_ACOMP VALUES(21, 10, 'Pizzaria Pizza Ria', 2);
INSERT INTO POSSUI_PEDIDO_ACOMP VALUES(30, 3, 'Que Delicia Pizzaria', 1);
INSERT INTO POSSUI_PEDIDO_ACOMP VALUES(45, 2, 'Pizzaria Felicidade', 3);
INSERT INTO POSSUI_PEDIDO_ACOMP VALUES(67, 8, 'Clown Pizzas', 2);
INSERT INTO POSSUI_PEDIDO_ACOMP VALUES(90, 1, 'Pizzaria Anima Tudo', 1);
INSERT INTO POSSUI_PEDIDO_ACOMP VALUES(80, 2, 'Big Pizza Pizzaria', 2);
INSERT INTO POSSUI_PEDIDO_ACOMP VALUES(32, 3, 'Pizzaria Sabor dos Sonhos', 2);
INSERT INTO POSSUI_PEDIDO_ACOMP VALUES(42, 9, 'Clown Pizzas', 2);

INSERT INTO POSSUI_PEDIDO_PIZZA VALUES(19, 'Mussarela', 'Happy Pizza', 'Napolitana', 'Muito', 'Grossa');
INSERT INTO POSSUI_PEDIDO_PIZZA VALUES(20, 'Brigadeiro', 'Pizzaria Pizza Ria', 'Siciliana', 'Medio', 'Fina');
INSERT INTO POSSUI_PEDIDO_PIZZA VALUES(21, 'Calabresa', 'Cheiro Bom Pizzaria', 'Nova York', 'Pouco', 'Fina');
INSERT INTO POSSUI_PEDIDO_PIZZA VALUES(30, 'Peperone', 'Clown Pizzas', 'Napolitana', 'Medio', 'Grossa');
INSERT INTO POSSUI_PEDIDO_PIZZA VALUES(42, 'Franbacon', 'Que Delicia Pizzaria', 'Nova York', 'Pouco', 'Grossa');
INSERT INTO POSSUI_PEDIDO_PIZZA VALUES(45, 'Peperone', 'Pizzaria Anima Tudo', 'Siciliana', 'Muito', 'Fina');
INSERT INTO POSSUI_PEDIDO_PIZZA VALUES(67, 'Banana com canela', 'Big Pizza Pizzaria', 'Siciliana', 'Muito', 'Fina');
INSERT INTO POSSUI_PEDIDO_PIZZA VALUES(90, 'Prestígio', 'Pizzaria Sabor dos Sonhos', 'Napolitana', 'Medio', 'Grossa');
INSERT INTO POSSUI_PEDIDO_PIZZA VALUES(80, 'Frango com Catupiry', 'Clown Pizzas','Napolitana', 'Pouco', 'Grossa');
INSERT INTO POSSUI_PEDIDO_PIZZA VALUES(32, 'Mussarela', 'Cheiro Bom Pizzaria', 'Napolitana', 'Muito', 'Grossa');

INSERT INTO PIZZA_PEDIDO VALUES(19, 'Mussarela', 'Happy Pizza');
INSERT INTO PIZZA_PEDIDO VALUES(20, 'Brigadeiro', 'Pizzaria Pizza Ria');
INSERT INTO PIZZA_PEDIDO VALUES(21, 'Calabresa', 'Cheiro Bom Pizzaria');
INSERT INTO PIZZA_PEDIDO VALUES(30, 'Peperone', 'Clown Pizzas');
INSERT INTO PIZZA_PEDIDO VALUES(42, 'Franbacon', 'Que Delicia Pizzaria');
INSERT INTO PIZZA_PEDIDO VALUES(45, 'Peperone', 'Pizzaria Anima Tudo');
INSERT INTO PIZZA_PEDIDO VALUES(67, 'Banana com canela', 'Big Pizza Pizzaria');
INSERT INTO PIZZA_PEDIDO VALUES(90, 'Prestígio', 'Pizzaria Sabor dos Sonhos');
INSERT INTO PIZZA_PEDIDO VALUES(80, 'Frango com Catupiry', 'Clown Pizzas');
INSERT INTO PIZZA_PEDIDO VALUES(32, 'Mussarela', 'Cheiro Bom Pizzaria');

INSERT INTO CONTEM VALUES(3, 19, 'Mussarela', 'Cheiro Bom Pizzaria');
INSERT INTO CONTEM VALUES(10, 20, 'Brigadeiro', 'Pizzaria Pizza Ria');
INSERT INTO CONTEM VALUES(8, 21, 'Calabresa', 'Cheiro Bom Pizzaria');
INSERT INTO CONTEM VALUES(1, 30, 'Peperone', 'Clown Pizzas');
INSERT INTO CONTEM VALUES(5, 42, 'Franbacon', 'Que Delicia Pizzaria');
INSERT INTO CONTEM VALUES(2, 45, 'Peperone', 'Pizzaria Anima Tudo');
INSERT INTO CONTEM VALUES(3, 67, 'Banana com canela', 'Big Pizza Pizzaria');
INSERT INTO CONTEM VALUES(7, 90, 'Prestígio', 'Pizzaria Sabor dos Sonhos');
INSERT INTO CONTEM VALUES(6, 80, 'Frango com Catupiry', 'Clown Pizzas');
INSERT INTO CONTEM VALUES(7, 32, 'Mussarela', 'Cheiro Bom Pizzaria');

-- INÍCIO DAS CONSULTAS!

-- Calcula a media dos preços das pizzas de cada pizzaria e mostra qual a menor:

SELECT pi.nome_pizzaria, AVG(pi.preco)
FROM PIZZA pi, PIZZARIA pi2
WHERE pi.nome_pizzaria = pi2.nome_pizzaria
GROUP BY pi.nome_pizzaria
HAVING AVG(pi.preco) <= ALL(SELECT AVG(pi.preco)
						FROM PIZZA pi, PIZZARIA pi2
						WHERE pi.nome_pizzaria = pi2.nome_pizzaria
						GROUP BY pi.nome_pizzaria
						);
						
-- Mostra nome e quantidade de pedidos da(s) pizzaria(s) que possuem maior número de pedidos:

SELECT nome_pizzaria, COUNT(id_pedido)
FROM PIZZA_PEDIDO
GROUP BY nome_pizzaria
HAVING COUNT(id_pedido) >= ALL(SELECT COUNT(id_pedido)
							FROM PIZZA_PEDIDO
							GROUP BY nome_pizzaria);

-- Mostra o nome de cada acompanhamento existente junto com sua quantidade total individual 
-- e a quantidade total de acompanhamentos (ambos dentre todos os pedidos):

SELECT ac.nome_acompanhamento, SUM(pac.quantidade)
FROM ACOMPANHAMENTOS ac INNER JOIN POSSUI_PEDIDO_ACOMP pac ON 
	pac.codigo_acomp = ac.codigo_acomp and pac.nome_pizzaria = ac.nome_pizzaria
GROUP BY ROLLUP(ac.nome_acompanhamento);

-- Mostra o id do pedido que demorou menos tempo para ser entregue juntamente com esse tempo:

SELECT id_pedido, horario_entrega - horario_realizado
FROM PEDIDO
WHERE horario_entrega - horario_realizado <= ALL(SELECT horario_entrega - horario_realizado
												FROM PEDIDO
												);


-- Mostra a(s) pizza(s) mais vendida(s) de cada pizzaria, seu preço e o nome dessas pizzarias:

SELECT F2.nome_pizzaria, MAX(F2.nome_pizza),F2.preco
FROM (
	SELECT COUNT(PIZZA.nome_pizza), PIZZA.nome_pizzaria, PIZZA.nome_pizza,PIZZA.preco
	FROM  PIZZA_PEDIDO, POSSUI_PEDIDO_PIZZA, PEDIDO, PIZZA
	WHERE POSSUI_PEDIDO_PIZZA.id_pedido = PIZZA_PEDIDO.id_pedido AND
		  PEDIDO.id_pedido = PIZZA_PEDIDO.id_pedido AND
	  	  PIZZA.nome_pizza = POSSUI_PEDIDO_PIZZA.nome_pizza and
		  Pizza.nome_pizzaria = pizza_pedido.nome_pizzaria
	GROUP BY PIZZA.nome_pizza,PIZZA.preco, PIZZA.nome_pizzaria
) AS F2
group by F2.nome_pizzaria, F2.preco;

-- Mostra o animador que mais recebeu dentre todos (utilizando função criada):

SELECT nome_art, calcula_dinheiro_animador(nome_art)
FROM ANIMADOR
WHERE calcula_dinheiro_animador(nome_art) >= ALL(SELECT calcula_dinheiro_animador(nome_art)
													FROM ANIMADOR
													);
													
-- Mostra os id's de todos os pedidos junto com a quantidade de pessoas de cada e por fim
-- a quantia de dinheiro que ficaria para cada pessoa caso forem dividir o preço total das pizzas
													
SELECT ped1.id_pedido, ped2.qnt_pessoas, SUM(preco) / qnt_pessoas
FROM POSSUI_PEDIDO_PIZZA ped1, PEDIDO ped2, PIZZA pi
WHERE ped1.id_pedido = ped2.id_pedido and ped1.nome_pizza = pi.nome_pizza and 
	ped1.nome_pizzaria = pi.nome_pizzaria
GROUP BY ped1.id_pedido, qnt_pessoas;

-- Seleciona o animador mais contratado de cada pizzaria:

SELECT MAX(F1.COUNT), F1.nome_pizzaria, F1.nome_art
FROM POSSUI_PEDIDO_PIZZA p3, Animador a2, (
	SELECT COUNT(nome_art), p1.nome_pizzaria, nome_art, p1.id_pedido, cpf
	FROM POSSUI_PEDIDO_PIZZA p1, PEDIDO_ENTRETENIMENTO p2, ANIMADOR a1
	WHERE p1.id_pedido = p2.id_pedido AND
      	  a1.cpf = p2.cpf_animador
	GROUP BY p1.nome_pizzaria, nome_art, p1.id_pedido, cpf
) AS F1
WHERE p3.id_pedido = F1.id_pedido AND
      a2.cpf = F1.cpf
GROUP BY F1.nome_pizzaria, F1.nome_art;	

-- Mostra qual(is) ingrediente(s) esta presente em cada pedido:

SELECT nome_ingrediente, cn.id_pedido
FROM INGREDIENTE_EXTRA ie, CONTEM cn
WHERE cn.cod_id = ie.cod_id
GROUP BY nome_ingrediente, cn.id_pedido;

-- Mostra todos os animadores que trabalham nos fins de semana:

SELECT nome_art
FROM ANIMADOR ani, TRABALHA tr
WHERE (tr.disponibilidade LIKE '%Sabado%' and tr.disponibilidade LIKE '%Domingo%')
	and tr.cpf_animador = ani.cpf;


-- FIM DAS CONSULTAS!

-- Tabela que o segundo trigger irá utilizar:

CREATE TABLE HISTORICO_PRECOS(
	nome_pizza VARCHAR(50) NOT NULL,
	nome_pizzaria VARCHAR(50) NOT NULL,
	preco_antigo REAL NOT NULL,
	preco_novo REAL NOT NULL,
	situacao VARCHAR(50),
	porcentagem FLOAT4,
	usuario CHAR(20),
	data_feita TIMESTAMP
);

-- Trigger que grava historico de cada alteração do preco de alguma pizza armazenando o
-- seu valor antigo, o novo, se o mesmo aumentou ou diminuiu ou ficou indiferente, a porcentagem
-- que aumentou ou diminuiu, o usuario que fez a alteração e o horário em que foi feita:

CREATE OR REPLACE FUNCTION att_preco()
RETURNS TRIGGER AS $$
DECLARE pc FLOAT4;
BEGIN
	
	
	IF new.preco > old.preco THEN
		
		pc := ((new.preco - old.preco) / old.preco) * 100;
			
		INSERT INTO HISTORICO_PRECOS VALUES (old.nome_pizza, old.nome_pizzaria, old.preco, new.preco, 'Aumentou', pc, CURRENT_USER, NOW());
	
	ELSIF new.preco < old.preco THEN
		
		pc := ((old.preco - new.preco) / old.preco) * 100;
			
		INSERT INTO HISTORICO_PRECOS VALUES (old.nome_pizza, old.nome_pizzaria, old.preco, new.preco, 'Diminuiu', pc, CURRENT_USER, NOW());
	
	ELSIF new.preco = old.preco THEN
	
		pc := 0;
			
		INSERT INTO HISTORICO_PRECOS VALUES (old.nome_pizza, old.nome_pizzaria, old.preco, new.preco, 'Indiferente', pc, CURRENT_USER, NOW());
	
	END IF;
	
	RETURN NULL;

END $$ LANGUAGE 'plpgsql';

CREATE TRIGGER add_historico
AFTER UPDATE OF preco ON PIZZA
FOR EACH ROW
EXECUTE PROCEDURE att_preco();

-- Testes:

UPDATE PIZZA SET preco = 34.00 WHERE nome_pizza = 'Mussarela' and nome_pizzaria = 'Happy Pizza';
UPDATE PIZZA SET preco = 50.00 WHERE nome_pizza = 'Peperone' and nome_pizzaria = 'Que Delicia Pizzaria';
UPDATE PIZZA SET preco = 40.00 WHERE nome_pizza = 'Peperone' and nome_pizzaria = 'Que Delicia Pizzaria';
UPDATE PIZZA SET preco = 67.50 WHERE nome_pizza = 'Brigadeiro' and nome_pizzaria = 'Pizzaria Pizza Ria';
UPDATE PIZZA SET preco = 40.50 WHERE nome_pizza = 'Portuguesa' and nome_pizzaria = 'Pizzaria Anima Tudo';

SELECT *
FROM HISTORICO_PRECOS;

SELECT *
FROM PIZZA;
