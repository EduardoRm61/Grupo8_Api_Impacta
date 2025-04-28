cmd como adm

netstat -ano | findstr :5002

retorno
  TCP    0.0.0.0:5002           0.0.0.0:0              LISTENING       15151
  TCP    [::]:5002              [::]:0                 LISTENING       14141
  TCP    [::1]:5002             [::]:0                 LISTENING       13131

anotar o pid

taskkill /PID NUMERO_PID /F

taskkill /PID 15151 /F

retorno
ÊXITO: o processo com PID 15368 foi finalizado.
ou
ERRO: o processo "15368" não foi encontrado.

fecha o processo

.............................
docker exec -it cont_mysql mysql -u root -psenha
ocker exec -it cont_mysql mysql -u root -psenha123

docker exec = executar um comando dentro do container

-it = modo interativo e terminal

cont_mysql = nome do contêiner

mmysql dentro do contêiner mysql

-u root = usuário do mysql

-p senha-password

senha123

deixe para digitar a senha depois
docker exec -it cont_mysql mysql -u root -p

resposta

docker exec -it cont_mysql mysql -u adm -p 
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 164
Server version: 8.0.42 MySQL Community Server - GPL

Copyright (c) 2000, 2025, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
agora estou dentro do mysql
