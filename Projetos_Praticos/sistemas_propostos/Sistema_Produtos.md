# Sistema de Controle de Produtos (Mercado)

## Descrição do Sistema
Desenvolver um sistema para controle de estoque de um mercado/loja, gerenciando produtos, preços, quantidades e movimentações de entrada e saída. O sistema deve facilitar o controle de inventário e operações comerciais.

## Requisitos Funcionais

### Vetores/Listas de Cadastro (Mínimo 2)
1. **nomes[]** - Lista para armazenar nomes dos produtos
2. **precos[]** - Lista para armazenar preços dos produtos
3. **quantidades[]** - Lista para armazenar quantidades em estoque

*Nota: Os três vetores trabalham com índices sincronizados*

### Operações CRUD Obrigatórias

#### 1. CREATE (Cadastrar Produto)
- Cadastrar novos produtos no sistema
- Campos obrigatórios: nome, preço, quantidade inicial
- Validações: preço e quantidade devem ser positivos
- Adicionar simultaneamente nas três listas
- Manter sincronização dos índices

#### 2. READ (Listar Produtos)
- Exibir todos os produtos cadastrados
- Mostrar nome, preço e quantidade disponível
- Numeração sequencial para identificação
- Formatação de preços em moeda (R$)
- Identificar produtos com estoque baixo

#### 3. UPDATE (Atualizar Produto/Estoque)
- **Atualizar Produto**: modificar nome, preço ou quantidade
- **Entrada de Estoque**: adicionar quantidades ao estoque
- **Saída de Estoque**: reduzir quantidades (vendas)
- Manter consistência entre as três listas
- Validar alterações antes de aplicar

#### 4. DELETE (Remover Produto)
- Remover produto do sistema
- Excluir das três listas simultaneamente
- Confirmar operação antes de excluir
- Reorganizar índices após remoção

### Funcionalidades Específicas

#### Sistema de Menu
- Menu principal com todas as opções
- Interface numerada e organizada
- Navegação intuitiva entre funcionalidades
- Opção de sair do sistema

#### Controle de Estoque
- Movimentações de entrada (reposição)
- Movimentações de saída (vendas)
- Verificar disponibilidade antes das saídas
- Alertas para estoque baixo ou zerado

#### Relatórios do Inventário
- Balanço completo do inventário
- Valor total em estoque
- Produtos em falta
- Produtos com estoque crítico

#### Sistema de Testes
- Função para popular produtos de exemplo
- Facilitar testes do sistema
- Produtos variados para demonstração

### Validações Necessárias
- Nome do produto não pode estar vazio
- Preço deve ser positivo
- Quantidade deve ser inteira e positiva
- Verificar se produto existe antes de operações
- Não permitir saída maior que estoque disponível
- Manter sincronização entre listas

### Interface do Usuário
- Menu claro e organizado
- Formatação adequada de valores monetários
- Mensagens de confirmação para operações
- Tratamento de erros com orientações
- Listagem organizada e numerada

