# Sistema de Loja de Doces

## Descrição do Sistema
Desenvolver um sistema para gerenciar uma loja de doces, controlando produtos, estoque, vendas e reposição. O sistema deve facilitar a operação comercial com controle de inventário e registro de vendas.

## Requisitos Funcionais

### Vetores/Listas de Cadastro (Mínimo 2)
1. **nomes_produtos[]** - Vetor para armazenar nomes dos produtos
2. **precos[]** - Vetor para armazenar preços dos produtos
3. **estoques[]** - Vetor para armazenar quantidades em estoque
4. **vendas_produto[]** - Vetor para registrar total de vendas por produto (opcional)

*Nota: Os quatro vetores trabalham com índices sincronizados*

### Operações CRUD Obrigatórias

#### 1. CREATE (Cadastrar Produto)
- Cadastrar novos produtos na loja
- Campos obrigatórios: nome, preço, quantidade em estoque
- Adicionar simultaneamente nos três vetores principais
- Validação: preço e estoque devem ser positivos
- Não permitir produtos duplicados (mesmo nome)
- Inicializar com estoque informado
- Manter sincronização dos índices

#### 2. READ (Listar Produtos)
- Exibir todos os produtos cadastrados
- Mostrar nome, preço e quantidade em estoque
- Identificar produtos em falta (estoque = 0)
- Numeração sequencial para identificação
- Formatação de preços em moeda

#### 3. UPDATE (Repor Estoque / Fazer Venda)
- **Repor Estoque**: somar quantidades ao estoques[índice]
- **Fazer Venda**: subtrair quantidade vendida do estoques[índice]
- **Alterar preço**: modificar precos[índice]
- Validar disponibilidade antes da venda
- Calcular valor total da venda (quantidade × precos[índice])
- Atualizar estoque automaticamente após venda

#### 4. DELETE (Remover Produto)
- Remover produtos do catálogo
- Excluir dos três vetores simultaneamente (nome, preço, estoque)
- Confirmar operação antes de excluir
- Verificar se há estoque antes de remover (opcional: permitir remoção com aviso)
- Reorganizar índices após remoção

### Funcionalidades Específicas

#### Sistema de Menu
- Menu principal com todas as opções
- Interface numerada e organizada
- Navegação intuitiva
- Opção de sair do sistema

#### Controle de Estoque
- Verificar disponibilidade antes de vendas
- Alertas para produtos em falta
- Controle de quantidades mínimas
- Reposição de estoque com validação

#### Sistema de Vendas
- Calcular valor total da venda
- Verificar quantidade disponível
- Atualizar estoque automaticamente
- Não permitir venda de quantidade maior que estoque

#### Relatórios da Loja
- Lista de produtos disponíveis
- Produtos em falta (estoque zero)
- Histórico de vendas
- Valor total de vendas realizadas

### Validações Necessárias
- Nome do produto não pode estar vazio
- Preço deve ser positivo
- Estoque deve ser número inteiro positivo
- Quantidade de venda não pode exceder estoque
- Verificar existência do produto antes de operações
- Validar entrada de dados numéricos

### Interface do Usuário
- Menu claro e organizado
- Mensagens de confirmação para vendas
- Alertas para estoque baixo
- Formatação de valores monetários
- Tratamento de erros amigável

