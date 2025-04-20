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