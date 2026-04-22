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

# ─────────────────────────────────────────
# QUESTÃO 14 — TEORIA: Verdadeiro ou Falso
# ─────────────────────────────────────────
"""
Analise cada afirmação e escreva, nos comentários, se é VERDADEIRA ou FALSA.
Se for falsa, corrija-a em uma linha adicional.

a) Em Python, o índice do primeiro elemento de uma lista é 1.
b) O índice -1 sempre se refere ao último elemento da lista.
c) A função len() retorna o maior valor da lista.
"""

# Suas respostas:
# a)
# b)
# c)


# ─────────────────────────────────────────
# QUESTÃO 15 — ANÁLISE DE CÓDIGO
# ─────────────────────────────────────────
"""
Leia o trecho abaixo e responda às perguntas SEM executar o código:

  animais = ["gato", "cachorro", "peixe", "pássaro", "hamster"]
  print(animais[1])
  print(animais[-2])
  print(len(animais))

a) O que cada print exibe? Escreva o resultado esperado ao lado de cada linha.
b) Se adicionarmos animais.append("tartaruga"), qual será o novo len(animais)?
c) Qual seria o índice negativo para acessar "cachorro" nessa lista?
"""

# Suas respostas:
# a)
# b)
# c)


# ─────────────────────────────────────────
# QUESTÃO 16 — ANÁLISE DE CÓDIGO: slicing
# ─────────────────────────────────────────
"""
Dada a lista abaixo, qual é a saída de cada linha?
Responda nos comentários SEM executar o código.

  numeros = [10, 20, 30, 40, 50, 60, 70, 80]

  print(numeros[2:5])
  print(numeros[:3])
  print(numeros[5:])

a) O que numeros[2:5] exibe?
b) O que numeros[:3] exibe?
c) O que numeros[5:] exibe?
"""

# Suas respostas:
# a)
# b)
# c)


# ─────────────────────────────────────────
# QUESTÃO 17 — TEORIA: Lacunas conceituais
# ─────────────────────────────────────────
"""
Preencha as lacunas com o termo ou símbolo correto:

a) Para acessar o segundo elemento de uma lista `x`, usamos x[___].
b) O método ___________ retorna quantas vezes um valor aparece na lista.
c) O método ___________ retorna o índice da primeira ocorrência de um valor.
"""

# Suas respostas:
# a)
# b)
# c)


# ─────────────────────────────────────────
# QUESTÃO 18 — ANÁLISE DE CÓDIGO: for
# ─────────────────────────────────────────
"""
Analise o código abaixo e responda às perguntas:

  valores = [3, 7, 2, 9, 5, 1, 8]
  total = 0
  contador = 0

  for v in valores:
      if v > 4:
          total += v
          contador += 1

  print(total)
  print(contador)

a) Quais elementos da lista são maiores que 4?
b) Qual é o valor impresso por print(total)?
c) Qual é o valor impresso por print(contador)?
"""

# Suas respostas:
# a)
# b)
# c)


# ─────────────────────────────────────────
# QUESTÃO 19 — Prática: construção com for e append
# ─────────────────────────────────────────
"""
  a) Crie uma lista vazia chamada `quadrados`
  b) Use um for com range(1, 11) para adicionar com append()
     o quadrado de cada número (1², 2², 3², ..., 10²)
  c) Imprima a lista completa
"""

# Seu código aqui:


# ─────────────────────────────────────────
# QUESTÃO 20 — Prática: filtragem com for
# ─────────────────────────────────────────
"""
Dada a lista:
  temperaturas = [36.5, 37.0, 38.2, 35.9, 39.1, 36.8, 40.0, 37.5]

  a) Use um for para imprimir apenas as temperaturas acima de 37.5
     no formato: "Febre alta: X°C"
  b) Conte quantas temperaturas estão abaixo de 37.5 (estado normal)
  c) Calcule a temperatura média da lista
"""

temperaturas = [36.5, 37.0, 38.2, 35.9, 39.1, 36.8, 40.0, 37.5]

# Seu código aqui:


# ─────────────────────────────────────────
# QUESTÃO 21 — ANÁLISE DE CÓDIGO: append e for
# ─────────────────────────────────────────
"""
O que a lista `resultado` contém ao final deste código?
Responda nos comentários SEM executar.

  numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  resultado = []

  for n in numeros:
      if n % 3 == 0:
          resultado.append(n)

  print(resultado)
  print(len(resultado))

a) Qual é o conteúdo de `resultado`?
b) Qual é o valor de len(resultado)?
c) Qual é o critério usado para filtrar os números?
"""

