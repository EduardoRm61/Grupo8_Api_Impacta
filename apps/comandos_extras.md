-------------------------------------------------------------------------------------------------------
|                                                                                                     |
|                           erro na porta do local para remoto                                        |
|                                                                                                     |
-------------------------------------------------------------------------------------------------------
antes deve Executar o script de entrada da aplicação/ run the application entry script/ Subir a aplicação 
tudo isso é rodar 
                                        python app.py (no caso python apps/app.py)


não fecha, abra outro terminal, pode ser powershell e rode o cód

                                                 netstat -ano | findstr :5002

netstat -> Ferramenta do Windows que mostra estatísticas de rede e conexões ativas

-a -> Mostra todas as conexões e portas em escuta (LISTENING)
Listening/ escutando = estado de um processo que está ativamente aguardando conexões de entrada em uma porta específica
Flask roda app.run(), ele coloca o servidor no estado LISTENING na porta configurada (ex: 5002)

-n -> Exibe números de portas e endereços IP em formato numérico (ao invés de tentar resolver nomes)

-o -> Mostra o ID do processo (PID) associado a cada conexão

| (pipe) -> Redireciona a saída do netstat para o próximo comando (findstr)

findstr :5002 -> Filtra apenas as linhas que contêm :5002 (sua porta do Flask)

retorno:
                      TCP    127.0.0.1:5002         0.0.0.0:0              LISTENING       10088

TCP = protocolo de rede usado/ Transmission Control Procol  
o flask está usando tcp para conexões http/web
obs - UDP = conexões sem estados

127.0.0.1 = ip do localhost (conexões da própria máquina)
# se quiser acessar de outra máquina ou docker deve mudar para 0.0.0.0 (endereço remoto)
ficando 0.0.0.0:5002

:5002 = porta onde o flask "ouve"
