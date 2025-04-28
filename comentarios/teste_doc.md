docker-compose up -d

docker ps

<span style ="color: #003f88; background-color: #cdb4db;">docker exec -it cont_mysql mysql -u adm -p</span>

USE nome_do_banco_de_dados;

<span style ="color: #003f88; background-color: #cdb4db;">USE dados_mysql;</span>

<span style ="color: #003f88; background-color: #cdb4db;">SHOW TABLES;</span>

Empty set (0.01 sec)

CREATE TABLE Professor (

    id INT PRIMARY KEY NOT NULL,

    nome VARCHAR(100) NOT NULL,

    idade INT,

    materia VARCHAR(100) NOT NULL,

    obs VARCHAR(200)
);

<span style = "color: #003f88; background-color: #cdb4db">
CREATE TABLE Professor (    id INT PRIMARY KEY NOT NULL,    nome VARCHAR(100) NOT NULL,    idade INT,    materia VARCHAR(100) NOT NULL,    obs VARCHAR(200));</span>

&nbsp;
retorno

Query OK, 0 rows affected (0.05 sec)

<span style=" color:#003f88; background-color: #cdb4db;">
INSERT INTO Professor (id, nome, materia, idade, obs) 
VALUES (1, 'João Silva', 'Matemática', 45, 'Professor titular');</span>
&nbsp;

retorno

ERROR 1146 (42S02): Table 'dados_mysql.Professor' doesn't exist

retorno após criar tabela
Query OK, 0 rows affected (0.05 sec)

ver se tudo foi salvo

todos os registros da tabela
<span style=" color:#003f88; background-color: #cdb4db;">
SELECT * FROM Professor;</span>

vê se a tabela existe,  no caso professor
<span style=" color:#003f88; background-color: #cdb4db;">
SHOW TABLES LIKE 'Professor';</span>

deve ser ' ' e não " "

+-----------------------------------+
| Tables_in_dados_mysql (Professor) |
+-----------------------------------+
| Professor                         |
+-----------------------------------+
1 row in set (0.00 sec)

listar id e nome

<span style=" color:#003f88; background-color: #cdb4db;">
SELECT id, nome FROM Professor;</span>

+----+-----------+
| id | nome      |
+----+-----------+
| 10 | Caio      |
| 11 | Odair     |
| 12 | Gustavooo |
| 13 | Evandro   |
+----+-----------+
4 rows in set (0.00 sec)

&nbsp;
especificar id
SELECT * FROM Professor WHERE id = [ID_PARA_TESTAR];
<span style=" color:#003f88; background-color: #cdb4db;">
SELECT * FROM Professor WHERE id = 10;</span>

ver estrutura da tabela pelo id
<span style=" color:#003f88; background-color: #cdb4db;">
DESCRIBE Professor;</span>

+---------+--------------+------+-----+---------+-------+
| Field   | Type         | Null | Key | Default | Extra |
+---------+--------------+------+-----+---------+-------+
| id      | int          | NO   | PRI | NULL    |       |
| nome    | varchar(100) | NO   |     | NULL    |       |
| idade   | int          | YES  |     | NULL    |       |
| materia | varchar(100) | NO   |     | NULL    |       |
| obs     | varchar(200) | YES  |     | NULL    |       |
+---------+--------------+------+-----+---------+-------+
5 rows in set (0.03 sec)


contagem de registros
<span style=" color:#003f88; background-color: #cdb4db;">
SELECT COUNT(*) FROM Professor;</span>

&nbsp;
+----------+
| COUNT(*) |
+----------+
|        4 |
+----------+

1 row in set (0.01 sec)


Verificar se o autocommit está ativado (deve estar ON)
<span style=" color:#003f88; background-color: #cdb4db;">
SELECT @@autocommit;</span>
&nbsp;

+--------------+
| @@autocommit |
+--------------+
|            1 |
+--------------+

1 row in set (0.01 sec)
Autocommit ligado (1): Todas as alterações são confirmadas (committed) automaticamente após cada comando SQL
Garantia de persistência: Quando você faz INSERT, UPDATE ou DELETE, as mudanças são imediatamente gravadas no disco

fechar total mysql

<span style=" color:#003f88; background-color: #cdb4db;">
EXIT;</span>
&nbsp;

refazer

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

<span style=" color:#003f88; background-color: #cdb4db;">
docker stop cont_mysql</span>

&nbsp;

<span style=" color:#003f88; background-color: #cdb4db;">
docker start cont_mysql</span>

&nbsp;


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

<span style = "color: #9b5de5">docker inspect cont_mysql | grep -A 10 Mounts</span>

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

