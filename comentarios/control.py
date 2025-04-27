# blueprint - separa rotas em vários locais 
# tira da responsabiliade dos app a inicialização das rotas
# app não pode ser separado, ex, tem de ter um app apenas - uma aplicação diferentes, uma api | como há mais de uma entidade, cada uma deveria ter um app, e aí, se separasse, e criasse um app para cada, seeriam 32 instâncias, 3 apis, e isso não pode acontecer pois queremos apenas uma
# para resolver - cria-se os blue prints para ser entrada das rotas
# agrupa rotas e viws
# tem módulos independentes - desacopla das aplicações as rotas e as torna independentes (tira do app) | pode usar em várias aplicações diferentes
# manutenção de cód, se torna fácil de achar e atualizar partes específicas
# teremos que fazer uma instãncia (classe - objeto) - cria rota - valida - registra no aplicativo (acho que app)

#ver como fica aqui