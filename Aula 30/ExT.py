"""
Exercício  - Análise de Matriz
Desenvolva um programa que:
1. Crie uma matriz 4x4 com números aleatórios entre 0 e 50
2. Calcule e mostre:
   - A soma da diagonal principal
   - A soma da diagonal secundária
   - O maior valor de cada linha
3. Exiba a matriz de forma organizada
"""

import random


def criar_matriz(tamanho):
    return [[random.randint(0, 50) for _ in range(tamanho)] for _ in range(tamanho)]



def exibir_matriz(matriz):
    print("\nMatriz 4x4:")
    print("-" * 25)
    for linha in matriz:
        for num in linha:
            print(f"|{num:3d}|", end=" ")
        print()
    print("-" * 25)


def soma_diagonal_principal(matriz):
    return sum(matriz[i][i] for i in range(len(matriz)))


def soma_diagonal_secundaria(matriz):
    tamanho = len(matriz)
    return sum(matriz[i][tamanho-1-i] for i in range(tamanho))


def maiores_valores_linhas(matriz):
    return [max(linha) for linha in matriz]


# Programa principal
tamanho = 4
matriz = criar_matriz(tamanho)


# Exibe a matriz
exibir_matriz(matriz)

# Calcula e exibe os resultados
print(f"\nSoma da diagonal principal: {soma_diagonal_principal(matriz)}")
print(f"Soma da diagonal secundária: {soma_diagonal_secundaria(matriz)}")

# Exibe o maior valor de cada linha
maiores = maiores_valores_linhas(matriz)
for i, valor in enumerate(maiores):
    print(f"Maior valor da linha {i+1}: {valor}")
