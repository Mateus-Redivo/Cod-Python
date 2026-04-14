"""
=========================================
QUESTÕES DE FIXAÇÃO - INTRODUÇÃO A LISTAS
=========================================
Conceitos abordados:
  - Criação e acesso a listas
  - len(), in, índices positivos e negativos
  - append()
  - count(), index()
  - Fatiamento (slicing)
  - Percorrer listas com for
"""

# ─────────────────────────────────────────
# QUESTÃO 1 — Criação e acesso por índice
# ─────────────────────────────────────────
"""
Crie uma lista chamada `planetas` com os seguintes valores (nessa ordem):
"Mercúrio", "Vênus", "Terra", "Marte", "Júpiter"

Em seguida, imprima:
  a) O primeiro planeta da lista
  b) O último planeta usando índice negativo
  c) O terceiro planeta usando índice positivo
"""

# Seu código aqui:


# ─────────────────────────────────────────
# QUESTÃO 2 — Tamanho e verificação de elemento
# ─────────────────────────────────────────
"""
Dada a lista abaixo:
  disciplinas = ["Matemática", "Português", "História", "Ciências", "Inglês"]

  a) Imprima quantas disciplinas existem na lista
  b) Verifique se "Inglês" está na lista e exiba uma mensagem informando o resultado
  c) Verifique se "Filosofia" está na lista e exiba uma mensagem informando o resultado
"""

disciplinas = ["Matemática", "Português", "História", "Ciências", "Inglês"]

# Seu código aqui:


# ─────────────────────────────────────────
# QUESTÃO 3 — Modificar e append
# ─────────────────────────────────────────
"""
Comece com a lista:
  times = ["Flamengo", "Palmeiras", "Santos"]

  a) Altere "Santos" para "Grêmio"
  b) Adicione "Corinthians" no final da lista

Imprima a lista após cada modificação.
"""

times = ["Flamengo", "Palmeiras", "Santos"]

# Seu código aqui:


# ─────────────────────────────────────────
# QUESTÃO 4 — count() e index()
# ─────────────────────────────────────────
"""
Dada a lista:
  notas = [7, 8, 6, 10, 8, 9, 6, 8, 5, 10]

  a) Quantas vezes o valor 8 aparece na lista?
  b) Quantas vezes o valor 6 aparece?
  c) Em qual índice está o primeiro 10?
  d) Em qual índice está o primeiro 5?

Imprima os resultados com mensagens explicativas.
"""

notas = [7, 8, 6, 10, 8, 9, 6, 8, 5, 10]

# Seu código aqui:


# ─────────────────────────────────────────
# QUESTÃO 5 — Fatiamento (slicing)
# ─────────────────────────────────────────
"""
Dada a lista:
  meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun",
           "Jul", "Ago", "Set", "Out", "Nov", "Dez"]

Usando slicing, imprima:
  a) Os 3 primeiros meses
  b) Os 3 últimos meses (use índices negativos)
  c) Os meses do segundo semestre (Jul a Dez)
  d) Apenas os meses de índice par (Jan, Mar, Mai...) usando passo 2
"""

meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun",
         "Jul", "Ago", "Set", "Out", "Nov", "Dez"]

# Seu código aqui:


# ─────────────────────────────────────────
# QUESTÃO 6 — Percorrer lista com for
# ─────────────────────────────────────────
"""
Dada a lista de preços:
  precos = [15.90, 8.50, 22.00, 4.75, 31.20]

  a) Use um for para imprimir cada preço no formato: "Produto X: R$ Y"
     (X é o número do produto começando em 1, Y é o preço)
  b) Calcule e imprima o total de todos os preços
  c) Calcule e imprima a média dos preços
"""

precos = [15.90, 8.50, 22.00, 4.75, 31.20]

# Seu código aqui:


# ─────────────────────────────────────────
# QUESTÃO 7 — Índices e acesso avançado
# ─────────────────────────────────────────
"""
Dada a lista:
  cores = ["vermelho", "azul", "verde", "amarelo", "branco", "preto"]

  a) Imprima o penúltimo elemento usando índice negativo
  b) Imprima o segundo e o quarto elemento usando índices positivos
  c) Verifique se "roxo" está na lista e exiba uma mensagem
  d) Imprima o total de elementos da lista usando len()
"""

cores = ["vermelho", "azul", "verde", "amarelo", "branco", "preto"]

# Seu código aqui:


# ─────────────────────────────────────────
# QUESTÃO 8 — append() e construção de lista
# ─────────────────────────────────────────
"""
  a) Crie uma lista vazia chamada `pares`
  b) Use um for com range() para adicionar com append() todos os números
     pares de 2 até 20 (inclusive)
  c) Imprima a lista completa
  d) Imprima quantos elementos ela possui
"""

# Seu código aqui:


# ─────────────────────────────────────────
# QUESTÃO 9 — count() e index() avançado
# ─────────────────────────────────────────
"""
Dada a lista:
  letras = ["a", "b", "a", "c", "b", "a", "d", "b", "a", "c"]

  a) Quantas vezes "a" aparece?
  b) Quantas vezes "b" aparece?
  c) Em qual índice está o primeiro "c"?
  d) Em qual índice está o primeiro "d"?
  e) Qual letra aparece mais vezes: "a" ou "b"? Exiba uma mensagem com a resposta.
"""

letras = ["a", "b", "a", "c", "b", "a", "d", "b", "a", "c"]

# Seu código aqui:


# ─────────────────────────────────────────
# QUESTÃO 10 — Fatiamento avançado
# ─────────────────────────────────────────
"""
Dada a lista:
  numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

  a) Imprima os 5 primeiros elementos
  b) Imprima os 4 últimos elementos usando índice negativo
  c) Imprima os elementos do índice 2 ao 7 (inclusive)
  d) Imprima todos os elementos de passo 2 (índices pares)
  e) Imprima a lista de trás para frente usando passo -1
"""

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Seu código aqui:


# ─────────────────────────────────────────
# QUESTÃO 11 — for com índice e acumulador
# ─────────────────────────────────────────
"""
Dada a lista:
  idades = [14, 23, 17, 31, 19, 25, 16, 28]

  a) Use um for para imprimir cada idade no formato: "Pessoa X tem Y anos"
     (X começa em 1)
  b) Conte quantas pessoas têm menos de 18 anos
  c) Calcule a soma de todas as idades
  d) Imprima a idade que está no meio da lista (índice len()//2)
"""

idades = [14, 23, 17, 31, 19, 25, 16, 28]

# Seu código aqui:


# ─────────────────────────────────────────
# QUESTÃO 12 — Combinando len(), in e for
# ─────────────────────────────────────────
"""
Dada a lista:
  frutas = ["maçã", "banana", "uva", "manga", "pera", "uva", "banana", "uva"]

  a) Imprima o total de frutas na lista
  b) Verifique se "abacaxi" está na lista
  c) Use um for para imprimir apenas as frutas que têm mais de 4 letras
  d) Conte quantas vezes "uva" aparece usando count()
  e) Imprima em qual índice está a primeira "banana"
"""

frutas = ["maçã", "banana", "uva", "manga", "pera", "uva", "banana", "uva"]

# Seu código aqui:


# ─────────────────────────────────────────
# QUESTÃO 13 — Desafio: lista dinâmica
# ─────────────────────────────────────────
"""
Crie um programa que:
  1. Começa com uma lista vazia chamada `alunos`
  2. Pede ao usuário para digitar 5 nomes de alunos e os adiciona
     à lista com append()
  3. Exibe os alunos numerados (1, 2, 3...) usando for com range(len(...))
  4. Pergunta ao usuário um nome para buscar:
       - Se encontrado: mostra em qual posição está (índice + 1)
       - Se não encontrado: exibe uma mensagem informando
"""

# Seu código aqui:
