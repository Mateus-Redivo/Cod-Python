# Sistema de Playlist Musical

## Descrição do Sistema
Desenvolver um sistema para gerenciar uma coleção de músicas, permitindo organizar playlists, buscar por gêneros, simular reprodução e controlar uma biblioteca musical pessoal.

## Requisitos Funcionais

### Vetores/Listas de Cadastro (Mínimo 2)
1. **titulos[]** - Vetor para armazenar títulos das músicas
2. **artistas[]** - Vetor para armazenar artistas das músicas
3. **generos[]** - Vetor para armazenar gêneros musicais
4. **duracoes[]** - Vetor para armazenar durações em segundos

*Nota: Os quatro vetores trabalham com índices sincronizados*

### Operações CRUD Obrigatórias

#### 1. CREATE (Adicionar Música)
- Cadastrar novas músicas na playlist
- Campos obrigatórios: título, artista
- Campos opcionais: gênero (padrão: "Não informado"), duração
- Adicionar simultaneamente nos quatro vetores
- Validação: duração deve ser positiva (em segundos)
- Não permitir músicas duplicadas (mesmo título e artista)
- Manter sincronização dos índices

#### 2. READ (Listar/Buscar Músicas)
- Listar todas as músicas da playlist
- Buscar músicas por gênero específico
- Exibir informações completas: título, artista, gênero, duração
- Formatar duração em minutos e segundos
- Contar total de músicas na playlist

#### 3. UPDATE (Editar Informações da Música)
- Alterar informações de músicas existentes
- Permitir edição de: titulos[índice], artistas[índice], generos[índice], duracoes[índice]
- Localizar música por índice ou busca
- Manter consistência dos dados nos vetores
- Validar novas informações antes da alteração

#### 4. DELETE (Remover Música)
- Remover músicas da playlist
- Excluir dos quatro vetores simultaneamente (título, artista, gênero, duração)
- Confirmar operação antes de excluir
- Mostrar detalhes da música antes de remover
- Reorganizar índices após remoção

### Funcionalidades Específicas

#### Sistema de Menu
- Menu principal com todas as opções
- Interface numerada e intuitiva
- Navegação clara entre funcionalidades
- Opção de sair do sistema

#### Sistema de Reprodução (Simulado)
- Simular "reprodução" de músicas
- Selecionar música por índice
- Exibir informações durante "reprodução"
- Registrar no histórico (se implementado)
- Mostrar progresso ou tempo de duração

#### Busca e Filtros
- Buscar por gênero musical
- Listar músicas de artista específico
- Filtrar por duração
- Busca por título parcial

#### Controle de Biblioteca
- Estatísticas da playlist (total de músicas, duração total)
- Gêneros disponíveis na coleção
- Artistas únicos na playlist
- Música mais longa/mais curta

### Validações Necessárias
- Título e artista são obrigatórios
- Duração deve ser positiva (se informada)
- Verificar duplicação antes do cadastro
- Validar índice de seleção de músicas
- Tratar entradas vazias ou inválidas

### Interface do Usuário
- Menu organizado e claro
- Formatação adequada da duração (MM:SS)
- Mensagens informativas sobre operações
- Listagem numerada para seleção
- Tratamento de erros amigável

