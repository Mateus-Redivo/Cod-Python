# Sistema de Cadastro de Pets

## Descrição do Sistema
Desenvolver um sistema para gerenciar informações de animais de estimação, incluindo dados básicos dos pets e controle de vacinação. O sistema deve permitir o acompanhamento da saúde e histórico vacinal dos animais cadastrados.

## Requisitos Funcionais

### Vetores/Listas de Cadastro (Mínimo 2)
1. **nomes_pets[]** - Vetor para armazenar nomes dos pets
2. **especies[]** - Vetor para armazenar espécies dos pets
3. **idades[]** - Vetor para armazenar idades dos pets
4. **vacinas[]** - Vetor de listas, onde cada posição contém a lista de vacinas do pet correspondente

*Nota: Os quatro vetores trabalham com índices sincronizados*

### Operações CRUD Obrigatórias

#### 1. CREATE (Cadastrar Pet)
- Cadastrar novos pets no sistema
- Campo obrigatório: nome
- Campos opcionais: espécie (padrão: "Não informado"), idade
- Adicionar simultaneamente nos quatro vetores
- Inicializar lista vazia de vacinas para cada pet (vacinas[índice] = [])
- Validação: nome não pode estar vazio, idade deve ser positiva
- Manter sincronização dos índices

#### 2. READ (Listar Pets)
- Exibir todos os pets cadastrados
- Mostrar informações básicas: nome, espécie, idade
- Exibir quantidade de vacinas aplicadas
- Numeração sequencial para identificação
- Tratar caso de lista vazia

#### 3. UPDATE (Vacinar Pet/Editar Informações)
- **Aplicar vacinas**: adicionar vacina na lista vacinas[índice] do pet específico
- **Editar informações**: alterar nome, espécie ou idade em seus respectivos vetores
- Validar se o pet existe (verificar índice válido)
- Não permitir vacinas vazias ou duplicadas no mesmo pet
- Manter consistência entre todos os vetores

#### 4. DELETE (Remover Pet)
- Remover pets do sistema
- Excluir dos quatro vetores simultaneamente (nome, espécie, idade, vacinas)
- Confirmar operação antes de excluir
- Mostrar informações do pet antes da exclusão
- Reorganizar índices após remoção

### Funcionalidades Específicas

#### Sistema de Menu
- Menu principal com todas as opções
- Interface amigável com numeração
- Opção de sair do sistema
- Tratamento de opções inválidas

#### Controle de Vacinação
- Ver vacinas aplicadas em cada pet
- Histórico completo de vacinação
- Validar nome da vacina antes de aplicar
- Permitir múltiplas vacinas por pet

#### Busca e Consulta
- Buscar pet por nome
- Ver detalhes completos de um pet específico
- Listar pets por espécie
- Relatório de vacinação

### Validações Necessárias
- Nome do pet é obrigatório
- Idade deve ser um número positivo
- Nome da vacina não pode estar vazio
- Verificar existência do pet antes das operações
- Validar índices de seleção

### Interface do Usuário
- Menu claro e organizado
- Mensagens de confirmação para operações
- Tratamento de erros com mensagens amigáveis
- Formatação visual consistente
- Exibição organizada das informações dos pets

