FROM python:3.11

# Definindo o diretório de trabalho no container
WORKDIR /app

# Copia o requirements.txt do diretório de cima (onde o docker-compose está) para dentro do container
COPY requirements.txt .  

# Instala as dependências
RUN pip install -r requirements.txt

# Copia todos os arquivos do diretório 'apps' para dentro do diretório de trabalho no container
COPY apps/ .  

# Expõe a porta que o Flask vai usar
EXPOSE 5002

# Comando para iniciar a aplicação
CMD ["python", "app.py"]  
