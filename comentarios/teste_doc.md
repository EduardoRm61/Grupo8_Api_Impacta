docker-compose up -d

docker ps

docker exec -it cont_mysql mysql -u adm -p

USE nome_do_banco_de_dados;

USE dados_mysql;

SHOW TABLES;

Empty set (0.01 sec)

INSERT INTO Professor (id, nome, materia, idade, obs) 
VALUES (1, 'João Silva', 'Matemática', 45, 'Professor titular');