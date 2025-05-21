"""
Exercício 20 - Soma das Diagonais

Objetivo: Calcular e comparar a soma das diagonais principal e secundária.

Tarefas:
1. Criar uma matriz quadrada 4x4
2. Calcular a soma da diagonal principal (↘)
3. Calcular a soma da diagonal secundária (↙)
4. Determinar qual diagonal tem a maior soma
5. Exibir os elementos de cada diagonal
"""

# Criar matriz 4x4
matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# Função para imprimir a matriz de forma organizada


def imprimir_matriz(mat):
    for linha in mat:
        for elemento in linha:
            print(f"|{elemento:3d}|", end=" ")
        print()


# Calcular soma da diagonal principal
diagonal_principal = []
soma_principal = 0
for i in range(4):
    diagonal_principal.append(matriz[i][i])
    soma_principal += matriz[i][i]

# Calcular soma da diagonal secundária
diagonal_secundaria = []
soma_secundaria = 0
for i in range(4):
    diagonal_secundaria.append(matriz[i][3-i])
    soma_secundaria += matriz[i][3-i]
# Exibir resultados
print("\nMatriz:")
imprimir_matriz(matriz)

print(f"\nElementos da diagonal principal: {diagonal_principal}")
print(f"Soma da diagonal principal: {soma_principal}")

print(f"\nElementos da diagonal secundária: {diagonal_secundaria}")
print(f"Soma da diagonal secundária: {soma_secundaria}")

if soma_principal > soma_secundaria:
    print("\nA diagonal principal tem a maior soma")
elif soma_secundaria > soma_principal:
    print("\nA diagonal secundária tem a maior soma")
else:
    print("\nAs diagonais têm a mesma soma")
