# Plano de Reestruturação — Repositório de Códigos Python

> Documento de trabalho. Descreve o padrão-alvo do repositório, os templates de cada tipo de
> arquivo e a ordem de execução da migração. É **autocontido**: tudo o que você precisa copiar
> está aqui dentro, não depende de consultar nenhum outro repositório.

---

## 1. Por que mexer

O conteúdo é bom. O problema é que ele foi escrito **arquivo a arquivo**, ao longo do tempo, e não
desenhado de cima para baixo. Os sintomas:

| Sintoma | Exemplo concreto hoje |
| --- | --- |
| Três estilos de escrita convivendo | `05_Condicionais/if_else.py` (banners + prints, com acento) × `04_Funcoes/01_introducao_funcoes.py` (narrativa em comentário, sem acento) × `03_Estruturas_De_Dados/01_Listas/manipulacao_vetores.py` (código puro) |
| Nomenclatura inconsistente | `tipos_basicos.py` × `01_while_loop.py` × `Comparacao_Strings.py` × `EX1.py` |
| Cobertura irregular de README | 12 pastas têm; `01_Tipos_E_Variaveis`, `03_Matrizes` e `04_Algoritmos_Ordenacao` não têm |
| Gabarito ao lado do exercício | `questoes_listas.py` e `respostas_quest_listas.py` na mesma pasta |
| Progressão invisível de dentro da pasta | nada em `04_Funcoes` diz "você precisa ter feito laços antes" |
| Entulho na raiz | `Test/` e `Nova pasta/` (vazia) |
| Sem fechamento de ciclo | não existe auto-avaliação, erros comuns nem critério de aceitação em lugar nenhum |

Nada disso é erro de conteúdo. É falta de **contrato**: uma forma única que todo módulo respeita.

---

## 2. O contrato do módulo

Toda pasta de módulo, sem exceção, tem esta forma:

```text
modulo-NN-nome-do-tema/
├── README.md              <- A AULA. Teoria em prosa, na voz de professor.
├── exemplos/              <- Códigos curtos, rodáveis, um conceito por arquivo.
│   ├── 01_conceito.py
│   └── 02_outro_conceito.py
└── exercicios/            <- Enunciados em .md. Nunca a resposta.
    ├── EXERCICIO-01-nome.md
    └── EXERCICIO-02-nome.md
```

E o `README.md` do módulo tem sempre as mesmas oito seções, nesta ordem:

1. **Título + frase-ponte** — liga ao módulo anterior em uma frase.
2. **Objetivos de aprendizagem** — lista de checkbox, começando com verbo ("Explicar…", "Escrever…").
3. **Pré-requisitos** — link explícito para o módulo anterior.
4. **Conceito** — o problema *antes* da solução. Sempre com código.
5. **Exemplos guiados** — o que cada arquivo de `exemplos/` mostra + como rodar.
6. **Exercícios** — links para os enunciados.
7. **Auto-avaliação** — checkbox que o aluno marca sozinho.
8. **Erros comuns** — tabela `Erro | O que está acontecendo`.
9. **Rodapé de navegação** — `Anterior | Próximo`.

> **Regra de ouro da migração:** a aula mora no README, não no `.py`.
> O arquivo `.py` deixa de ser apostila executável e vira **demonstração curta**: 30 a 60 linhas,
> um conceito só, com um docstring de cabeçalho. O aluno lê o README e roda o exemplo — não lê
> 140 linhas de `print` para chegar em 6 linhas de `if`.

---

## 3. A trilha alvo

```text
Codigos-Python/
├── README.md                      <- porta de entrada: trilha + tabela de módulos
├── GUIA-DO-ALUNO.md               <- instalar Python, rodar arquivo, fluxo de estudo
├── GLOSSARIO.md                   <- termos em linguagem simples
├── PLANO-REESTRUTURACAO.md        <- este arquivo (apagar quando a migração acabar)
│
├── modulo-00-preparacao/
├── modulo-01-tipos-e-variaveis/
├── modulo-02-operadores/
├── modulo-03-entrada-e-saida/
├── modulo-04-condicionais/
├── modulo-05-lacos-de-repeticao/
├── modulo-06-listas/
├── modulo-07-strings/
├── modulo-08-funcoes/
├── modulo-09-matrizes/
├── modulo-10-tratamento-de-erros/
├── modulo-11-algoritmos-de-ordenacao/
├── modulo-12-leitura-e-refatoracao/
├── modulo-13-estudo-de-caso-crud/
├── modulo-14-projeto-integrador/
│
├── gabaritos/                     <- TODAS as resoluções, longe dos enunciados
│   ├── README.md                  <- "use com responsabilidade"
│   ├── modulo-04-ex01-idade/
│   └── modulo-05-ex01-tabuada/
│
├── banco-de-exercicios/           <- prática extra, não ligada a um módulo
│   ├── nivel-1-iniciante/
│   ├── nivel-2-intermediario/
│   └── nivel-3-avancado/
│
├── projetos/                      <- jogos e calculadoras: desafios opcionais
│   ├── calculadoras/
│   └── jogos/
│
├── material-apoio/
│   ├── resumo-sintaxe.md          <- cola de sintaxe Python
│   ├── guia-de-comentarios.md     <- vem do atual Extras/Comentarios.md
│   └── rubrica-avaliacao.md       <- como os trabalhos são corrigidos
│
│
└── apendice-padroes-de-projeto/   <- fora da trilha, com aviso no topo
```

### De onde vem cada módulo

| Novo módulo | Origem hoje | Observação |
| --- | --- | --- |
| 00 — Preparação | *não existe* | escrever do zero: instalar Python, VS Code, rodar o primeiro `.py` |
| 01 — Tipos e variáveis | `01_Fundamentos_Python/01_Tipos_E_Variaveis` | falta README |
| 02 — Operadores | `01_Fundamentos_Python/02_Operadores` | 3 arquivos já bem separados |
| 03 — Entrada e saída | `01_Fundamentos_Python/03_Entrada_Saida` + `04_Conversoes` | juntar: ler dado e converter é o mesmo assunto |
| 04 — Condicionais | `01_Fundamentos_Python/05_Condicionais` + `02_Estruturas_De_Controle/01_Condicionais` + `03_Match_Case` | `match/case` vira seção final do módulo |
| 05 — Laços | `01_Fundamentos_Python/08_Lacos_Repeticao` + `02_Estruturas_De_Controle/02_Loops` | `04_codigos_resolucao.py` e `05_analise.py` vão para `gabaritos/` |
| 06 — Listas | `01_Fundamentos_Python/07_Introducao_Listas` + `03_Estruturas_De_Dados/01_Listas` | `respostas_quest_listas.py` vai para `gabaritos/` |
| 07 — Strings | `03_Estruturas_De_Dados/02_Strings` | falta README |
| 08 — Funções | `04_Funcoes` + `07_Revisao_E_Listas/Funcoes_e_Procedimentos` | a lista de 20 exercícios vira `exercicios/` |
| 09 — Matrizes | `03_Estruturas_De_Dados/03_Matrizes` (+ `extras/`) | `extras/` vira seção "Para ir além" do README |
| 10 — Tratamento de erros | `01_Fundamentos_Python/09_Tratamento_De_Erros` | ver nota abaixo |
| 11 — Ordenação | `03_Estruturas_De_Dados/04_Algoritmos_Ordenacao` | falta README |
| 12 — Leitura e refatoração | `07_Revisao_E_Listas/Cognitivo` + `Listas/Refatoracao` + `Extras/Comentarios.md` | o par `Base/` + `Refatorado/` já é ouro, só falta a prosa |
| 13 — Estudo de caso CRUD | `06_Projetos_Praticos/03_Sistemas/Implementacoes` | sistema pronto, comentado linha a linha no README |
| 14 — Projeto integrador | `06_Projetos_Praticos/03_Sistemas/Propostas` | as 9 propostas viram o cardápio do trabalho final |
| `banco-de-exercicios/` | `05_Exercicios_Praticos` | o que casar com um módulo migra para lá; o resto fica de prática extra |
| `projetos/` | `06_Projetos_Praticos/01_Calculadoras` + `02_Jogos` | desafios opcionais, citados nos módulos |
| `apendice-padroes-de-projeto/` | `08_Avancado` | manter o aviso de "fora do escopo" |

**Nota sobre o módulo 10 (erros).** Ele fica no fim, mas a dor aparece no módulo 03: `int(input())`
quebra assim que o aluno digita texto. Resolva como o resto do repositório vai resolver — com
**antecipação honesta**. No módulo 03, escreva:

