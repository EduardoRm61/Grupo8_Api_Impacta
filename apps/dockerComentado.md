------------------------ CONFIGURAÇÃO DO CONTÊINER ------------------------------------------

                           DOCKER DEVE ESTAR RUNNIG


 por conversão, o nome do file é com D maiúsculo mesmo
 Docker vai ler e vai criar imagem
 imagem = pacote imutável que tem camadas leves de dependências, bibliotecas, configurações | cód de aplicações ex file.py | instruções
 em imagem não tem Kernel(seria o "núcleo da máquina que está rodando") completo do os
 contêiner é a instância/objeto da imagem(pacote) em execcução

 criar um folder e deixar fora apenas arquivo Dockerfile e requirements.txt

FROM python:3.9
 do python:3 pegue sua imagem

WORKDIR /app
defina o diretório de trabalho dentro do contêiner , colocando apenas nome da pasta
 ex C:\Users\ar\deletarr\Grupo8_Api_Impacta - ficaria apenas Grupo8_Api_Impacta
 
COPY requirements.txt .
RUN pip install -r requirements.txt
 ESTAVA ASSIM RUN pip install -r requirementes.txt OBSERVAR FINAL COM TES, MAS O CORRETO É NTS
 copiando e instalando todas bibliotecas entre outros, na versão usada
 ponto no final está relacionado a pasta raiz
 pasta raiz = devo analisar os files que serão rodados/principais como dockerfile e app.py, se está na filha a filha é raiz (pouco confuso para mim, entendi levemente) 


COPY . .
copiar tudo que está na pasta e leve ao destino, raiz do docker, por exemplo

CMD ["python", "apps/app.py"]

 define o comando que será executado ao iniciar o contêiner | roda


# -------------------------------------- RODAR E CRIAR IMAGEM - TERMINAL bash ------------------------------
    
# explicação dada
# dockfile é quase uma receita (posso dizer quase um protocolo?) que cria um pacote(imagem) do app
# para rodar

# !!!!!!!!!    docker build -t grupo8-testedock .     !!!!!!!!!    -feito ok   
# ATENÇÃO NOME ESTAVA docker build -t grupo8_testeDock .
# DEU 
#docker build -t grupo8_testeDock .
# ...
# ERROR: invalid tag "grupo8_testeDock": repository name must be lowercase
# TRADUZINDO - APENAS LETRAS MINÚSCULAS
# outro erro
# É PERMITIDO - TRAÇO E . PONTO
# NÃO É PERMITIDO _ E / SEM CONTEXTO DE REPOSITÓRIO (EX: app/configuração - acho eu)

# -t = tag/etiqueta = nome que dará a imagem
# o ponto no final mostra a pasta raiz 
# (grupo8-flask é nome que será criado da imagem)

# run contêiner

# !!!!!!!!!    docker run -p 5000:5000 --name projetoapp grupo8-flask     !!!!!!!!!      ---- foi

# -p = mapeamento de portas - 1° 5000 porta do localhost (host/meu computador) 2° 5000 relacionado com rota do flask (n° padrão)
# resumindo quando acessa o url localhost:500 o docker reddireciona para o 5000 relacionado ao contêiner
# no docker desktop - contêiner 
# run contêiner

#    obs
# outro lugar fez 
# !!!!!!!!!    docker run -it nomeImagem     !!!!!!!!!  
# -it de interatico

# !!!!!!!!!    docker exec meu-flask python testes.py     !!!!!!!!!

# no terminal onde roda os comandos

# como entregar o trabalho
# enviar a pasta do projeto
# enviar a imagem - para exportar 

# !!!!!!!!!    docker save -o grupo8-flask.tar grupo8-flask     !!!!!!!!!

# .tar formato compactado comum no linux - ele empacota imagem docker em um único arquivo

#comandos que podem ser úteis
# docker ps                    - lista contêiners ativos
# docker stop meu-flask        - para o contêiner
# docker rm meu-flask          - remove o contêiner]
# docker rmi grupo8-flask      - remove a imagem

#mandar para git é comando normal mesmo


#          ERRO QUE NÃO ENTENDO 

# docker build -t grupo8_testeDock .
# ERROR: error during connect: Head "http://%2F%2F.%2Fpipe%2FdockerDesktopLinuxEngine/_ping": open //./pipe/dockerDesktopLinuxEngine: The system cannot find the file s
# pecified.

