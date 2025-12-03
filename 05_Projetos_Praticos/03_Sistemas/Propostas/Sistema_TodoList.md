# Sistema de Lista de Tarefas (To-Do List)

## Descrição do Sistema

Desenvolver um sistema para gerenciar tarefas pessoais, permitindo adicionar, listar, marcar como concluída e remover tarefas. O sistema deve facilitar a organização das atividades diárias e acompanhamento de progresso.

## Requisitos Funcionais

### Vetores/Listas de Cadastro

1. **descricoes_tarefas[]** - Armazena descrições das tarefas
2. **status_tarefas[]** - Armazena status (True=concluída, False=pendente)
3. **datas_criacao[]** - Armazena datas de criação (opcional)

> **Nota:** Os vetores trabalham com índices sincronizados

### Operações CRUD Obrigatórias

#### 1. CREATE (Adicionar Tarefa)

- Cadastrar novas tarefas na lista
- Campo obrigatório: descrição da tarefa
- Adicionar simultaneamente nos vetores correspondentes
- Inicializar com status False (pendente)
- Validação: descrição não pode estar vazia
- Adicionar timestamp de criação (se implementado)
- Manter sincronização dos índices

#### 2. READ (Listar Tarefas)

- Exibir todas as tarefas cadastradas
- Mostrar status de cada tarefa (pendente/concluída)
- Numeração sequencial para identificação
- Separar visualmente tarefas concluídas das pendentes
- Exibir contadores de tarefas por status

#### 3. UPDATE (Marcar como Concluída)

- Alterar status_tarefas[índice] de False para True (marcar como concluída)
- Permitir "desmarcar": alterar status_tarefas[índice] de True para False
- Validar existência da tarefa (verificar índice válido)
- Atualizar contadores automaticamente
- Permitir edição de descricoes_tarefas[índice] se necessário

#### 4. DELETE (Remover Tarefa)

- Remover tarefas da lista
- Excluir dos vetores sincronizados (descrição, status, data se houver)
- Permitir remoção de tarefas pendentes e concluídas
- Confirmar operação antes de excluir
- Mostrar descrição da tarefa antes de remover
- Reorganizar índices após remoção

### Funcionalidades Específicas

#### Sistema de Menu

- Menu principal com todas as opções
- Interface numerada e intuitiva
- Navegação clara entre funcionalidades
- Opção de sair do sistema

#### Controle de Status

- Identificar tarefas pendentes e concluídas
- Símbolos visuais para diferentes status
- Contadores de produtividade
- Relatório de progresso

#### Organização de Tarefas

- Listar apenas tarefas pendentes
- Listar apenas tarefas concluídas
- Visualização completa com separação clara
- Estatísticas de conclusão

#### Produtividade

- Contar tarefas pendentes vs concluídas
- Calcular percentual de conclusão
- Mostrar progresso geral
- Motivar usuário com estatísticas

### Validações Necessárias

- Descrição da tarefa não pode estar vazia
- Verificar existência da tarefa antes de operações
- Validar índices de seleção
- Confirmar operações de exclusão
- Tratar entrada de dados inválidos

### Interface do Usuário

- Menu claro e organizado
- Símbolos para status (✓ concluída, ○ pendente)
- Mensagens motivacionais
- Contadores visuais de progresso
- Tratamento de erros amigável
