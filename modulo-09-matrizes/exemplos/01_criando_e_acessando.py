"""
Módulo 09 — Matrizes
Exemplo 01: criando e acessando

Este arquivo mostra:
  - a matriz como lista de listas
  - o acesso com dois índices: [linha][coluna]
  - as dimensões, e por que len() conta linhas

Como executar:
  python 01_criando_e_acessando.py
"""

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print("            col 0   col 1   col 2")
print(f"  linha 0 [   {matriz[0][0]}  ,    {matriz[0][1]}  ,    {matriz[0][2]}   ]")
print(f"  linha 1 [   {matriz[1][0]}  ,    {matriz[1][1]}  ,    {matriz[1][2]}   ]")
print(f"  linha 2 [   {matriz[2][0]}  ,    {matriz[2][1]}  ,    {matriz[2][2]}   ]")
print()

# --- Dois índices: linha primeiro, coluna depois ---------------------
print(f"matriz[0][0] = {matriz[0][0]}   (linha 0, coluna 0)")
print(f"matriz[1][2] = {matriz[1][2]}   (linha 1, coluna 2)")
print(f"matriz[2][1] = {matriz[2][1]}   (linha 2, coluna 1)")
print()

# Trocar a ordem não dá erro — dá o elemento ERRADO.
print(f"matriz[1][2] = {matriz[1][2]}  mas  matriz[2][1] = {matriz[2][1]}")
print()

# --- Um índice só devolve a LINHA inteira ----------------------------
print(f"matriz[1]    = {matriz[1]}   <- a linha inteira, que é uma lista")
print(f"matriz[1][2] = {matriz[1][2]}          <- o elemento 2 dessa lista")
print()

# --- Dimensões -------------------------------------------------------
print(f"len(matriz)     = {len(matriz)}   quantas LINHAS")
print(f"len(matriz[0])  = {len(matriz[0])}   quantas COLUNAS")
print(f"total de elementos = {len(matriz) * len(matriz[0])}")
print()
print("Repare: len(matriz) de uma 3x3 dá 3, não 9.")
print()

# --- Alterar um elemento ---------------------------------------------
matriz[1][1] = 50
print(f"após matriz[1][1] = 50:  {matriz}")


# --- Experimento ---------------------------------------------------
# 1. Rode print(matriz[3][0]). Qual erro? E print(matriz[0][3])?
#    Os dois são IndexError, mas por motivos diferentes — um estourou
#    nas linhas, o outro nas colunas.
#
# 2. Rode print(matriz[0][0][0]). O erro diz "'int' object is not
#    subscriptable": você pediu um terceiro nível que não existe.
#
# 3. Crie uma matriz 2x4 (duas linhas, quatro colunas) e confira o que
#    len(matriz) e len(matriz[0]) devolvem.
