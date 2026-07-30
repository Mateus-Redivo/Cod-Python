"""
Módulo 06 — Listas
Exemplo 04: fatias e funções úteis

Este arquivo mostra:
  - fatiar com [inicio:fim] e o limite exclusivo
  - len, sum, max, min e o operador in
  - que a fatia devolve uma lista NOVA

Como executar:
  python 04_fatiando.py
"""

numeros = [10, 20, 30, 40, 50]
print(f"numeros = {numeros}")
print("índice:    0   1   2   3   4")
print()

# --- Fatias ----------------------------------------------------------
# O limite final é EXCLUSIVO — a mesma regra do range() do módulo 05.
print(f"numeros[1:3]  = {numeros[1:3]}      <- do 1 até ANTES do 3")
print(f"numeros[:3]   = {numeros[:3]}  <- do começo até antes do 3")
print(f"numeros[2:]   = {numeros[2:]}  <- do 2 até o fim")
print(f"numeros[-2:]  = {numeros[-2:]}      <- os dois últimos")
print(f"numeros[:]    = {numeros[:]}  <- a lista inteira")
print()

# A fatia devolve uma lista NOVA. Mexer nela não afeta a original.
metade = numeros[:2]
metade.append(999)
print(f"metade após append: {metade}")
print(f"numeros continua:   {numeros}   <- intacta")
print()


# --- Funções que economizam laço -------------------------------------
notas = [8, 7, 10, 6]
print(f"notas = {notas}")
print(f"len(notas) = {len(notas)}     quantos elementos")
print(f"sum(notas) = {sum(notas)}    soma tudo")
print(f"max(notas) = {max(notas)}    o maior")
print(f"min(notas) = {min(notas)}     o menor")
print(f"média      = {sum(notas) / len(notas):.2f}")
print()


# --- in: está na lista? ----------------------------------------------
frutas = ["maçã", "banana", "laranja"]
print(f"frutas = {frutas}")
print(f'"banana" in frutas -> {"banana" in frutas}')
print(f'"manga"  in frutas -> {"manga" in frutas}')
print()

# Serve direto num if, e lê como português:
if "banana" in frutas:
    print("Tem banana na lista.")

# E o contrário:
if "manga" not in frutas:
    print("Não tem manga na lista.")


# --- Experimento ---------------------------------------------------
# 1. Rode numeros[1:10]. A lista só tem 5 elementos — dá IndexError?
#    Fatia é mais tolerante que índice: ela apenas para no fim.
#
# 2. Rode numeros[3:1]. O que vem? Por que uma fatia "de trás para
#    frente" devolve lista vazia em vez de erro?
#
# 3. Rode sum(["a", "b"]). Qual erro? sum só soma números.
