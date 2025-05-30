[Arquitetura](#arquitetura)
&nbsp;&nbsp;
[Tecnologias](#tecnologias)
&nbsp;&nbsp;
[Passo a passo](#passo-a-passo)
<br>
[Endpoints ](#endpoints)
&nbsp;&nbsp;
[Estrutura do projeto](#estrutura-do-projeto)
&nbsp;&nbsp;
[Autores](#autores)

&nbsp;
&nbsp;

# 🧑🏻‍💻Sistema Escolar👨🏻‍🏫

Este repositório possui infromações sobre professores, alunos e disciplinas.
<br>
<br>
## 🧰Arquitetura

Esta api gerencia sitemas de uma faculdade tendo as entidades professores, alunos e turmas/disciplina.
Este microsserviço faz parte de outro sistema que devem ser executados simultaneamente:

<br>
Reserva de Sala
<br>
https://github.com/Vinicioslima29/Reserva-de-sala.git
<br>
Controle de Atividade
<br>
https://github.com/Rafaelawr/Atividades.git
<br>
<br>

## 🔌Tecnologias
<br>
Python&nbsp,&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspFlask,&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspJinja,&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspDocker,
&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspSQLAlchemy,&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspSQLite,&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspVPM,&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspRender
<br  
<br>

## 🥾Passo a passo

#### 1° No Github copiar o url e o https 

https://github.com/EduardoRm61/Grupo8_Api_Impacta.git
<br>
#### 2° No editor de código desejado clonar o repositório

No terminal 
- criar uma pasta - mkdir nomeDaPasta
- cd nomeDaPasta
- code .
- ctrl + j para abrir terminal
- git clone url
&nbsp;
#### 3° Instalar as dependências

No terminal
- pip install -r requirements.txt
&nbsp;
#### 4° Executar API

No terminal
- python pessoa_service/app.py
    retorno será http://localhost:5002
<br>
<br>

## 🌐Endpoints 

Todos médoto get/get(id)/post/put/delet

- ttp://localhost:5002/api/docs
<br>
<br>

## 🧱Estrutura do projeto

<br>grupo8_api_impacta/
<br>|
<br>|-- apps/
<br>|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- alunos/
<br>|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- model_aluno.py
<br>|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- route_aluno.py
<br>|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|
<br>|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- professores/
<br>|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- model_prof.py
<br>|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- route_prof.py
<br>|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|
<br>|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- swagger/
<br>|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- namespace/
<br>|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- aluno_namespaces.py
<br>|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- professor_namespaces.py
<br>|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- turma_namespaces.py
<br>|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- __init__.py
<br>|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- swagger_config.py
<br>|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|
<br>|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- turma/
<br>|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- model_turma.py
<br>|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- route_turma.py
<br>|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|
<br>|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- venv/
<br>|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|
<br>|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- app.py
<br>|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- config.py
<br>|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- init_db.py
<br>|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- README.md
<br>|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-- testes.py
<br>|
<br>|-- docker-compose.yaml
<br>|-- Dockerfile
<br>|-- Procfile
<br>|-- requirements.txt
<br>|
<br>|__________

## 📝Autores

Alessandra F Rigonatti
<br>
Eduardo Nunes
<br>
Rafaela Rodrigues
<br>
Thainá Foltran
<br>
Vinicius de Lima

<br>
