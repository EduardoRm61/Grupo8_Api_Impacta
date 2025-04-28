docker-compose up -d

docker ps

docker exec -it cont_mysql mysql -u adm -p

USE nome_do_banco_de_dados;

USE dados_mysql;

SHOW TABLES;

Empty set (0.01 sec)

CREATE TABLE Professor (
    id INT PRIMARY KEY NOT NULL,
    nome VARCHAR(100) NOT NULL,
    idade INT,
    materia VARCHAR(100) NOT NULL,
    obs VARCHAR(200)
);

CREATE TABLE Professor (    id INT PRIMARY KEY NOT NULL,    nome VARCHAR(100) NOT NULL,    idade INT,    materia VARCHAR(100) NOT NULL,    obs VARCHAR(200));

retorno

Query OK, 0 rows affected (0.05 sec)


INSERT INTO Professor (id, nome, materia, idade, obs) 
VALUES (1, 'João Silva', 'Matemática', 45, 'Professor titular');

retorno
ERROR 1146 (42S02): Table 'dados_mysql.Professor' doesn't exist

retorno após criar tabela
Query OK, 0 rows affected (0.05 sec)

ver se tudo foi salvo

todos os registros da tabela
SELECT * FROM Professor;

contagem de registros
SELECT COUNT(*) FROM Professor;
+----------+
| COUNT(*) |
+----------+
|        4 |
+----------+

1 row in set (0.01 sec)


Verificar se o autocommit está ativado (deve estar ON)
SELECT @@autocommit;
+--------------+
| @@autocommit |
+--------------+
|            1 |
+--------------+
1 row in set (0.01 sec)
Autocommit ligado (1): Todas as alterações são confirmadas (committed) automaticamente após cada comando SQL
Garantia de persistência: Quando você faz INSERT, UPDATE ou DELETE, as mudanças são imediatamente gravadas no disco

fechar total mysql
EXIT;

docker exec -it cont_mysql mysql -u adm -p dados_mysql -e 
"SELECT * FROM Professor;"
+----+-----------+-------+---------+-----------------------+
| id | nome      | idade | materia | obs                   |
+----+-----------+-------+---------+-----------------------+
| 10 | Caio      |    23 | Api     | Reponsvel pelo deploy |
| 11 | Odair     |    30 | Amb Des | Docker com api        |
| 12 | Gustavooo |    30 | Mobile  | sexta da maldade      |
| 13 | Evandro   |    30 |         |                       |
+----+-----------+-------+---------+-----------------------+

docker stop cont_mysql

docker start cont_mysql

docker exec -it cont_mysql mysql -u adm -p dados_mysql -e 
"SELECT * FROM Professor;"
+----+-----------+-------+---------+-----------------------+
| id | nome      | idade | materia | obs                   |
+----+-----------+-------+---------+-----------------------+
| 10 | Caio      |    23 | Api     | Reponsvel pelo deploy |
| 11 | Odair     |    30 | Amb Des | Docker com api        |
| 12 | Gustavooo |    30 | Mobile  | sexta da maldade      |
| 13 | Evandro   |    30 |         |                       |
+----+-----------+-------+---------+-----------------------+

Persistência efetiva: Os dados sobreviveram ao reinício do container

Volume Docker funcionando: Seu container está corretamente configurado com armazenamento persistente

docker inspect cont_mysql | grep -A 10 Mounts
            "Mounts": [
                {
                    "Type": "volume",
                    "Source": "grupo8_api_impacta_mysql_data",
                    "Target": "/var/lib/mysql",
                    "VolumeOptions": {}
                }
            ],
            "MaskedPaths": [
                "/proc/asound",
                "/proc/acpi",
--
        "Mounts": [
            {
                "Type": "volume",
                "Name": "grupo8_api_impacta_mysql_data",
                "Source": "/var/lib/docker/volumes/grupo8_api_impacta_mysql_data/_data",
                "Destination": "/var/lib/mysql",
                "Driver": "local",
                "Mode": "z",
                "RW": true,
                "Propagation": ""
            }

            deveria mostrar este mapeamento mesmo