"""
Módulo 06 — Listas
Exemplo 01: criando e acessando

Este arquivo mostra:
  - criar listas de números, textos e vazias
  - acessar por índice positivo e negativo
  - por que o índice começa em zero, e o IndexError

Como executar:
  python 01_criando_e_acessando.py
"""

# --- Criando ---------------------------------------------------------
numeros = [1, 2, 3, 4, 5]
nomes = ["Ana", "Bruno", "Carlos", "Diana"]
vazia = []

print(f"numeros = {numeros}")
print(f"nomes   = {nomes}")
print(f"vazia   = {vazia}")
print()


# --- Acessando -------------------------------------------------------
cores = ["vermelho", "azul", "verde", "amarelo"]

print(f"cores = {cores}")
print("índice:      0        1       2        3")
print("negativo:   -4       -3      -2       -1")
print()

print(f"cores[0]  = {cores[0]}      <- o PRIMEIRO é o zero")
print(f"cores[2]  = {cores[2]}")
print(f"cores[-1] = {cores[-1]}      <- o último, sem saber o tamanho")
print(f"cores[-2] = {cores[-2]}")
print()


# --- Por que o zero --------------------------------------------------
# O índice não diz "qual elemento", diz "quantos pular".
# O primeiro não pula nenhum, então é 0.
print(f"a lista tem {len(cores)} elementos")
print(f"os índices válidos vão de 0 até {len(cores) - 1}")
print()

# As duas formas de pegar o último:
print(f"cores[len(cores) - 1] = {cores[len(cores) - 1]}")
print(f"cores[-1]             = {cores[-1]}      <- prefira esta")
print()


# --- IndexError ------------------------------------------------------
# A lista tem 4 elementos, mas cores[4] NÃO existe.
# Descomente a linha abaixo para ver:
#
# print(cores[4])
#
#   IndexError: list index out of range
#
# "out of range" = fora da faixa. O 4 seria o quinto elemento.
print("A lista tem 4 elementos, e o último índice é 3.")
print("cores[4] daria IndexError — descomente no arquivo para ver.")


# --- Experimento ---------------------------------------------------
# 1. Descomente o print(cores[4]) e rode. Leia a mensagem e comente
#    de novo.
#
# 2. Rode print(cores[-5]). Também dá IndexError? Por quê?
#
# 3. Rode print(vazia[0]). Uma lista vazia não tem nem o índice 0 —
#    é o erro que aparece quando você esquece de checar se a lista
#    tem algo antes de acessar.