> Digite uma letra quando o programa pedir um número e veja o que acontece: `ValueError`.
> Por enquanto, combine com o programa: só números. No módulo 10 você vai aprender a tratar isso
> de verdade e nunca mais deixar o programa morrer por causa de uma digitação errada.

Esse tipo de frase — prometer e cumprir depois — é o que dá sensação de trilha.

---

## 4. Convenções de escrita

### 4.1 Nomes

| Item | Regra | Exemplo |
| --- | --- | --- |
| Pasta de módulo | `modulo-NN-kebab-case`, sem acento | `modulo-05-lacos-de-repeticao` |
| Arquivo de exemplo | `NN_snake_case.py`, **sempre numerado** | `03_break_continue.py` |
| Enunciado | `EXERCICIO-NN-tema.md` | `EXERCICIO-01-tabuada.md` |
| Pasta de gabarito | `modulo-NN-exNN-tema/` | `gabaritos/modulo-05-ex01-tabuada/` |
| Variáveis e funções | `snake_case` em português, sem abreviação críptica | `calcular_media`, `notas_da_turma` |
| Constantes | `MAIUSCULO_COM_UNDERLINE` | `NOTA_MINIMA = 6.0` |

**Nada de `EX1.py`.** Se o arquivo se chama `EX1.py`, ninguém sabe o que tem dentro sem abrir.

### 4.2 Acentuação — decida uma vez e não volte atrás

- **Nomes de arquivo e pasta:** sem acento, sem espaço, sem cedilha. Sempre.
- **Conteúdo (comentários, docstrings, strings, README):** **com acento normal**. Python 3 é UTF-8
  por padrão e todo editor moderno lida bem. Texto didático sem acento parece descuidado.

Hoje o repositório faz os dois. Escolha o acento e padronize na migração.

### 4.3 A voz: conversa de professor com aluno

O texto fala **com** o aluno, na segunda pessoa, e explica o *porquê* antes do *como*.

**Faça assim:**

> Você já sabe repetir código com `while`. Mas repare no incômodo: toda vez você precisa criar o
> contador, lembrar de incrementar e torcer para não esquecer. Esqueceu o `contador += 1`? Loop
> infinito. O `for` existe justamente para tirar essa responsabilidade das suas costas.

**Não faça assim:**

> O laço `for` é uma estrutura de repetição que itera sobre um iterável.

Três hábitos que sustentam essa voz:

1. **Problema antes de solução.** Mostre o código ruim doendo, depois apresente o recurso que cura.
2. **Antecipe o erro do aluno.** "Vai dar vontade de escrever `if nota = 10`. Não vai funcionar,
   e a seção *Erros comuns* explica por quê."
3. **Peça ação, não leitura.** "Rode o exemplo, troque o `10` por `0` e veja o programa quebrar.
   Agora conserte."

---

## 5. Templates para copiar

### 5.1 `README.md` de módulo

````markdown
# Módulo 05 — Laços de repetição

No módulo anterior seu programa aprendeu a **decidir**. Agora ele vai aprender a **insistir**:
fazer a mesma coisa dez, mil ou "quantas vezes o usuário quiser" — sem você escrever dez linhas iguais.

## Objetivos de aprendizagem

Ao final deste módulo você será capaz de:

- [ ] Explicar quando usar `while` e quando usar `for`
- [ ] Escrever um laço com contador sem cair em loop infinito
- [ ] Usar `range()` com um, dois e três argumentos
- [ ] Interromper e pular iterações com `break` e `continue`
- [ ] Somar e contar valores dentro de um laço (o padrão "acumulador")

## Pré-requisitos

[Módulo 04 — Condicionais](../modulo-04-condicionais/) concluído, exercícios feitos.

## Conceito

### O problema: copiar e colar não escala

Para mostrar a tabuada do 7, sem laço, você escreveria:

```python
print(f"7 x 1 = {7 * 1}")
print(f"7 x 2 = {7 * 2}")
print(f"7 x 3 = {7 * 3}")
# ... e mais sete linhas quase idênticas
```

Funciona. Mas e se a tabuada tiver que ir até 100? E se o usuário escolher o número?
Sempre que você se pegar copiando uma linha e trocando um detalhe, **é um laço pedindo para nascer**.

### `while`: repete enquanto a condição for verdadeira

```python
contador = 1
while contador <= 10:
    print(f"7 x {contador} = {7 * contador}")
    contador += 1        # <- esquecer esta linha = loop infinito
```

