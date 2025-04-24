docker run -d \
  --name MySQL \
  -e MYSQL_ROOT_PASSWORD=rt \
  -e MYSQL_DATABASE=impacta \          # 👈 Cria um banco inicial
  -e MYSQL_USER=app \                  # 👈 Usuário não-root (recomendado)
  -e MYSQL_PASSWORD=senha_segura \     # 👈 Senha do usuário
  -p 3306:3306 \                       # 👈 Expõe a porta para conexão externa
  -v mysql_data:/var/lib/mysql \       # 👈 Persistência de dados (volume Docker)
  --restart unless-stopped \           # 👈 Reinicia automaticamente se cair
  mysql:8.0 \
  --default-authentication-plugin=mysql_native_password  # 👈 Compatibilidade