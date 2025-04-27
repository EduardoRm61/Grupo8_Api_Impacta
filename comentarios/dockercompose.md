EXECUTAR CONTÊINER - PASSANDO VARIÁVEL DE AMBIENTE 
&nbsp;
OBS:  ao rodar apenas docker mysql:verão (tipo8.0) - haverá um ma mensagem de erro pedindo para configuar senha.
&nbsp;
<span style="color:rgb(119, 178, 237); background-color:rgb(11, 43, 75);"> docker run -e MYSQL_ALLOW_EMPTY_PASSWORD=yes -v mysql:latest </span>
&nbsp;
<span style="color:rgb(119, 178, 237); background-color:rgb(11, 43, 75);"> docker run -e  </span>
&nbsp;
Estava errado pois coloquei uma , no lugar de ; após 1° cor - -span style="color: #0466c8,MYSQL_ROOT_PASSWORD:ro0ts  <- aqui
&nbsp;
retorno: Docker Compose version v2.34.0-desktop.1