# Suas respostas:
# a)
# b)
# c)


# ─────────────────────────────────────────
# QUESTÃO 22 — Prática: índices e modificação
# ─────────────────────────────────────────
"""
Dada a lista:
  notas = [5, 7, 4, 9, 6, 3, 8, 7]

  a) Substitua a primeira nota por 6
  b) Substitua a última nota por 10 (use índice negativo)
  c) Imprima a nota do meio da lista usando len()//2 como índice
"""

notas = [5, 7, 4, 9, 6, 3, 8, 7]

# Seu código aqui:


# ─────────────────────────────────────────
# QUESTÃO 23 — TEORIA: corrija os erros
# ─────────────────────────────────────────
"""
Cada trecho abaixo contém UM erro. Identifique e corrija cada um.

a)  lista = [1, 2, 3]
    print(lista[3])          # erro aqui

b)  frutas = ["maçã", "pera"]
    frutas.append["uva"]     # erro aqui

c)  nomes = ["Ana", "Bia", "Carlos"]
    print(len[nomes])        # erro aqui
"""

# Suas correções:
# a)
# b)
# c)


# ─────────────────────────────────────────
# QUESTÃO 24 — Prática: count() e index() com lógica
# ─────────────────────────────────────────
"""
Dada a lista:
  respostas = ["A", "B", "A", "C", "A", "B", "D", "A", "C", "B"]

  a) Quantas vezes cada alternativa aparece? (A, B, C e D)
  b) Qual alternativa foi mais marcada?
  c) Em qual índice está a primeira resposta "D"?
"""

respostas = ["A", "B", "A", "C", "A", "B", "D", "A", "C", "B"]

# Seu código aqui:


# ─────────────────────────────────────────
# QUESTÃO 25 — ANÁLISE DE CÓDIGO: slicing com passo
# ─────────────────────────────────────────
"""
Analise o código e responda SEM executar:

  letras = ["a", "b", "c", "d", "e", "f", "g", "h"]

  print(letras[1::2])
  print(letras[::3])
  print(letras[6:1:-2])

a) O que cada print exibe?
b) O que o passo negativo em letras[6:1:-2] significa?
c) Por que letras[6:1:-2] não inclui o elemento do índice 1?
"""

# Suas respostas:
# a) letras[1::2]    →
#    letras[::3]     →
#    letras[6:1:-2]  →
# b)
# c)


# ─────────────────────────────────────────
# QUESTÃO 26 — Prática: for com range(len())
# ─────────────────────────────────────────
"""
Dadas as listas:
  produtos = ["Arroz", "Feijão", "Macarrão", "Óleo", "Sal"]
  precos   = [5.49, 8.90, 3.25, 6.70, 2.10]

  a) Use for com range(len(produtos)) para imprimir cada produto
     e seu preço no formato: "1. Arroz — R$ 5.49"
  b) Calcule e imprima o total da compra
  c) Imprima o nome do produto mais barato (use index() sobre a lista precos)
"""

produtos = ["Arroz", "Feijão", "Macarrão", "Óleo", "Sal"]
precos = [5.49, 8.90, 3.25, 6.70, 2.10]

# Seu código aqui:


# ─────────────────────────────────────────
# QUESTÃO 27 — TEORIA: preveja a saída
# ─────────────────────────────────────────
"""
Escreva exatamente o que cada bloco imprime, sem executar.

Bloco A:
  x = [1, 2, 3, 4, 5]
  print(x[len(x) - 1])

Bloco B:
  y = ["sol", "lua", "estrela"]
  y.append("cometa")
  print(y[-2])

Bloco C:
  z = [10, 20, 30, 40, 50]
  print(z.count(30))
  print(z.index(40))
"""

# Suas respostas:
# Bloco A →
# Bloco B →
# Bloco C →


# ─────────────────────────────────────────
# QUESTÃO 28 — Desafio: votação
# ─────────────────────────────────────────
"""
Crie um programa de votação simples:

  a) Comece com candidatos = ["Alice", "Bruno", "Carla"] e votos = []
     Use um for com range(8) pedindo ao usuário um nome a cada rodada.
     - Se o nome estiver em candidatos, adicione a votos
     - Caso contrário: exiba "Voto inválido!"

  b) Ao final, exiba quantos votos cada candidato recebeu (use count())

  c) Exiba o nome do candidato vencedor
     (dica: use count() para comparar e uma variável acumuladora)
"""

# Seu código aqui:
