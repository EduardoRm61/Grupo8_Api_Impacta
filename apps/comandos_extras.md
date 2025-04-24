 ### <center>Comandos extras<center/>
 &nbsp;
 - <b>erro na porta do local para remoto </b>
&nbsp;
    antes deve Executar o script de entrada da aplicação/ run the application entry script/ Subir a aplicação 
    tudo isso é rodar 
&nbsp;
    <span style="color: #0466c8; background-color: #d9dcd6;">python app.py (no caso python apps/app.py)</span>
&nbsp;
    não fecha, abra outro terminal, pode ser powershell e rode o cód
&nbsp;
    <span style="color: #0466c8; background-color: #d9dcd6;">netstat -ano | findstr :5002</span>
&nbsp;
    netstat -> Ferramenta do Windows que mostra estatísticas de rede e conexões ativas

    -a -> Mostra todas as conexões e portas em escuta (LISTENING)
    Listening/ escutando = estado de um processo que está ativamente aguardando conexões de entrada em uma porta específica
    Flask roda app.run(), ele coloca o servidor no estado LISTENING na porta configurada (ex: 5002)

    -n -> Exibe números de portas e endereços IP em formato numérico (ao invés de tentar resolver nomes)

    -o -> Mostra o ID do processo (PID) associado a cada conexão

    (pipe) -> Redireciona a saída do netstat para o próximo comando (findstr)

    findstr :5002 -> Filtra apenas as linhas que contêm :5002 (sua porta do Flask)
&nbsp;
    retorno:
    <span style="font-family: monospace; white-space: pre;">TCP    127.0.0.1:5002         0.0.0.0:0              LISTENING       10088</span>
&nbsp; 
    TCP = protocolo de rede usado/ Transmission Control Procol  
    o flask está usando tcp para conexões http/web
    obs - UDP = conexões sem estados
&nbsp;
    127.0.0.1 = ip do localhost (conexões da própria máquina)
&nbsp;

    - <b><u> se quiser acessar de outra máquina ou docker deve mudar para 0.0.0.0 (endereço remoto) - ficando 0.0.0.0:5002 </u></b>
&nbsp;
    :5002 = porta onde o flask "ouve"
&nbsp;
Resultado -  config.py mudou de ao rodar a  1° vez apareceu mensagem de que se quero permitir acesso externo. No docker a porta foi "aceita"
&nbsp;
&nbsp;
- <b> Problema push github </b>
&nbsp;

    <span style="color:rgb(35, 59, 14); background-color:rgb(248, 252, 213);">git branch</span>
&nbsp;
    ver se está na branch a ser enviada
&nbsp;

    <span style="color:rgb(35, 59, 14); background-color:rgb(248, 252, 213);">git log --oneline</span>
&nbsp;
    ver commits locais
&nbsp;

    <span style="color:rgb(35, 59, 14); background-color:rgb(248, 252, 213);">git remote -v</span>
&nbsp;
    ver quel repositório remoto está, neste caso aparece:
    origin  https://github.com/EduardoRm61/Grupo8_Api_Impacta.git (fetch)
    origin  https://github.com/EduardoRm61/Grupo8_Api_Impacta.git (push)
&nbsp;
    Apenas relembrando:
&nbsp;
    <span style="color:rgb(35, 59, 14); background-color:rgb(248, 252, 213);">git add . ou git add nomeFile</span>
&nbsp;
    adicona todos arquivos ou envia apemas arquivo/s posto/s
&nbsp;

    <span style="color:rgb(35, 59, 14); background-color:rgb(248, 252, 213);">git commit -m "recumo"</span>
&nbsp;
    prepara para envio para nuvem , promessa de envio
&nbsp;

    <span style="color:rgb(35, 59, 14); background-color:rgb(248, 252, 213);">git push --all ou git push origin nomeBranch</span>
&nbsp;
    envia para o github tudo ou apenas a branch desejada
&nbsp;

    <span style="color:rgb(35, 59, 14); background-color:rgb(248, 252, 213);">git push -u origin nomeBranch</span>
&nbsp;
    força a criação do branch remoto, caso seja novo (aqui não é o caso) - só curiosidade mesmo
&nbsp;
    - <b><span style="color: #bc4b51;">volta para estatus/commit anterior</span></b>
    Dei um git pull e desarrumou tudo, então resolvi voltar para o último commit feito e arrumado
&nbsp;
    <span style="color:rgb(35, 59, 14); background-color:rgb(248, 252, 213);">git reflog</span>
&nbsp;
    verifica histórico de commit, mostra todas ações recentes do git
    retorna algo assim:
    4396e26 (HEAD -> professor) HEAD@{0}: commit: fix config branch professor
    c4dbcde HEAD@{1}: commit: fix na branch professor
    38aca36 (develop) HEAD@{2}: checkout: moving from develop to professor
    .....
    obsrvar 4396e26 (HEAD -> professor) <u><i><b> HEAD@{0} </u></i></b> - é este que deverá analisar e por no comando no terminal, meu caso foi {0}
    obs: para sair apertar <b>q</b>
&nbsp;
    <span style="color:rgb(35, 59, 14); background-color:rgb(248, 252, 213);">git reset --hard HEAD@{N° QUE QUER VOLTAR DO COMMIT}</span>
&nbsp;
    retonou assim:
    <u>HEAD is now at 4396e26 </u>fix config branch professor config.py - troca de localhost para 0.0.0.0 trocando e arrumando .txt para .md
    voltou para o que eu queria
    detalhe, não fiz push dele, só existia no local
&nbsp;
    - <b>forçando envio para remoto</b>
&nbsp;
    <span style="color:rgb(35, 59, 14); background-color:rgb(248, 252, 213);">git push -f origin professor</span>
&nbsp;
    Como minha branch está atrás do remoto, teria de fazer o pull, mas ele está muito desatualizado (fiz push que não foram), então resolvi forçar
&nbsp;
&nbsp;
-----------------------------------------------------------------------
-----------------------------------------------------------------------
### Utilizando MYSQL com Docker - AlgaWorks - tentativa 1

-----------------------------------------------------------------------
-----------------------------------------------------------------------
&nbsp;
Não tendo no local (SO) o servidore MySql
&nbsp;
usaremos docker
&nbsp;
- ver se docker foi feito com sucesso
&nbsp;
    <span style="color:rgb(245, 57, 104); background-color: #d8e2dc;">docker version</span>
&nbsp;
    Tipo de resposta que deve aparecer:
    Client:
    Version:           28.0.1
    ...
    Server: Docker Desktop 4.39.0 (184744)
    ...
&nbsp;
    Imagem = conjunto de arquivos e instruções para um contêiner rodar - todo servidor sql + componetes independentes
&nbsp;
    Docker register - onde ficam as imagens
    Comando para puxar a imagem
&nbsp;
    <span style="color:rgb(245, 57, 104); background-color: #d8e2dc;">docker pull mysql</span>
&nbsp;
    retorno esperado:
    ...
    Status: Downloaded newer image for mysql:latest
    docker.io/library/mysql:latest
&nbsp;
    Obs: 1° vê se tem a imgem no computador, se não tiver busca no docker
&nbsp;
    Foi baixado versão latest
    Latest = tag padrão que diz que a versão mais recente estável foi baixada
    Para saber a versão
&nbsp;
    <span style="color:rgb(245, 57, 104); background-color: #d8e2dc;">docker run --rm mysql:latest mysql --version</span>
&nbsp;
    tipo de resposta:
    mysql  Ver 9.3.0 for Linux on x86_64 (MySQL Community Server - GPL)
&nbsp;
    Como em lastes a verão irá mudar conforme lançamento, <span style ="color: #f28482;"> NÃO SE USA EM AMBIENTE DE PRODUÇÃO</span>
&nbsp;
    <span style="color:rgb(245, 57, 104); background-color: #d8e2dc;">docker pull mysql:9.3.0</span>
&nbsp;
    Peguei referência dada da versão do latest
    Ver imagens <span style="color:rgb(245, 57, 104); background-color: #d8e2dc;">docker images</span>, terão duas imagens
    resposta neste caso:
    mysql        9.3.0     7839322bd6c3   5 days ago    1.17GB
    mysql        latest    7839322bd6c3   5 days ago    1.17GB
&nbsp;
    site hub.docker.com -> pesquisar mysql -> aoarecerá uma lista -> clicar na mysql docker official images (tem um golfinho) -> tem tudo para rodar e usar a imagem.
&nbsp;
    Rodar/run a imagem do mysql com a versão
&nbsp;
    <span style="color:rgb(245, 57, 104); background-color: #d8e2dc;">docker run mysql:9.3.0</span>
&nbsp;
    <span style="color:#ffba08; background-color: #0d3b66;">AQUI CRIPU SEM NOMEAR O CONTÊINER, DESCENDO TEM COMO FAZER JÁ NOMEANDO </span>
    <span style="color:rgb(245, 57, 104); background-color: #d8e2dc;">docker run -e MYSQL_ROOT_PASSWORD=senha --name nomeConteiner -d mysql:9.3.0</span>
&nbsp;
    Resposta com ok e erro:
    2025-04-20 20:01:16+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 9.3.0-1.el9 started.
    2025-04-20 20:01:17+00:00 [Note] [Entrypoint]: Switching to dedicated user 'mysql'
    2025-04-20 20:01:17+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 9.3.0-1.el9 started.
    2025-04-20 20:01:17+00:00 [ERROR] [Entrypoint]: Database is uninitialized and password option is not specified
        You need to specify one of the following as an environment variable:
        - MYSQL_ROOT_PASSWORD
        - MYSQL_ALLOW_EMPTY_PASSWORD
        - MYSQL_RANDOM_ROOT_PASSWORD
&nbsp;
    Precisa de senha para associar o root/usuário 
    senha fixa - MYSQL_ROOT_PASSWORD
    senha vazia - MYSQL_ALLOW_EMPTY_PASSWORD
    senha aleatória - MYSQL_RANDOM_ROOT_PASSWORD
&nbsp;
        <span style="color:rgb(245, 57, 104); background-color: #d8e2dc;">docker run -e MYSQL_ROOT_PASSWORD=ro0t mysql:9.3.0 (coloquei ro0t - r o zero t)</span>
&nbsp;
    -e = environment variable/ambiente variável - define variáveis dentro do contêiner
    .......................................................................- configura software e ser executado no contêiner
    .......................................................................- passa parâmetros sensíveis como senha de froma segura
    obs: as informações ficam no contêiner e não nas imagens
&nbsp;
    resposta ao rodar:
    ...
    qld: ready for connections. Version: '9.3.0'  socket: ...
&nbsp;
    Deixar o terminal como está, abrir outro (abri git bash mesmo)
&nbsp;
    Pegar infromações do contêiner rodando <span style="color:rgb(245, 57, 104); background-color: #d8e2dc;">docker ps</span>
&nbsp;
    retorno que deu:
    55...46b   mysql:9.3.0   "docker-entrypoint.s…"   3 minutes ago    Up 3 minutes    3306/tcp, 33060/tcp    distracted_merkle
&nbsp;
    obs: acessar contêiner vou usar a porta exposta 3306/tcp
&nbsp;
    destravar o ternimal
    1 . para de rodar o contêiner
    <span style="color:rgb(245, 57, 104); background-color: #d8e2dc;">docker stop 5597367f746b (docker stop id ou docker stop nome Conteiner)</span>
&nbsp;
    Quando dá <span style="color:rgb(245, 57, 104);">docker ps</span> e não tem contêiners rodando retonar apenas:
    CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
