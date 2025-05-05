## COMANDOS SQLIGHT TERMINAL

### FEITO 1° NO TERMONAL E EM SEGUIDA FILE

JÁ TINHA FEITO, ENTÃO VOU TERMINAR DE VER CRUED NO TERMINAL

RESETAREI NO FINAL E FAREI FILE DE TESTE, PARA APENAS RODAR-LO

#### Comandos 

1° Verificar se o servidor está rodando
<span style="color: #f4acb7; background-color: rgb(41, 43, 42)" > python app.py </span>

retorno neste caso:
Running on http://127.0.0.1:5002

2° 
<span style="color: #f4acb7; background-color:rgb(41, 43, 42);" > sqlite3 instance/app.db</span>

DEVIDO PROBLEMA EM OUTRAS TABELAS CRIEI UM PARA ANALISAR PROFESSOR

APPS/ temporario_professor_test

para rodar

- Executar
<span style="color: #f4acb7; background-color:rgb(41, 43, 42);" > python -m apps.tempo_prof_test</span>

retorno:
 * Running on http://127.0.0.1:5002

 - quanto quiser removel/deletar no terminal
<span style="color:rgba(160, 12, 165, 0.86);" > python -m apps.temporario_professor_test</span>

&nbsp;

- GET "all"

<span style="color: #f4acb7; background-color:rgb(41, 43, 42);" > curl -X GET http://localhost:5002/professores/professores</span>

retorno:
{
  "mensagem": "Ok",
  "professores": []
}

- POST 

curl -X POST http://localhost:5002/professores/professores \
-H "Content-Type: application/json" \
-d '{
    "id": 1,
    "nome": "Carlos Silva",
    "materia": "Matemática",
    "idade": 45,
    "obs": "Professor titular"
}'

resposta: 
.!doctype html>
.html lang=en>
title>400 Bad Request</title>
h1>Bad Request</h1>
p>Failed to decode JSON object: &#39;utf-8&#39; codec can&#39;t decode byte 0xe1 in position 123: invalid continuation byte</p>

tradução : <span style="color: red;"> NÃO USE CARATERES ESPECIAIS</span>

curl -X POST http://localhost:5002/professores/professores \
-H "Content-Type: application/json" \
-d '{
    "id": 1,
    "nome": "Carlos Silva",
    "materia": "Matematica",
    "idade": 45,
    "obs": "Professor titular"
}'

retorno:
{
  "mensagem": "Created",
  "professor": {
    "id": 1,
    "idade": 45,
    "materia": "Matematica",
    "nome": "Carlos Silva",
    "obs": "Professor titular"
  }
}

- testando não por parte obrigatória

curl -X POST http://localhost:5002/professores/professores \
-H "Content-Type: application/json" \
-d '{
    "id":4,
    "nome": "Tkai",
    "materia": "",
    "idade": ,
    "obs": ""
}'

retorno esperado:

!doctype html>
html lang=en>
title>400 Bad Request</title>
h1>Bad Request</h1>
p>Failed to decode JSON object: Expecting value: line 5 column 14 (char 66)</p>

arrumando:

 curl -X POST http://localhost:5002/professores/professores -H "Content-Type: application/json" -d '{
    "id":4,
    "nome": "Tkai",
    "materia": "Eng de Requi",
    "idade":null ,
    "obs": null
}'

- - GET ID

<span style="color: #f4acb7; background-color:rgb(41, 43, 42);" > curl -X GET http://localhost:5002/professores/professores/2</span>

RETORNO:

{
  "mensagem": "Ok",
  "professor": {
    "id": 2,
    "idade": 23,
    "materia": "Dev API Mmicros",
    "nome": "Caio",
    "obs": "resposavel pela prova api api"
  }
}
 LISTA


TESTANDO FORA DA LISTA

curl -X GET http://localhost:5002/professores/professores/7
{
  "mensagem": "error",
  "professor": "Not Found: Erro, Professor n\u00e3o indentificado ou existente!"
}

- PUT/ ATUALIZAR

curl -X PUT http://localhost:5002/professores/professores/4 \
-H "Content-Type: application/json" \
-d '{
    "nome": "Takai"
}'

retorno:

{
  "mensagem": "Atualizado",
  "professor": {
    "id": 4,
    "idade": null,
    "materia": "Eng de Requi",
    "nome": "Takai",
    "obs": null
  }
}

- DELETE

curl -X DELETE http://localhost:5002/professores/professores/deletar/1

resultado

!doctype html>
html lang=en>
  head>
    title>TypeError: unhashable type: &#39;dict&#39;
 // Werkzeug Debugger</title>
    link rel="stylesheet" href="?__debugger__=yes&amp;cmd=resource&amp;f=style.css">
    link rel="shortcut icon"
        href="?__debugger__=yes&amp;cmd=resource&amp;f=console.png">
    script src="?__debugger__=yes&amp;cmd=resource&amp;f=debugger.js"></script>
    script>
      var CONSOLE_MODE = false,
          EVALEX = true,
          EVALEX_TRUSTED = false,
          SECRET = "4RQNCOdslFnB2tMcVekk";
    /script>
  /head>
  body style="background-color: #fff">
    div class="debugger">
h1>TypeError</h1>
div class="detail">
  p class="errormsg">TypeError: unha....

devido na rota_prof.py
    try:
        resultado = modf.deletarProfessorPorId(id_professor)
        return jsonify({"mensagem": "Ok", "professor": resultado}), 200
Erro em {resultado} - deve ser apenas resultado, sem chaves

novo cód com novo resultado:

curl -X DELETE http://localhost:5002/professores/professores/deletar/4
{
  "mensagem": "Ok",
  "professor": {
    "mensagem": "Professor Tkai eletado"
  }
}

- reset

curl -X DELETE http://localhost:5002/professores/professores/resetar

retorno

{
  "mensagem": "Ok",
  "professor": "Resetado"
}
