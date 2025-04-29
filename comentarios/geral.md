Pytest = framework (conjunto de códigos que usam ferramentas, diretrizes e práticas para construir aplicações) para facilitar testes simples e escaláveis de:

- endpoint = rotas e seus estados e dados

- comportamento = respostas de diferentes inputs

- garante que novas alterações não quebrem

- facilita ci/cd = ci - integração contínua, cd - entrega/ implementação contínua = juntas automatizam o processo

<center>pytest</center>
roda todos os testes

<center>pytest --cov=app</center>
roda todos os testes com abertura de cód

<center>pytest tests/test_routes.py::test_get_produtos</center>
roda teste específico