"""
Módulo 09 — Matrizes
Exemplo 03: somando linhas, colunas e diagonais

Este arquivo mostra:
  - por que somar linha é fácil e somar coluna dá trabalho
  - as duas diagonais
  - o total geral

Como executar:
  python 03_somas.py
"""

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print("Matriz:")
for linha in matriz:
    print("  " + "".join(f"{v:4d}" for v in linha))
print()


# --- Linha: fácil, porque ela JÁ é uma lista -------------------------
print("Soma de cada linha:")
for indice in range(len(matriz)):
    print(f"  linha {indice}: {sum(matriz[indice])}")
print()


# --- Coluna: dá trabalho, porque ela não existe como lista -----------
# A coluna está espalhada: um elemento em cada linha.
print("Soma de cada coluna:")
for coluna in range(len(matriz[0])):
    total = 0
    for linha in range(len(matriz)):
        total += matriz[linha][coluna]      # o índice FIXO é o segundo
    print(f"  coluna {coluna}: {total}")
print()


# --- Diagonal principal: onde linha == coluna ------------------------
diagonal_principal = 0
for i in range(len(matriz)):
    diagonal_principal += matriz[i][i]

print(f"Diagonal principal (1, 5, 9):  {diagonal_principal}")


# --- Diagonal secundária: da direita para a esquerda -----------------
diagonal_secundaria = 0
tamanho = len(matriz)
for i in range(tamanho):
    diagonal_secundaria += matriz[i][tamanho - 1 - i]

print(f"Diagonal secundária (3, 5, 7): {diagonal_secundaria}")
print()


# --- Total geral -----------------------------------------------------
total = 0
for linha in matriz:
    total += sum(linha)

print(f"Total de todos os elementos: {total}")
print(f"Maior elemento: {max(max(linha) for linha in matriz)}")


# --- Experimento ---------------------------------------------------
# 1. No laço da coluna, troque matriz[linha][coluna] por
#    matriz[coluna][linha]. Os números mudam: você passou a somar as
#    linhas de novo, com outro nome.
#
# 2. Na diagonal secundária, entenda o "tamanho - 1 - i":
#    com i=0 pega [0][2], com i=1 pega [1][1], com i=2 pega [2][0].
#    Escreva os três à mão antes de rodar.
#
# 3. Use uma matriz 2x3 (não quadrada) e rode. As diagonais ainda
#    fazem sentido? Diagonal só existe em matriz quadrada.
