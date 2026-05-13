"""
==========================================================================
LISTA DE EXERCÍCIOS - FUNDAMENTOS DO PYTHON
Baseada nos conteúdos de 01_Fundamentos_Python
==========================================================================

INSTRUÇÕES:
  - Escreva seu código logo abaixo de cada enunciado.
  - Leia com atenção os exemplos antes de resolver.
  - Use print() para exibir os resultados sempre que indicado.
==========================================================================
"""
# ==========================================================================
# SEÇÃO 1 – TIPOS E VARIÁVEIS
# ==========================================================================

# --------------------------------------------------------------------------
# Exercício 1 — Identificando Tipos
# Crie três variáveis: uma do tipo int, uma float e uma str.
# Exiba o valor e o tipo de cada uma usando print() e type().
#
# Exemplo de saída:
#   Valor: 42   | Tipo: <class 'int'>
#   Valor: 3.14 | Tipo: <class 'float'>
#   Valor: Olá  | Tipo: <class 'str'>
# --------------------------------------------------------------------------



# --------------------------------------------------------------------------
# Exercício 2 — Apresentação Pessoal
# Declare variáveis para nome (str), idade (int) e altura (float).
# Exiba uma linha de apresentação formatada usando f-string.
#
# Saída esperada:
#   "Olá! Meu nome é Ana, tenho 20 anos e minha altura é 1.65 m."
# --------------------------------------------------------------------------



# --------------------------------------------------------------------------
# Exercício 3 — Avaliação Booleana
# Crie quatro variáveis com os valores: 1, 0, "" e "Python".
# Para cada uma, exiba o resultado de bool(variavel).
#
# Saída esperada:
#   bool(1)        -> True
#   bool(0)        -> False
#   bool("")       -> False
#   bool("Python") -> True
# --------------------------------------------------------------------------



# ==========================================================================
# SEÇÃO 2 – OPERADORES ARITMÉTICOS E EXPRESSÕES
# ==========================================================================

# --------------------------------------------------------------------------
# Exercício 4 — Quatro Operações
# Declare a = 10 e b = 3.
# Exiba o resultado de cada operação básica em uma linha separada.
#
# Saída esperada:
#   10 + 3 = 13
#   10 - 3 = 7
#   10 * 3 = 30
#   10 / 3 = 3.3333333333333335
# --------------------------------------------------------------------------



# --------------------------------------------------------------------------
# Exercício 5 — Divisão Inteira e Resto
# Dados a = 10 e b = 3, exiba o quociente inteiro e o resto da divisão.
#
# Saída esperada:
#   Quociente: 3
#   Resto: 1
# --------------------------------------------------------------------------



# --------------------------------------------------------------------------
# Exercício 6 — Potência com Repetição
# Calcule 2^10 usando um laço (for ou while), SEM usar ** nem pow().
# Exiba o resultado ao final.
#
# Saída esperada:
#   2 elevado a 10 = 1024
# --------------------------------------------------------------------------



# --------------------------------------------------------------------------
# Exercício 7 — Média Ponderada
# Declare três notas e seus respectivos pesos conforme abaixo:
#   nota1 = 8,  peso1 = 2
#   nota2 = 6,  peso2 = 3
#   nota3 = 9,  peso3 = 5
# Calcule e exiba a média ponderada.
# Fórmula: (nota1*peso1 + nota2*peso2 + nota3*peso3) / (peso1+peso2+peso3)
#
# Saída esperada:
#   Média ponderada: 7.7
# --------------------------------------------------------------------------



# ==========================================================================
# SEÇÃO 3 – CONVERSÕES DE TIPOS
# ==========================================================================

# --------------------------------------------------------------------------
# Exercício 8 — String para Número
# Dada a string texto = "42", converta-a para int e exiba o resultado.
# Dada a string texto = "3.14", converta-a para float e exiba o resultado.
#
# Saída esperada:
#   "42"   -> 42   (int)
#   "3.14" -> 3.14 (float)
# --------------------------------------------------------------------------



# --------------------------------------------------------------------------
# Exercício 9 — Inteiro para Binário
# Dado numero = 10, exiba sua representação em binário sem o prefixo "0b".
# Dica: use bin() e fatiamento de string.
#
# Saída esperada:
#   10 em binário = 1010
# --------------------------------------------------------------------------



# --------------------------------------------------------------------------
# Exercício 10 — Arredondamento
# Dado numero = 3.14159, exiba o valor arredondado para 2 casas decimais.
# Use round().
#
# Saída esperada:
#   3.14159 arredondado = 3.14
# --------------------------------------------------------------------------



# ==========================================================================
# SEÇÃO 4 – CONDICIONAIS
# ==========================================================================

# --------------------------------------------------------------------------
# Exercício 11 — Par ou Ímpar
# Peça um número ao usuário e informe se ele é Par ou Ímpar.
#
# Exemplo de saída:
#   Digite um número: 7
#   7 é Ímpar.
# --------------------------------------------------------------------------



# --------------------------------------------------------------------------
# Exercício 12 — Classificação de Nota
# Peça uma nota ao usuário (0 a 10) e exiba o conceito correspondente:
#   >= 9.0  -> "A – Excelente"
#   >= 7.0  -> "B – Bom"
#   >= 5.0  -> "C – Regular"
#   >= 3.0  -> "D – Insuficiente"
#   < 3.0   -> "E – Reprovado"
# --------------------------------------------------------------------------



