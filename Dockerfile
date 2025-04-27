

FROM python:3.9
# do python:3 pegue sua imagem

WORKDIR /app
#defina o diretório de trabalho dentro do contêiner , colocando apenas nome da pasta
# ex C:\Users\ar\deletarr\Grupo8_Api_Impacta - ficaria apenas Grupo8_Api_Impacta
 
COPY requirements.txt .
RUN pip install -r requirements.txt
# copiando e instalando todas bibliotecas entre outros, na versão usada
# ponto no final está relacionado a pasta raiz

COPY . .
#copiar tudo que está na pasta e leve ao destino, raiz do docker, por exemplo

EXPOSE 5002

CMD ["python", "apps/app.py"]

# define o comando que será executado ao iniciar o contêiner | roda





# -----------------------------------------------------------------------------------#
#      comando ( comando 1, ir para dockerdesktop, play na imagem, volta 2°)         #
#                                                                                    #
#                                                                                    #
#                         docker build -t grup9-api .                                #
#                      docker run -p 5002:5002 grup9-api    (rodar o compose, não este)                            #
#                                                                                    #
# -----------------------------------------------------------------------------------#