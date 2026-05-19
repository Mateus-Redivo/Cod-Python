"""
Exercício 16 - Introdução a Matrizes

Objetivo: Criar, acessar e modificar elementos de uma matriz simples.

Conceito:
    Uma matriz é uma tabela de valores organizada em LINHAS e COLUNAS.
    Em Python, representamos matrizes como listas de listas (listas aninhadas).

    Visualização de uma matriz 3x3 com índices:

              col 0   col 1   col 2
    linha 0 [   1,      2,      3   ]
    linha 1 [   4,      5,      6   ]
    linha 2 [   7,      8,      9   ]

    Para acessar um elemento: matriz[linha][coluna]
    Exemplos:
        matriz[0][0] → 1    (linha 0, coluna 0)
        matriz[1][2] → 6    (linha 1, coluna 2)
        matriz[2][1] → 8    (linha 2, coluna 1)

Tarefas:
1. Criar uma matriz 3x3 com valores numéricos sequenciais
2. Acessar elementos específicos da matriz
3. Modificar o valor de um elemento
4. Calcular a soma de todos os elementos
"""


def exibir_matriz(matriz):
    """Exibe a matriz com alinhamento de colunas."""
    for linha in matriz:
        print("  " + "  ".join(f"{num:4d}" for num in linha))


# --- 1. Criação da matriz 3x3 ---
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print("=== Matriz Original (3x3) ===")
exibir_matriz(matriz)

# --- 2. Acessando elementos por [linha][coluna] ---
print("\n--- Acessando elementos ---")
print(f"  matriz[0][0] = {matriz[0][0]}  (linha 0, coluna 0)")
print(f"  matriz[1][2] = {matriz[1][2]}  (linha 1, coluna 2)")
print(f"  matriz[2][1] = {matriz[2][1]}  (linha 2, coluna 1)")

# --- 3. Modificando um elemento ---
print("\n--- Modificando matriz[0][0]: de 1 para 10 ---")
matriz[0][0] = 10

print("\n=== Matriz Após Modificação ===")
exibir_matriz(matriz)

# --- 4. Calculando a soma com loop aninhado ---
soma = 0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        soma += matriz[i][j]

print(f"\nSoma de todos os elementos: {soma}")
