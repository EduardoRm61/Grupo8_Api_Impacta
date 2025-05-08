# Avisos encontrados

### Alunos

- deletar lista
- linhas 3 e 4 - import dando erro, deixei co from
- linha 17 - Foreignkey ("Id") - acho que não precisa, se precisar volto e comento na póxima linha

    Ao usar forengkey - como se criou um "objeto de mapeamento" - ao chamar, deve ser pelo nome da tabela

- linhas 63 - turma letra minúscula

- mostra linhas amarela nas linhas 133, 139, 143, 146, 154, 161, com dados - vou por Aluno - referenciando class Aluno

### Turma

- file que estava era mais anitgo que da branch testes
- copiei aqui o file de_turma
- linhas 1 a 3 imposts estavam dadno erro de caminho
- linha 184 estava professorexistente(def) - linha amarela - coloquei ProfessorExiste(class), linhas saiu

### Git

- erro ao copiar arquivo model_turma.py da branch testes

error: pathspec 'model_turma.py' did not match any file(s) known to git

<span style="color: blue;">git ls-tree -r testes --name-only | grep model_turma.py</span> vê se tem o arquivo e dá o caminho inteiro

retorno : apps/turma/model_turma.py

<span style="color: blue,"> git checkout testes -- apps/turma/model_turma.py </span> copia arquivo/s específicos de outras branchs

retorno  : "interno" - atualiza o file, ou copia, sem retorno escrito

<span style="color: green;">git diff --staged</span> verificação de mudanças adiconadas no staged (pós add )

<span style="color: green;">git diff --staged caminho/do/arquivo</span> verificação de mudanças adiconadas no staged (pós add ) file específico

<span style="color: green;">git diff --staged caminho/do/arquivo</span> verificação de mudanças não adiconadas no staged (pré add ) 

### app.py

- linas 14 - bp comentada, tirei comentário | arrumei /Truma, estava aluno

- linhas 15 - recoloquei bp aluno 

### Professor

- linhas -4 - upload __tablename__ = "professores" = tipo objeto que rastrei esta classe/ tabelas 

-  professor = Professor.query.get(id_professor) - ele referencia a chave primária pk da tabela

chama quando for pegar algo específico, no nosso caso, por id

ex : saber nome do professor, deletar por id, get porfessor por id, etc -

-linhas - 57,65,106, 133