# Sistema de Biblioteca

## Descrição do Sistema
Desenvolver um sistema para gerenciar uma biblioteca simples, permitindo o controle de livros e suas operações básicas como empréstimo e devolução. O sistema deve manter registro dos livros disponíveis e emprestados.

## Requisitos Funcionais

### Vetores/Listas de Cadastro (Mínimo 2)
1. **titulos[]** - Vetor para armazenar títulos dos livros
2. **autores[]** - Vetor para armazenar autores dos livros
3. **disponibilidade[]** - Vetor para controlar se o livro está disponível (True/False)

*Nota: Os três vetores trabalham com índices sincronizados*

### Operações CRUD Obrigatórias

#### 1. CREATE (Adicionar Livro)
- Cadastrar novos livros na biblioteca
- Campos obrigatórios: título, autor
- Adicionar simultaneamente nos três vetores
- Inicializar disponibilidade como True (disponível)
- Validação: título e autor não podem estar vazios
- Manter sincronização dos índices

#### 2. READ (Listar Livros)
- Exibir todos os livros cadastrados
- Mostrar status (Disponível/Emprestado)
- Numeração sequencial para identificação
- Tratar caso de lista vazia

#### 3. UPDATE (Emprestar/Devolver Livro)
- **Emprestar livro**: alterar disponibilidade[índice] de True para False
- **Devolver livro**: alterar disponibilidade[índice] de False para True
- Validar se o livro existe (verificar índice válido)
- Verificar status atual antes de permitir a operação
- Manter consistência entre os vetores

#### 4. DELETE (Remover Livro)
- Remover livros do sistema
- Excluir dos três vetores simultaneamente (título, autor, disponibilidade)
- Confirmar operação antes de excluir
- Não permitir exclusão de livros emprestados (disponibilidade = False)
- Reorganizar índices após remoção

### Funcionalidades Específicas

#### Sistema de Menu
- Menu principal com todas as opções
- Interface amigável com numeração
- Opção de sair do sistema
- Tratamento de opções inválidas

#### Controle de Empréstimos
- Verificar disponibilidade antes do empréstimo
- Impedir empréstimo duplo do mesmo livro
- Permitir devolução apenas de livros emprestados
- Exibir mensagens informativas sobre as operações

### Validações Necessárias
- Campos obrigatórios não podem estar vazios
- Verificar existência do livro antes das operações
- Validar índices de seleção de livros
- Confirmar operações importantes

### Interface do Usuário
- Menu claro e organizado
- Mensagens de confirmação para operações
- Tratamento de erros com mensagens amigáveis
- Formatação visual consistente