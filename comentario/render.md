### <center> 👻 Render 👀</center>
&nbsp;

Transforma o cód em "imagens" que iremos ver no pag web/ navegador

Pega o cód, traduz e "vetoriza"

Resumindo - Crio meus código no Vscode(ou outro editor de cód) que dará infromações para o servidor que manda para o navegador que irá interpretar, renderizar e mostrar na tela o resultado

services:
  type: web

Configura que está configurado um serviço do tipo web - requisito https

name: grupo8-api

identificador interno da api no provedor de hospedagem

runtime: python
buildCommand: pip install -r requirements.txt

startCommand: gunicorn app:app

inicia a aplicação ao iniciar
gunicorn servidor HTTP que roda Flask
app:app nome do módulo do arquivo app.py (módulo python): variável app do flask

envVars:
. - key: FLASK_ENV
value: production

aqui configura o Flask em modo de produção, desativando debug mode

plan: free

plano de hospedagem gratuito