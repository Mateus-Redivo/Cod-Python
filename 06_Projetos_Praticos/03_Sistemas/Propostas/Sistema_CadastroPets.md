# Sistema de Cadastro de Pets

## Descrição do Sistema

Desenvolver um sistema para gerenciar informações de animais de estimação, incluindo dados básicos dos pets e controle de vacinação. O sistema deve permitir o acompanhamento da saúde e histórico vacinal dos animais cadastrados.

## Requisitos Funcionais

### Vetores/Listas de Cadastro

1. **nomes_pets[]** - Armazena nomes dos pets
2. **especies[]** - Armazena espécies dos pets
3. **idades[]** - Armazena idades dos pets

> **Nota:** Os vetores trabalham com índices sincronizados

### Operações CRUD Obrigatórias

#### 1. CREATE (Cadastrar Pet)

- Cadastrar novos pets no sistema
- Campo obrigatório: nome
- Campos opcionais: espécie (padrão: "Não informado"), idade
- Adicionar simultaneamente nos quatro vetores
- Validação: nome não pode estar vazio, idade deve ser positiva
- Manter sincronização dos índices

#### 2. READ (Listar Pets)

- Exibir todos os pets cadastrados
- Mostrar informações básicas: nome, espécie, idade
- Exibir quantidade de vacinas aplicadas
- Numeração sequencial para identificação
- Tratar caso de lista vazia

#### 3. UPDATE (Vacinar Pet/Editar Informações)

- **Alterar Pet**: alterar informações do pet
- Permitir alteração de nome, espécie e idade
- Localizar pet por nome ou índice
- Atualizar vetores correspondentes
- Manter consistência entre os quatro vetores

#### 4. DELETE (Remover Pet)

- Remover pets do sistema
- Excluir dos quatro vetores simultaneamente (nome, espécie, idade)
- Confirmar operação antes de excluir
- Mostrar informações do pet antes da exclusão
- Reorganizar índices após remoção

### Funcionalidades Específicas

#### Sistema de Menu

- Menu principal com todas as opções
- Interface amigável com numeração
- Opção de sair do sistema
- Tratamento de opções inválidas

#### Busca e Consulta

- Buscar pet por nome
- Ver detalhes completos de um pet específico
- Listar pets por espécie

### Validações Necessárias

- Nome do pet é obrigatório
- Idade deve ser um número positivo
- Verificar existência do pet antes das operações
- Validar índices de seleção

### Interface do Usuário

- Menu claro e organizado
- Mensagens de confirmação para operações
- Tratamento de erros com mensagens amigáveis
- Formatação visual consistente
- Exibição organizada das informações dos pets