# 1° ver se está rodando

# !!!!!!!!!     docker run hello-world     !!!!!!!!!

# resposta
# Hello from Docker!
# This message shows that your installation appears to be working correctly.
# ...
# lista contêiner ativos

# !!!!!!!!!      docker ps     !!!!!!!!!

# resposta
# docker ps
# CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
# lista de contêiners geral

# !!!!!!!!!      docker ps -a     !!!!!!!!!

# todos deram resposta positivas


# pwd
# verifica  diretório
# resposta
# c/Users/ar/API/Grupo8_Api_Impacta
# cd app
# ls -ls
# para listar diretórios  e arquivos no local com detalhes, icluindo permissões, proprietário, grupo, tamanho, data de modificação
# exempro de resposta
# ls = Linux/unix (inclui Mac e windows) | -la = flag - lista detalhada em formato detalhado (-l) + mostrar arquivos ocultos (-a =  all)
# total 63
# drwxr-xr-x 1 arfur 197609     0 Apr  8 22:44 ./
# drwxr-xr-x 1 arfur 197609     0 Apr  8 22:44 ../
# -rw-r--r-- 1 arfur 197609   913 Apr  8 08:12 .gitignore
# drwxr-xr-x 1 arfur 197609     0 Apr  7 18:47 .vscode
# observação - significados
# d:   É um diretório.
# rwx: Permissões do dono (ler, escrever, executar).
# r-x: Permissões do grupo (ler, executar).
# r-x: Permissões de outros (ler, executar).

# ! ! ! ! ! ! RODOU ! ! ! ! 

# ERRO NO REQUIREMENTS - instalação do requirements.txt
# retorno
# Dockerfile:20
# --------------------
#   18 |
#   19 |     COPY requirements.txt .
#   20 | >>> RUN pip install -r requirements.txt
#   21 |     # ESTAVA ASSIM RUN pip install -r requirementes.txt OBSERVAR FINAL COM TES, MAS O CORRETO É NTS
#   22 |     # copiando e instalando todas bibliotecas entre outros, na versão usada
# --------------------
# ERROR: failed to solve: process "/bin/sh -c pip install -r requirements.txt" did not complete successfully: exit code: 1

#ls -la requirements.txt
# RESPOSTA
#-rw-r--r-- 1 arfur 197609 1287 Apr  8 17:35 requirements.txt
# ISSO É QUE ESTÁ NO LOCAL QUE ESTOU (PASTA APP)
#cat requirements.txt
# verifica o conteúdo do file !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! muito legal
# resposta 
# alembic==1.13.3
# asttokens==2.4.1
# beautifulsoup4==4.13.3 .....
# cat -e requirements.txt
# alembic==1.13.3^M$
# asttokens==2.4.1^M$
# beautifulsoup4==4.13.3^M$
# cat = concatenate - concatenar = função original é junta do arquivo
# cat mostra o conteúdo de arquivos no terminal
# o -e caracteres ocultos (exemplo quebra de linhas, espaço, caractéres inválidos)
# Adiciona $ no final de cada linha (para visualizar onde terminam as linhas)
# ^M = caractere especial do Windows

# ARRUMAR PROBLEMA COM CARACTERES ESPECIAIS - bash

#          !!!!!!! sed -i 's/\r$//' requirements.txt  # Linux/macOS     !!!!!!!! 
# converter arquivo em unix, até onde entendi tira estes caracteres especiais
#



#refazendo
# docker build -t grupo8 .
# docker run -p 5000:5000 grupo8
# docker exec projetoapp python testes.py  # deu erro

# 1. Construir a imagem
# 2. Executar o container com nome apropriado
# docker run -d -p 5000:5000 --name projetoapp grupo8-testedock
#obs:
# docker run -p 5000:5000 --name projetoapp grupo8-testedock
# o -p modo interativo - foreground - roda em 1° - terminal fica travado enquanto conteiner roda
# docker run -d -p 5000:5000 --name projetoapp grupo8-testedock
# mode desanexado (detached/background) - roda em segundo plano, não bl0quendo o terminal, pode usar outros comandos no terminal enquanto o contêiner roda
# 3. Executar o script dentro do container (quando estiver rodando)
# docker exec projetoapp python testes.py



# ----------------------------------------------------------------

docker build -t grupo8 .
# docker run -p 5000:5000 --grupo8
# docker run -p 5000:5000 grupo8