"""
Análise de Matriz

Objetivo: Analisar uma matriz quadrada 4x4 calculando:
  1. A soma da diagonal principal
  2. A soma da diagonal secundária
  3. O maior valor de cada linha

Conceito — Diagonais de uma matriz quadrada N x N:

    Diagonal PRINCIPAL: elementos onde coluna == linha  →  A[i][i]
    Diagonal SECUNDÁRIA: elementos onde coluna + linha == N-1  →  A[i][N-1-i]

    Exemplo em uma matriz 4x4 (P = principal, S = secundária, B = ambas):

         col0  col1  col2  col3
    lin0 [  P     ·     ·     S  ]
    lin1 [  ·     P     S     ·  ]
    lin2 [  ·     S     P     ·  ]
    lin3 [  S     ·     ·     P  ]

    (quando N é ímpar, o elemento central pertence às duas diagonais)
"""
import random

# --- Criação da matriz 4x4 com valores aleatórios ---
tamanho = 4
matriz = [[random.randint(0, 50) for _ in range(tamanho)]
          for _ in range(tamanho)]

print("=== Matriz 4x4 (valores aleatórios 0–50) ===")
separador = "  +" + "-----+" * tamanho
print(separador)
for linha in matriz:
    print("  |" + "".join(f" {num:3d} |" for num in linha))
print(separador)

# --- Diagonais ---
soma_principal = sum(matriz[i][i] for i in range(tamanho))
soma_secundaria = sum(matriz[i][tamanho - 1 - i] for i in range(tamanho))

print(f"\nSoma da diagonal principal  (↘): {soma_principal}")
print(f"Soma da diagonal secundária (↙): {soma_secundaria}")

# Elementos de cada diagonal para visualização
print("\nElementos da diagonal principal  (A[i][i]):")
for i in range(tamanho):
    print(f"  A[{i}][{i}] = {matriz[i][i]}")

print("\nElementos da diagonal secundária (A[i][N-1-i]):")
for i in range(tamanho):
    j = tamanho - 1 - i
    print(f"  A[{i}][{j}] = {matriz[i][j]}")

# --- Maior valor por linha ---
print("\nMaior valor por linha:")
for i, linha in enumerate(matriz):
    print(f"  Linha {i}: {max(linha)}")
