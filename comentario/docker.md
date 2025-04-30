## <center> Docker</center>

<span style="color: #4a4e69; background-color:rgb(219, 202, 216);"> ls</span> no bash ou <span style="color: #4a4e69; background-color:rgb(219, 202, 216);"> dir</span> no powershell lista os files da pasta e os folders

<span style="color: #4a4e69; background-color:rgb(219, 202, 216);"> docker build -t teste-render . </span> cria a imagem. O (.) indica que o Dockerfile está na pasta atual/raiz (acho que raiz está certo). -t é tag para atribuir um nome, neste caso

<span style="color: #4a4e69; background-color:rgb(219, 202, 216);"> docker images</span> verifica se a imagem foi criada

<span style="color: #4a4e69; background-color:rgb(219, 202, 216);"> docker run -it teste-render</span> executa a imagem

retorno

ModuleNotFoundError: No module named 'flask_restx' - não instalei no docker