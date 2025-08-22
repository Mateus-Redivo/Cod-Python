# Sistema de Controle de Notas de Alunos

## Descrição do Sistema
Desenvolver um sistema para controlar as notas dos alunos, gerenciando informações acadêmicas e calculando médias. O sistema deve facilitar o acompanhamento do desempenho escolar, organizando notas de diferentes disciplinas.

## Requisitos Funcionais

### Vetores/Listas de Cadastro (Mínimo 2)
1. **Alunos[]** - Vetor para armazenar nomes dos alunos
2. **Notas[]** - Vetor de listas para armazenar múltiplas notas de cada aluno

*Nota: Os dois vetores trabalham com índices sincronizados, onde notas[i] é uma lista das notas do aluno[i]*

### Operações CRUD Obrigatórias

#### 1. CREATE (Cadastrar Aluno/Adicionar Nota)
- Cadastrar novos alunos no sistema
- Adicionar novas notas para alunos já cadastrados
- Campos obrigatórios: nome do aluno, nota
- Se aluno não existe: criar novo registro com lista de notas
- Se aluno existe: adicionar nova nota à sua lista
- Validação: não permitir nomes vazios
- Manter sincronização dos índices

#### 2. READ (Listar Alunos e Notas)
- Exibir lista de alunos cadastrados
- Mostrar para cada aluno: nome, todas as notas e média individual
- Exibir estatísticas gerais (maior nota, menor nota, média da turma)
- Listar alunos aprovados e reprovados com base na média

#### 3. UPDATE (Alterar Nota)
- Permitir alteração de notas específicas do aluno
- Localizar aluno por nome ou índice
- Exibir todas as notas do aluno e permitir escolha da nota a alterar
- Atualizar nota específica na lista de notas do aluno
- Manter consistência entre os dois vetores

#### 4. DELETE (Remover Aluno/Nota)
- Remover aluno completamente do sistema
- Ou remover nota específica de um aluno
- Para remoção de aluno: excluir dos dois vetores simultaneamente
- Para remoção de nota: remover da lista de notas do aluno
- Confirmar operação antes de excluir
- Reorganizar índices após remoção

### Funcionalidades Específicas

#### Sistema de Menu
- Menu principal com todas as opções
- Interface amigável e intuitiva
- Opção de sair do sistema

#### Controle de Notas
- Cada índice representa um aluno e sua lista de notas
- Formato de exibição: "Nome: [Nota1, Nota2, ...] - Média: X.X"
- Permitir múltiplas notas por aluno
- Calcular média individual automaticamente
- Garantir que cada aluno tenha pelo menos uma nota

#### Relatórios Acadêmicos
- Lista completa de alunos com todas as notas
- Média individual de cada aluno
- Estatísticas gerais (maior nota, menor nota, média da turma)
- Lista de alunos aprovados (média >= 6.0)
- Lista de alunos reprovados (média < 6.0)
- Relatório de desempenho por disciplina/avaliação

### Validações Necessárias
- Nome do aluno não pode estar vazio
- Nota deve estar entre 0.0 e 10.0
- Aluno deve ter pelo menos uma nota para cálculo de média
- Verificar existência do aluno antes de operações de alteração/remoção
- Validar índice da nota ao alterar/remover notas específicas

### Interface do Usuário
- Menu claro e organizado
- Mensagens de boas-vindas para novos alunos
- Confirmações de cadastro
- Tratamento de erros amigável

