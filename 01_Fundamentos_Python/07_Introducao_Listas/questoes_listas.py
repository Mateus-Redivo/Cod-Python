"""
=========================================
QUESTÕES DE FIXAÇÃO - INTRODUÇÃO A LISTAS
=========================================
Conceitos abordados:
  - Criação e acesso a listas
  - len(), in, índices positivos e negativos
  - append(), insert(), extend()
  - remove(), pop(), del, clear()
  - count(), index()
  - sort(), sorted(), reverse()
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
# QUESTÃO 3 — Modificar, append e insert
# ─────────────────────────────────────────
"""
Comece com a lista:
  times = ["Flamengo", "Palmeiras", "Santos"]

  a) Altere "Santos" para "Grêmio"
  b) Adicione "Corinthians" no final da lista
  c) Insira "Vasco" na posição 1 (segundo elemento)

Imprima a lista após cada modificação.
"""

times = ["Flamengo", "Palmeiras", "Santos"]

# Seu código aqui:


# ─────────────────────────────────────────
# QUESTÃO 4 — Remoção de elementos
# ─────────────────────────────────────────
"""
Dada a lista:
  esportes = ["Futebol", "Basquete", "Vôlei", "Natação", "Tênis"]

  a) Remova "Vôlei" usando remove()
  b) Remova o último elemento usando pop() e imprima qual foi removido
  c) Delete o elemento do índice 0 usando del
  d) Imprima a lista final
"""

esportes = ["Futebol", "Basquete", "Vôlei", "Natação", "Tênis"]

# Seu código aqui:


# ─────────────────────────────────────────
# QUESTÃO 5 — count() e index()
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
# QUESTÃO 6 — sort() e sorted()
# ─────────────────────────────────────────
"""
Dada a lista:
  temperaturas = [32, 18, 25, 11, 40, 28, 15]

  a) Crie uma nova lista ordenada de forma crescente com sorted()
     (a lista original NÃO deve ser modificada)
  b) Ordene a lista original em ordem decrescente com sort()
  c) Imprima as três listas: original após passo (b), a criada em (a)
     e confirme que sorted() não alterou a original antes do sort()

Dica: guarde a lista original com sorted() antes de aplicar sort().
"""

temperaturas = [32, 18, 25, 11, 40, 28, 15]

# Seu código aqui:


# ─────────────────────────────────────────
# QUESTÃO 7 — reverse() e extend()
# ─────────────────────────────────────────
"""
  a) Crie uma lista chamada `vogais` com: ["a", "e", "i", "o", "u"]
  b) Inverta a ordem da lista com reverse() e a imprima
  c) Crie uma lista chamada `extras` com: ["y", "w"]
  d) Adicione todos os elementos de `extras` em `vogais` usando extend()
  e) Imprima a lista final
"""

# Seu código aqui:


# ─────────────────────────────────────────
# QUESTÃO 8 — Fatiamento (slicing)
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
# QUESTÃO 9 — Percorrer lista com for
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
# QUESTÃO 10 — Desafio: lista dinâmica
# ─────────────────────────────────────────
"""
Crie um programa que:
  1. Começa com uma lista vazia chamada `alunos`
  2. Pede ao usuário para digitar 5 nomes de alunos e os adiciona
     à lista com append()
  3. Ordena a lista em ordem alfabética com sort()
  4. Exibe os alunos numerados (1, 2, 3...) usando for com range(len(...))
  5. Pergunta ao usuário um nome para buscar:
       - Se encontrado: mostra em qual posição está (índice + 1)
       - Se não encontrado: exibe uma mensagem informando
"""

# Seu código aqui:
