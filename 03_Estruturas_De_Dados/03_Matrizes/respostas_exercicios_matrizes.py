"""
Respostas — Introdução a Matrizes e Soma de Matrizes

Apenas listas aninhadas (sem bibliotecas externas).
"""

# ============================================================
# EXERCÍCIO 1
# ============================================================
print("EXERCÍCIO 1")

# Passo 1: criar a matriz 2x2
matriz = [
    [5, 10],
    [15, 20],
]

# Passo 2: acessar os elementos pelo índice [linha][coluna]
print("Elemento na linha 0, coluna 1:", matriz[0][1])  # 10
print("Elemento na linha 1, coluna 0:", matriz[1][0])  # 15

# ============================================================
# EXERCÍCIO 2
# ============================================================
print("\nEXERCÍCIO 2")

# Passo 1: criar a matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# Passo 2: exibir a matriz antes da modificação
print("Antes:")
for linha in matriz:
    print(linha)

# Passo 3: modificar o elemento central
matriz[1][1] = 99

# Passo 4: exibir a matriz depois da modificação
print("Depois:")
for linha in matriz:
    print(linha)

# ============================================================
# EXERCÍCIO 3
# ============================================================
print("\nEXERCÍCIO 3")

# Passo 1: definir a matriz
matriz = [
    [2, 4, 6],
    [8, 10, 12],
]

# Passo 2: percorrer cada elemento com dois loops e ir acumulando
soma = 0
for i in range(len(matriz)):        # percorre as linhas
    for j in range(len(matriz[i])):  # percorre as colunas de cada linha
        soma = soma + matriz[i][j]  # adiciona o elemento atual à soma

# Passo 3: exibir o resultado
print("Soma de todos os elementos:", soma)  # 42

# ============================================================
# EXERCÍCIO 4
# ============================================================
print("\nEXERCÍCIO 4")

# Passo 1: criar a matriz de zeros com list comprehension
# Para cada linha i (0, 1, 2), cria uma lista com 3 zeros
matriz_zeros = [[0 for j in range(3)] for i in range(3)]

# Passo 2: exibir a matriz
print("Matriz 3x3 de zeros:")
for linha in matriz_zeros:
    print(linha)

# ============================================================
# EXERCÍCIO 5
# ============================================================
print("\nEXERCÍCIO 5")

# Passo 1: definir as duas matrizes
A = [
    [1, 0, 2],
    [3, 1, 0],
    [2, 4, 1],
]

B = [
    [3, 3, 1],
    [0, 2, 4],
    [1, 0, 3],
]

# Passo 2: criar a matriz resultado C somando elemento a elemento
# C[i][j] = A[i][j] + B[i][j]
C = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# Passo 3: exibir as matrizes
print("Matriz A:")
for linha in A:
    print(linha)

print("Matriz B:")
for linha in B:
    print(linha)

print("Matriz C = A + B:")
for linha in C:
    print(linha)

# ============================================================
# EXERCÍCIO 6
# ============================================================
print("\nEXERCÍCIO 6")

# Passo 1: definir a matriz 3x2
matriz = [
    [7, 14],
    [21, 28],
    [35, 42],
]

# Passo 2: percorrer e imprimir cada elemento com sua posição
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f"Elemento [{i}][{j}] =", matriz[i][j])

# ============================================================
# EXERCÍCIO 7
# ============================================================
print("\nEXERCÍCIO 7")

# Passo 1: definir as duas matrizes 2x4
A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
]

B = [
    [9, 8, 7, 6],
    [5, 4, 3, 2],
]

# Passo 2: somar elemento a elemento
C = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# Passo 3: exibir o resultado
print("Matriz C = A + B:")
for linha in C:
    print(linha)

# ============================================================
# EXERCÍCIO 8
# ============================================================
print("\nEXERCÍCIO 8")

# Passo 1: definir a matriz
matriz = [
    [3, 17, 5],
    [42, 8, 11],
    [6, 29, 4],
]

# Passo 2: assumir que o primeiro elemento é o maior
maior = matriz[0][0]

# Passo 3: comparar cada elemento com o maior encontrado até agora
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] > maior:
            maior = matriz[i][j]  # atualiza se encontrar um maior

# Passo 4: exibir o resultado
print("Maior elemento:", maior)  # 42

# ============================================================
# EXERCÍCIO 9
# ============================================================
print("\nEXERCÍCIO 9")

# Passo 1: definir a matriz
matriz = [
    [1, 6, 3],
    [8, 2, 7],
    [4, 9, 5],
]

# Passo 2: contar quantos elementos são maiores que 5
contagem = 0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] > 5:
            contagem = contagem + 1  # incrementa o contador

# Passo 3: exibir o resultado
print("Elementos maiores que 5:", contagem)  # 4

# ============================================================
# EXERCÍCIO 10
# ============================================================
print("\nEXERCÍCIO 10")

# Passo 1: definir as duas matrizes (iguais neste caso)
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

B = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# Passo 2: calcular C = A + B
C = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# Passo 3: calcular a soma de todos os elementos de A
soma_A = 0
for i in range(len(A)):
    for j in range(len(A[i])):
        soma_A = soma_A + A[i][j]

# Passo 4: calcular a soma de todos os elementos de C
soma_C = 0
for i in range(len(C)):
    for j in range(len(C[i])):
        soma_C = soma_C + C[i][j]

# Passo 5: verificar se C é o dobro de A
print("Soma de A:", soma_A)         # 45
print("Soma de C:", soma_C)         # 90
print("C é o dobro de A?", soma_C == soma_A * 2)  # True
