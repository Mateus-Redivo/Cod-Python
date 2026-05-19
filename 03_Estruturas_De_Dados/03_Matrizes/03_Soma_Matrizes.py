"""
Exercício 17 - Soma de Matrizes

Objetivo: Implementar a soma de duas matrizes 2x3 utilizando list comprehension.

Conceito:
    Na soma de matrizes, somamos os elementos que estão na MESMA posição.
    Por isso, só é possível somar matrizes com as mesmas dimensões (M x N).

    Regra:  C[i][j] = A[i][j] + B[i][j]

    Exemplo com matrizes 2x3:

    A:               B:               C = A + B:
    [ 1   2   3 ]    [ 5   6   7 ]    [  6   8  10 ]
    [ 3   4   5 ]    [ 7   8   9 ]    [ 10  12  14 ]

Tarefas:
1. Criar duas matrizes A e B de dimensão 2x3
2. Realizar a soma elemento por elemento usando list comprehension
3. Exibir o passo a passo da operação
4. Exibir o resultado final
"""


def exibir_matriz(nome, matriz):
    """Exibe a matriz com rótulo e alinhamento de colunas."""
    print(f"\nMatriz {nome}:")
    for linha in matriz:
        print("  " + "  ".join(f"{num:4d}" for num in linha))


# --- Definição das matrizes (2 linhas x 3 colunas) ---
A = [[1, 2, 3],
     [3, 4, 5]]

B = [[5, 6, 7],
     [7, 8, 9]]

exibir_matriz("A", A)
exibir_matriz("B", B)

# --- Soma usando list comprehension ---
# Loop externo (i): percorre as linhas
# Loop interno (j): percorre as colunas de cada linha
C = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

exibir_matriz("C = A + B", C)

# --- Passo a passo da soma ---
print("\n--- Passo a passo ---")
for i in range(len(A)):
    for j in range(len(A[0])):
        resultado = A[i][j] + B[i][j]
        print(f"  C[{i}][{j}] = A[{i}][{j}] + B[{i}][{j}] = {A[i][j]} + {B[i][j]} = {resultado}")
