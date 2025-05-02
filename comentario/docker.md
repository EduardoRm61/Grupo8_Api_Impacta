## <center>🚛 Docker 📦</center>

### 1° coisa, abrir ambiente dockerdesktop e verificar se está rodando

retono caso não esteja

<u><b>ERROR: error during connect:</b></u> Head "http://%2F%2F.%2Fpipe%2FdockerDesktopLinuxEngine/_ping": open //./pipe/dockerDesktopLinuxEngine: The system cannot find the file specified.
&nbsp;

<i><u><b>SEMPRE QUE TIVER ALGUMA MODIFICAÇÃO NO PROJETO,, DEVE-SE CRIAR UMA NOVA IMAGEM DOCKER </b></u></i> cada run é como se estivesse instanciando um objeto. Traduzi assim, é uma imagem, se eu tirar um chapéu terei de tirar nova fota para ser usada
&nbsp;

<span style="color: #4a4e69; background-color:rgb(219, 202, 216);"> ls</span> no bash ou <span style="color: #4a4e69; background-color:rgb(219, 202, 216);"> dir</span> no powershell lista os files da pasta e os folders

<span style="color: #4a4e69; background-color:rgb(219, 202, 216);"> docker build -t teste-render . </span> cria a imagem. O (.) indica que o Dockerfile está na pasta atual/raiz (acho que raiz está certo). -t é tag para atribuir um nome, neste caso

<span style="color: #4a4e69; background-color:rgb(219, 202, 216);"> docker images</span> verifica se a imagem foi criada

<span style="color: #4a4e69; background-color:rgb(219, 202, 216);"> docker run -p 5002:5002-it teste-render</span> executa a imagem

retorno

ModuleNotFoundError: No module named 'flask_restx' - não instalei no docker


Deu problema no py, tive que desinstalar e dava erro

https://support.microsoft.com/pt-br/topic/corrigir-problemas-que-bloqueiam-a-instala%C3%A7%C3%A3o-ou-remo%C3%A7%C3%A3o-de-programas-cca7d1b6-65a9-3d98-426b-e9f927e1eb4d

baixei o app e rodei

coisa linda!

forçou desistalação