&nbsp;
    Quando dá <span style="color:rgb(245, 57, 104);">docker ps -a</span> pega todos contêiners, mesmo os não rodando
    -a = all
&nbsp;
    Remover contêiners antigos que não serão usados (removerei mais de um usando o nome agora)
    DEVEM ESTAR PARADOS, SE ESTIVEREM RODANDO ETRÁ DE FORÇAR (-f)
    <b>-rm </b>= <u>remove</u> (apenas os contêiners)
    obs -><b> -rmi </b>= <u>remove as imagens</u>
    obs -><b> -rm -v </b>= <u>remove contêiner _ volume associado</u>
&nbsp;
    <span style="color:rgb(245, 57, 104); background-color: #d8e2dc;">docker rm distracted_merkle beautiful_franklin mystifying_meninsky</span> 
&nbsp;
    Criando contêiner com nome "personalisado
&nbsp;
    <span style="color:rgb(245, 57, 104); background-color: #d8e2dc;">docker run -e MYSQL_ROOT_PASSWORD=ro0t --name testeMySQL -d mysql:8.0</span>
&nbsp;
    --name = nome que quero dar para o contêiner
    -d = detached/desanexdo/segudo plano - para não travar o terminal 
&nbsp;
    retorno :
    db8...91...58ecf32...fef89
    este n° enorme se chama <b>hash</b> = <i> id do contêiner, indentificados único</i>
    São 64 caracteres hexadecimal(0-9, a-f), mas o docker usa apenas os 12 primeiros ex c3f279d17e0a (não é o atual)
&nbsp;
    Para ver se está rodando e criado <span style="color:rgb(245, 57, 104);">docker ps</span>
    resposta: mostrar informações do id, image ..... names
&nbsp;
    <span style="color: #f5cac3; background: #1b4965;">Testar acesso do servidor</span>
&nbsp;
    <span style="color:rgb(245, 57, 104); background-color: #d8e2dc;">docker inspect testeMySQL</span>
&nbsp;
    Este comando retorna, no formato json, informações detalhadas do container, imagem (camadas, tamanho, autor), volume, redes (ip, portas mapeadas, DNS), estado (atual, em execução), recurso (limite do cpu/memóia), log (configuração do drive log) ...
    São listas [] com diconários {}
&nbsp;
    no caso quer apenas ip address, então
&nbsp;
        <span style="color:rgb(245, 57, 104); background-color: #d8e2dc;">docker inspect testeMySQL | grep IPAddress</span>
&nbsp;
    pipe (|) = redireciona/"canal" para a saída no 1° comando para o próximo comando (grep)
    grep encontra todas as ocorrências do ntermo que se deseja (no caso Ip address), é um filtro
&nbsp;
    retorno:
                "SecondaryIPAddresses": null,
            "IPAddress": "172.17.0.2",
                    "IPAddress": "172.17.0.2",

&nbsp;
-----------------------------------------------------------------------
-----------------------------------------------------------------------
-----------------------------------------------------------------------
resumindo - apenas isso
    <span style="color: #faedcd; background-color:rgb(55, 70, 7);">docker run -e MYSQL_ROOT_PASSWORD=ro0t --name testeMySQL -d mysql:8.0</span>
para ver see stá rdando
    <span style="color: #faedcd; background-color: rgb(55, 70, 7);">docker ps</span>

-----------------------------------------------------------------------
-----------------------------------------------------------------------

como ver infromações do contêiner (porta é uma delas)
&nbsp;
<span style="color: #caf0f8; background-color: #023e8a;">docker exec -it testeMySQL mysql -u root -p</span>
&nbsp;
- exec = executar
- -it = junção de flag = dentro do contêiner/ com o terminal do contêiner
- testeMysql - nome do contêiner que  o conando será executado
- mysql - comando executado (vou executar o mysql)
- -u = usuário
- root = nome do usuário (ver como mudar)
- -p = password = deverá inserir uma senha (criada nos comandos anteriores)
&nbsp;

&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;
&nbsp;