

FROM python:3.9-slim
# do python:3 pegue sua imagem
# IMAGEM REDUZIDA COM BÁSICO DO PYTHON, MAIS LEVE, PROJETOS MENORES
WORKDIR /app
#defina o diretório de trabalho dentro do contêiner , colocando apenas nome da pasta
# ex C:\Users\ar\deletarr\Grupo8_Api_Impacta - ficaria apenas Grupo8_Api_Impacta
 
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# --user é para evitar conflitos ao instalar a dependência
# copiando e instalando todas bibliotecas entre outros, na versão usada
# ponto no final está relacionado a pasta raiz

COPY . .
#copiar tudo que está na pasta e leve ao destino, raiz do docker, por exemplo

ENV PYTHONPATH=/app

EXPOSE 5002

CMD ["python", "apps/app.py"]

# define o comando que será executado ao iniciar o contêiner | roda





# -----------------------------------------------------------------------------------#
#      comando ( comando 1, ir para dockerdesktop, play na imagem, volta 2°)         #
#                                                                                    #
#                                                                                    #
#                         docker build -t grup9-api .                                #
#      docker run -p 5002:5002 grup9-api    (rodar o compose, não este)              #
#                                                                                    #
# -------------------------------------------------------------------------------#