Três coisas que todo `while` precisa ter, e a ordem importa:

1. **Inicializar** a variável de controle (antes do laço)
2. **Testar** a condição (no `while`)
3. **Atualizar** a variável de controle (dentro do laço)

Faltou a 3? O programa trava. Isso não é bug exótico: é o erro mais comum do módulo.

### `for`: repete um número conhecido de vezes

```python
for contador in range(1, 11):
    print(f"7 x {contador} = {7 * contador}")
```

As três responsabilidades acima viraram uma linha só. Por isso a regra prática:

| Situação | Use |
| --- | --- |
| Você sabe quantas vezes vai repetir | `for` |
| Você repete "até acontecer alguma coisa" (usuário digitar 0, acertar a senha…) | `while` |

## Exemplos guiados

| Arquivo | O que mostra |
| --- | --- |
| [exemplos/01_while.py](exemplos/01_while.py) | as três partes do `while` e o loop infinito na prática |
| [exemplos/02_for_e_range.py](exemplos/02_for_e_range.py) | `range()` com 1, 2 e 3 argumentos |
| [exemplos/03_break_continue.py](exemplos/03_break_continue.py) | sair antes da hora e pular uma volta |
| [exemplos/04_acumulador.py](exemplos/04_acumulador.py) | somar, contar e achar o maior dentro do laço |

Para rodar qualquer um deles:

```bash
cd modulo-05-lacos-de-repeticao/exemplos
python 01_while.py
```

Abra o `01_while.py`, **comente a linha do `contador += 1`** e rode de novo. Deixe travar de
propósito e interrompa com `Ctrl + C`. Ver o erro acontecer vale mais que ler sobre ele.

## Exercícios

1. [EXERCICIO-01-tabuada.md](exercicios/EXERCICIO-01-tabuada.md) — fixação de `for` e `range`.
2. [EXERCICIO-02-menu-com-while.md](exercicios/EXERCICIO-02-menu-com-while.md) — o menu que só sai quando o usuário mandar.

## Auto-avaliação

- [ ] Sei dizer, olhando um problema, se ele pede `while` ou `for`
- [ ] Já provoquei um loop infinito de propósito e sei por que ele acontece
- [ ] Sei escrever `range(1, 11)` e explicar por que o 11 não aparece na saída
- [ ] Consigo somar todos os números digitados pelo usuário até ele digitar 0

## Erros comuns

| Erro | O que está acontecendo |
| --- | --- |
| `while` que nunca termina | faltou atualizar a variável de controle dentro do laço |
| `range(1, 10)` para ir até 10 | o segundo argumento é exclusivo; use `range(1, 11)` |
| Zerar o acumulador dentro do laço | `soma = 0` tem que ficar **antes** do `for`, senão zera a cada volta |
| Confundir `=` com `==` no `while` | `=` atribui, `==` compara; em Python isso é erro de sintaxe |
| Indentação errada | a linha ficou fora do laço e executa só uma vez |

---

Anterior: [Módulo 04 — Condicionais](../modulo-04-condicionais/) | Próximo: [Módulo 06 — Listas](../modulo-06-listas/)
````

### 5.2 Arquivo de exemplo `.py`

```python
"""
Módulo 05 — Laços de repetição
Exemplo 01: as três partes do while

Este arquivo mostra:
  - inicializar, testar e atualizar a variável de controle
  - o que acontece quando você esquece de atualizar

Como executar:
  python 01_while.py
"""

# 1. INICIALIZAR a variável de controle, antes do laço
contador = 1

# 2. TESTAR: enquanto a condição for verdadeira, o bloco se repete
while contador <= 5:
    print(f"Volta número {contador}")

    # 3. ATUALIZAR: sem esta linha, contador vale 1 para sempre
    contador += 1

print(f"O laço terminou com contador = {contador}")


# --- Experimento ---------------------------------------------------
# Comente a linha "contador += 1" e rode de novo.
# O programa vai imprimir "Volta número 1" para sempre: é o loop infinito.
# Interrompa com Ctrl + C.
```

Regras do arquivo de exemplo:

- **Docstring de cabeçalho obrigatório**, com módulo, título, o que mostra e como executar.
- **Um conceito por arquivo.** Se precisar de dois títulos em caixa alta, são dois arquivos.
- **30 a 60 linhas.** Passou muito disso, quebre.
- **`print` mostra resultado, não explica teoria.** Explicação é trabalho do README.
- **Termine com um "Experimento":** uma instrução de mexer e quebrar.

