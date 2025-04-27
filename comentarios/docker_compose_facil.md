### <center>Docker-compose é fácil </center>

<center>Fernanda Kipper | dev</center>

&nbsp;
Definir o url_prefix na Blueprint (bp)
&nbsp;
Prefixo em flask/ web em geral = parte inicial fixada de uma url
Junta as rotas em um mesmo caminho
ex: prefixo = /professores - agora todas as rotas serão acessível sob este domínio /professores/add ou /professores/delete
&nbsp;
<b><center>Service:</center></b>
&nbsp;
Contêiners a serem executados, mapeados
&nbsp;
a - dar um nome para ele (sequirei exemplo do vídeo) =<span style="color:rgb(145, 3, 201);"> nginx:</span>
&nbsp;
declara como utilizar imagem - ex vem do docker, deploy etc
<span style="color:rgb(145, 3, 201);"> image: nginx:latest</span>
lembrar que latest sempre irá atualizar as versões do que estará "rodando"
&nbsp;
mapear as portas, volumes, depends_on (acho que é dependência)
<span style="color:rgb(145, 3, 201);"> ports:
-"80:80"
aqui seria a parte que se coloca -p 5002:5002
volumes:
-./nginx.conf:/etc/nginx/ninx.conf
não usarei - volume de disco - deletar
depends_on:
-app</span>
coloca contêiner dependente do outro
Sobe primeiro o contêiner base e depois seus dependentes
(ela tirou porque falou que não tem front, mas pesquisarei como se faz em outro lugar)
<span style="color:rgb(145, 3, 201);"> restart:aways
</span> sempre restartar quando inicializar docker compose
&nbsp;
<center> no terminal </center>
&nbsp;
<span style="color: rgb(145,3,201);">docker-compose up -d</span>

up = acho que seria equivalente a push, enviar, mandar
-d = detectme - detached mode = desanexado/desacoplado/ segundo plano/ não trava terminal/roda backgroud = MODO DESACOPLADO
&nbsp;
Ao rodar ele fará, como se fosse um pull, da/s imagem/ns 
resposta deverá ser algo com Created e Started
&nbsp;
<span style="color: rgb(145,3,201);">docker ps</span>
para listar contêiners rodando
ps = lista processo de sistemas, no caso o contêiner =  dá como respostas positivo, neste caso id contêiner, nome da imagem/versão, command, created, status, ports, names
&nbsp;
<span style="color: rgb(145,3,201);">network:
-"public_network"</span>
Eles acessam um ao outro atravéz da direta do nome do service
como criar:
networks:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  private_network: (ou o nome que desejar)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  briver: bridge (exemplo o banco de dados)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;public_network: (ou o nome que desejar)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; driver: bridge (exemplo o banco de dados)
