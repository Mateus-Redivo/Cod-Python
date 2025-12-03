# Sistema de Organização de Churrasco

## Descrição do Sistema

Desenvolver um sistema para organizar churrascos, gerenciando participantes e controlando os itens que cada pessoa irá trazer. O sistema deve facilitar a coordenação do evento, garantindo variedade de carnes e bebidas.

## Requisitos Funcionais

### Vetores/Listas de Cadastro

1. **participantes[]** - Armazena nomes dos participantes
2. **carnes[]** - Armazena tipos de carne que cada participante trará
3. **bebidas[]** - Armazena tipos de bebida que cada participante trará

> **Nota:** Os vetores trabalham com índices sincronizados

### Operações CRUD Obrigatórias

#### 1. CREATE (Cadastrar Participante)

- Cadastrar novos participantes do churrasco
- Campos obrigatórios: nome, tipo de carne, tipo de bebida
- Adicionar simultaneamente nos três vetores
- Cada participante deve trazer 1 carne e 1 bebida
- Validação: não permitir participantes duplicados
- Manter sincronização dos índices

#### 2. READ (Listar Participantes e Itens)

- Exibir lista de participantes cadastrados
- Mostrar para cada participante: nome, carne que trará, bebida que trará
- Listar todos os tipos de carne disponíveis
- Listar todas as bebidas disponíveis

#### 3. UPDATE (Alterar Contribuição)

- Permitir que participante altere tipo de carne (carnes[índice])
- Permitir que participante altere tipo de bebida (bebidas[índice])
- Localizar participante por nome ou índice
- Atualizar vetores correspondentes
- Manter consistência entre os três vetores

#### 4. DELETE (Remover Participante)

- Remover participante do churrasco
- Excluir dos três vetores simultaneamente (nome, carne, bebida)
- Confirmar operação antes de excluir
- Reorganizar índices após remoção

### Funcionalidades Específicas

#### Sistema de Menu

- Menu principal com todas as opções
- Interface amigável e intuitiva
- Opção de sair do sistema

#### Controle de Itens

- Cada índice representa um participante e suas contribuições
- Formato de exibição: "Nome: Carne + Bebida"
- Evitar duplicação de participantes
- Garantir que cada pessoa contribua com 2 itens

#### Relatórios do Churrasco

- Lista completa de participantes
- Inventário de carnes disponíveis
- Inventário de bebidas disponíveis
- Resumo total do evento

### Validações Necessárias

- Nome do participante não pode estar vazio
- Tipo de carne não pode estar vazio
- Tipo de bebida não pode estar vazio
- Não permitir participantes duplicados
- Verificar existência antes de operações de alteração/remoção

### Interface do Usuário

- Menu claro e organizado
- Mensagens de boas-vindas para novos participantes
- Confirmações de cadastro
- Tratamento de erros amigável