### 5.3 Enunciado de exercício

````markdown
# Exercício 01 — Tabuada (fixação)

| Nível | Tempo estimado | Conceitos |
| --- | --- | --- |
| 1 de 3 | 20 min | for, range, f-string |

## Objetivo

Escrever um programa que mostra a tabuada de um número escolhido pelo usuário.

## Requisitos

1. Peça ao usuário um número inteiro.
2. Mostre a tabuada desse número, de 1 até 10, uma linha por multiplicação.
3. Use `for` com `range` — nada de dez `print` copiados.
4. Formate a saída exatamente como no exemplo abaixo (use f-string).

## Exemplo de saída

```text
Digite um número: 7
Tabuada do 7:
7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70
```

## Critérios de aceitação

- [ ] O programa funciona para qualquer número digitado, não só para o 7
- [ ] Existe exatamente um `print` dentro do laço
- [ ] `range` vai até 10 inclusive (cuidado com o limite exclusivo)
- [ ] Nenhuma variável tem nome de uma letra só, exceto o contador do laço

## Desafio opcional

Pergunte também até quanto a tabuada deve ir (até 10? até 20?) e respeite a resposta.
````

### 5.4 `gabaritos/README.md`

```markdown
# Gabaritos

As resoluções ficam aqui, longe dos enunciados, **de propósito**.

Antes de abrir qualquer arquivo desta pasta:

1. Você tentou por pelo menos 20 minutos?
2. Você releu a seção "Erros comuns" do módulo?
3. Seu programa roda, mas você não sabe se está bom? Aí sim, compare.

Errar tentando ensina mais do que ler a resposta certa. O gabarito é para **conferir**, não para
começar. Cada resolução está comentada explicando as decisões, não só o resultado.
```

---

## 6. Ordem de execução

### Fase 0 — Limpeza (30 min)

- [ ] Apagar `Nova pasta/` (está vazia)
- [ ] Decidir o destino de `Test/` (`Lab.py`, `fix.py`, `Relatorio.txt`, `fix.txt`): apagar ou mover para fora do repositório
- [ ] Revisar o `.gitignore` (`__pycache__/`, `*.pyc`, `.venv/`)
- [ ] Commit: `chore: limpeza da raiz antes da reestruturacao`

### Fase 1 — Esqueleto e documentos de raiz (2 h)

- [ ] Criar as pastas vazias da árvore da seção 3
- [ ] Escrever `GUIA-DO-ALUNO.md` (instalar Python, rodar `.py` no VS Code e no terminal, fluxo de estudo, onde pedir ajuda)
- [ ] Escrever `GLOSSARIO.md` (variável, tipo, laço, função, parâmetro, retorno, escopo, lista, índice, exceção…)
- [ ] Escrever `material-apoio/resumo-sintaxe.md` e `material-apoio/rubrica-avaliacao.md`
- [ ] Mover `07_Revisao_E_Listas/Extras/Comentarios.md` → `material-apoio/guia-de-comentarios.md`
- [ ] Reescrever o `README.md` da raiz: trilha em Mermaid + tabela de módulos + como estudar
- [ ] Commit: `docs: estrutura base e materiais de apoio`

### Fase 2 — Módulo piloto (3 h) ⭐

**Converta um módulo inteiro e leve para a sala antes de converter o resto.**

Recomendação: **módulo 05 — Laços**, porque o material atual (`08_Lacos_Repeticao`) já está
numerado, já tem exercício e já tem resolução separada. É o menor atrito para validar o formato.

- [ ] Criar `modulo-05-lacos-de-repeticao/` com README, `exemplos/`, `exercicios/`
- [ ] Quebrar o conteúdo atual em exemplos de 30–60 linhas com docstring
- [ ] Mover `04_codigos_resolucao.py` e `05_analise.py` para `gabaritos/`
- [ ] Dar aula com ele. Anotar o que o aluno perguntou que o README não respondia.
- [ ] Ajustar o template desta seção 5 com o que você aprendeu **antes de seguir**
- [ ] Commit: `feat: modulo 05 no novo padrao (piloto)`

### Fase 3 — Fundamentos: módulos 00 a 07 (8–10 h)

