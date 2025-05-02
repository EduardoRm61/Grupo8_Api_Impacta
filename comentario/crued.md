<b>SQLight é uma biblioteca padrão do .py - então não se cria um docker mas se conecta a ela</b>

Conexão

1° contêiner deve estar rodando (da api)

docker run -p 5002:500: -it grupo9 - rodar

docker info  - ver se está rodando

se sim retorno - lista enorme com ...
- version
-context
- debug mode
-pluging
- <b>server</b>
......

se não estiver, retorno

mensagem de erro

-------------------

para meu teste irei

github - ir no repositório origina (github Edu)

- clicar em fork

-nomear - ok

- code

- copie url

-clonar o projeto

git clone urel

cd nome-do-repositorio-original

git remote add upstream <URL-DO-REPOSITORIO-ORIGINAL>

Agora você pode criar branches, fazer alterações, commitar e fazer push para o seu fork no GitHub (origin geralmente se refere ao seu fork). Suas alterações aqui não afetarão o repositório original (upstream).

buscar atualização

git fetch upstream

Este comando baixa os branches e commits do repositório original para o seu repositório local, mas não os mescla com seus branches ainda.

Trazer as últimas atualizações do repositório original para o seu fork: Nesse caso, você usará os comandos 

git fetch upstream

 e 
 
 git merge upstream/<branch-principal-do-original>

Contribuir com suas alterações de volta para o repositório original: Se você fez algo útil no seu fork e quer que a outra pessoa incorpore essas mudanças no projeto principal, você criará um 

Pull Request

 a partir do seu fork para o branch desejado no repositório original. A outra pessoa então revisará suas mudanças e decidirá se as aceita e as mescla.