# --------------------------------------------------------------------------
# Exercício 13 — Faixa Etária
# Peça a idade ao usuário e exiba a faixa etária:
#   0  a 12  -> "Criança"
#   13 a 17  -> "Adolescente"
#   18 a 59  -> "Adulto"
#   60 ou +  -> "Idoso"
# --------------------------------------------------------------------------



# --------------------------------------------------------------------------
# Exercício 14 — Maior de Três
# Peça três números ao usuário e exiba o maior deles.
# Use apenas if/elif/else, sem max().
# --------------------------------------------------------------------------



# --------------------------------------------------------------------------
# Exercício 15 — Calculadora com Condicional
# Peça dois números e uma operação (+, -, *, /) ao usuário.
# Exiba o resultado ou uma mensagem de erro para divisão por zero
# ou operação inválida.
#
# Exemplo de saída:
#   Primeiro número: 10
#   Operação: /
#   Segundo número: 0
#   Erro: divisão por zero não é permitida!
# --------------------------------------------------------------------------



# ==========================================================================
# SEÇÃO 5 – LISTAS
# ==========================================================================

# --------------------------------------------------------------------------
# Exercício 16 — Soma de Lista
# Dada a lista: numeros = [1, 2, 3, 4, 5]
# Calcule e exiba a soma dos elementos usando um laço (não use sum()).
#
# Saída esperada:
#   Soma: 15
# --------------------------------------------------------------------------



# --------------------------------------------------------------------------
# Exercício 17 — Média de Lista
# Dada a lista: notas = [6, 8, 10, 7, 9]
# Calcule e exiba a média aritmética.
#
# Saída esperada:
#   Média: 8.0
# --------------------------------------------------------------------------



# --------------------------------------------------------------------------
# Exercício 18 — Contar Pares
# Dada a lista: numeros = [1, 2, 3, 4, 5, 6, 7, 8]
# Conte e exiba quantos números são pares.
#
# Saída esperada:
#   Quantidade de pares: 4
# --------------------------------------------------------------------------



# --------------------------------------------------------------------------
# Exercício 19 — Filtrar Positivos
# Dada a lista: valores = [3, -1, 0, 7, -5, 2, -3, 8]
# Crie uma nova lista apenas com os números maiores que zero e exiba-a.
#
# Saída esperada:
#   Positivos: [3, 7, 2, 8]
# --------------------------------------------------------------------------



# --------------------------------------------------------------------------
# Exercício 20 — Inverter Lista
# Dada a lista: letras = ["a", "b", "c", "d", "e"]
# Crie uma nova lista com os elementos em ordem inversa usando um laço
# (não use reversed() nem [::-1]).
#
# Saída esperada:
#   Invertida: ['e', 'd', 'c', 'b', 'a']
# --------------------------------------------------------------------------



# --------------------------------------------------------------------------
# Exercício 21 — Máximo e Mínimo
# Dada a lista: numeros = [3, 1, 9, 2, 7, 5]
# Encontre e exiba o maior e o menor valor usando um laço (não use max()/min()).
#
# Saída esperada:
#   Maior: 9
#   Menor: 1
# --------------------------------------------------------------------------



# ==========================================================================
# SEÇÃO 6 – INTEGRAÇÃO (Programas Completos)
# ==========================================================================

# --------------------------------------------------------------------------
# Exercício 22 — Conversor de Temperatura
# Peça ao usuário uma temperatura em Celsius e exiba o equivalente
# em Fahrenheit e em Kelvin.
#
# Fórmulas:
#   Fahrenheit: F = C * 9/5 + 32
#   Kelvin:     K = C + 273.15
#
# Exemplo de saída:
#   Temperatura em Celsius: 100
#   Fahrenheit: 212.0 °F
#   Kelvin:     373.15 K
# --------------------------------------------------------------------------



# --------------------------------------------------------------------------
# Exercício 23 — Sistema de Notas
# Dada a lista: notas = [8, 6, 9, 4, 7]
# Calcule e exiba:
#   - Média da turma
#   - Maior nota
#   - Menor nota
#   - Quantidade de alunos aprovados (nota >= 7)
#   - Quantidade de alunos reprovados (nota < 7)
#   - Situação: "Turma Aprovada" se média >= 7, senão "Turma Reprovada"
#
# Saída esperada:
#   Média:      6.8
#   Maior nota: 9
#   Menor nota: 4
#   Aprovados:  3
#   Reprovados: 2
#   Situação:   Turma Reprovada
# --------------------------------------------------------------------------



# --------------------------------------------------------------------------
# Exercício 24 — Sequência de Fibonacci
# Peça ao usuário quantos termos da sequência deseja ver.
# Exiba os termos na tela. Sequência: 0, 1, 1, 2, 3, 5, 8, 13, ...
#
# Exemplo de saída:
#   Quantos termos? 7
#   Fibonacci: [0, 1, 1, 2, 3, 5, 8]
# --------------------------------------------------------------------------



# --------------------------------------------------------------------------
# Exercício 25 — Ordenação (Bubble Sort)
# Dada a lista: numeros = [5, 3, 8, 1, 9, 2]
# Ordene-a em ordem crescente usando o algoritmo Bubble Sort.
# Não use sort() nem sorted().
#
# Algoritmo:
#   Compare elementos adjacentes e troque-os se estiverem fora de ordem.
#   Repita até a lista estar ordenada.
#
# Saída esperada:
#   Lista ordenada: [1, 2, 3, 5, 8, 9]
# --------------------------------------------------------------------------