Um commit por módulo, na ordem 00, 01, 02, 03, 04, 06, 07 (o 05 já está pronto).
Use `git mv` nos arquivos que só mudam de lugar — preserva o histórico.

- [ ] 00 Preparação (escrever do zero)
- [ ] 01 Tipos e variáveis
- [ ] 02 Operadores
- [ ] 03 Entrada e saída (juntar com conversões)
- [ ] 04 Condicionais (absorver `match/case`)
- [ ] 06 Listas (separar `respostas_quest_listas.py` para gabaritos)
- [ ] 07 Strings

### Fase 4 — Estruturação: módulos 08 a 11 (6–8 h)

- [ ] 08 Funções (a lista de 20 exercícios vira `exercicios/` numerados)
- [ ] 09 Matrizes (`extras/` vira seção "Para ir além")
- [ ] 10 Tratamento de erros (fechar a promessa feita no módulo 03)
- [ ] 11 Algoritmos de ordenação

### Fase 5 — Fechamento: módulos 12 a 14 e periferia (6 h)

- [ ] 12 Leitura e refatoração (o par `Base/` + `Refatorado/` com a prosa que falta)
- [ ] 13 Estudo de caso CRUD (README comentando o sistema pronto por dentro)
- [ ] 14 Projeto integrador (requisitos obrigatórios + roteiro de fases + rubrica)
- [ ] Distribuir `05_Exercicios_Praticos` entre os módulos e o `banco-de-exercicios/`
- [ ] Mover jogos e calculadoras para `projetos/`, com um README que os liga aos módulos
- [ ] Mover `08_Avancado` para `apendice-padroes-de-projeto/`

### Fase 6 — Revisão final (2 h)

- [ ] Rodar **todos** os `.py` de `exemplos/` e confirmar que nenhum quebra
- [ ] Conferir que todo link relativo de `.md` aponta para arquivo existente
- [ ] Conferir que todo módulo tem as 8 seções do contrato
- [ ] Conferir que nenhum gabarito sobrou dentro de pasta de módulo
- [ ] Apagar este `PLANO-REESTRUTURACAO.md`
- [ ] Commit: `docs: fecha a reestruturacao do repositorio`

**Esforço total estimado: 28 a 32 horas.** Não tente fazer num fim de semana. Um módulo por dia,
na ordem em que você dá aula, mantém o repositório utilizável o tempo inteiro — o aluno vai
encontrando o material novo conforme o curso avança.

---

## 7. Definição de pronto

Um módulo só está pronto quando **todas** estas linhas puderem ser marcadas:

- [ ] `README.md` tem as 8 seções do contrato, na ordem
- [ ] Os objetivos de aprendizagem começam com verbo e são verificáveis
- [ ] O conceito mostra o **problema** antes da solução
- [ ] Todo arquivo em `exemplos/` tem docstring de cabeçalho e roda sem erro
- [ ] Nenhum arquivo de exemplo passa de ~60 linhas
- [ ] Todo exercício tem tabela de nível, exemplo de saída e critérios de aceitação
- [ ] Todo exercício tem gabarito comentado em `gabaritos/`
- [ ] Nenhuma resposta ficou dentro da pasta do módulo
- [ ] A tabela de erros comuns tem pelo menos 4 linhas (tirados da sua experiência de sala)
- [ ] O rodapé de navegação aponta para módulos que existem
- [ ] Os nomes seguem a seção 4.1, sem exceção

---

## 8. Duas decisões que valem a pena

**Aceite perder o estilo "apostila executável".** Rodar `if_else.py` e ver a aula sair na tela é
confortável para a demonstração ao vivo. Mas isso mistura o material do professor com o material do
aluno, e é a raiz da inconsistência de hoje. O README dá conta da explicação melhor do que uma
sequência de `print`, e o exemplo curto continua rodável para a demonstração. Se sentir falta de um
arquivo "para projetar na aula", crie `exemplos/00_demonstracao_aula.py` — mas assumido como tal,
não como o material padrão.

**Padronize o formato antes de melhorar o conteúdo.** É tentador reescrever explicações enquanto
migra. Não faça as duas coisas na mesma passada: primeiro tudo no formato novo, depois melhorias
de conteúdo módulo a módulo. Misturar as duas é o caminho mais curto para largar a reestruturação
pela metade — e um repositório meio migrado é pior que o de hoje.
