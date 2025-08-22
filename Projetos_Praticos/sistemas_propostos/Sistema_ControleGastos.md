# Sistema de Controle de Gastos

## Descrição do Sistema
Desenvolver um sistema para controle financeiro pessoal, permitindo o registro de receitas e despesas, com geração de relatórios e acompanhamento do saldo financeiro. O sistema deve ajudar na organização das finanças pessoais.

## Requisitos Funcionais

### Vetores/Listas de Cadastro (Mínimo 2)
1. **descricoes_receitas[]** - Vetor para armazenar descrições das receitas
2. **valores_receitas[]** - Vetor para armazenar valores das receitas
3. **descricoes_despesas[]** - Vetor para armazenar descrições das despesas  
4. **valores_despesas[]** - Vetor para armazenar valores das despesas

*Nota: Os quatro vetores trabalham com índices sincronizados*

### Operações CRUD Obrigatórias

#### 1. CREATE (Adicionar Receita/Despesa)
- **Adicionar Receita**: 
  - Campos: descrição, valor
  - Adicionar simultaneamente em descricoes_receitas[] e valores_receitas[]
  - Validação: valor deve ser positivo
- **Adicionar Despesa**: 
  - Campos: descrição, valor  
  - Adicionar simultaneamente em descricoes_despesas[] e valores_despesas[]
  - Validação: valor deve ser positivo
- Descrição não pode estar vazia
- Manter sincronização dos índices em cada par de vetores

#### 2. READ (Listar e Relatórios)
- Listar todas as receitas cadastradas
- Listar todas as despesas cadastradas
- Gerar relatório financeiro completo
- Mostrar saldo atual (receitas - despesas)
- Exibir totais de receitas e despesas

#### 3. UPDATE (Editar Receita/Despesa)
- **Editar receita**: alterar descrição ou valor nos vetores correspondentes
- **Editar despesa**: alterar descrição ou valor nos vetores correspondentes  
- Localizar item por índice
- Atualizar descricoes_receitas[índice] e/ou valores_receitas[índice]
- Atualizar descricoes_despesas[índice] e/ou valores_despesas[índice]
- Recalcular totais automaticamente

#### 4. DELETE (Remover Receita/Despesa)
- **Remover receita**: excluir dos vetores descricoes_receitas[] e valores_receitas[]
- **Remover despesa**: excluir dos vetores descricoes_despesas[] e valores_despesas[]
- Confirmar operação antes de excluir
- Reorganizar índices após remoção
- Atualizar saldo após remoção

### Funcionalidades Específicas

#### Sistema de Menu
- Menu principal com todas as opções
- Submenus para receitas e despesas
- Interface numerada e organizada
- Opção de sair do sistema

#### Controle Financeiro
- Cálculo automático do saldo (receitas - despesas)
- Total de receitas
- Total de despesas
- Identificação de situação financeira (positiva/negativa)

#### Relatórios Detalhados
- Relatório geral com todas as movimentações
- Resumo financeiro com totais
- Status do saldo (superávit/déficit)
- Listagem organizada por tipo

#### Validações Financeiras
- Valores devem ser positivos
- Descrições não podem estar vazias
- Formatação monetária adequada
- Verificação de existência antes de operações

### Validações Necessárias
- Descrição não pode estar vazia
- Valor deve ser número positivo
- Verificar existência do item antes de editar/remover
- Validar entrada numérica para valores
- Tratar erros de conversão de tipos

### Interface do Usuário
- Menu claro e organizado
- Mensagens de confirmação
- Formatação de valores em moeda (R$)
- Tratamento de erros amigável
- Cores ou símbolos para saldo positivo/negativo
