"""
Respostas — Introdução a Matrizes e Soma de Matrizes

Apenas listas aninhadas (sem bibliotecas externas).
"""

# ============================================================
# EXERCÍCIO 1
# ============================================================
print("=" * 50)
print("EXERCÍCIO 1")
print("=" * 50)

matriz = [
    [5, 10],
    [15, 20],
]

print(f"Elemento [0][1] = {matriz[0][1]}")
print(f"Elemento [1][0] = {matriz[1][0]}")

# ============================================================
# EXERCÍCIO 2
# ============================================================
print("\n" + "=" * 50)
print("EXERCÍCIO 2")
print("=" * 50)

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print("\nAntes:")
for linha in matriz:
    print("  " + "  ".join(f"{num:4d}" for num in linha))

matriz[1][1] = 99

print("\nDepois:")
for linha in matriz:
    print("  " + "  ".join(f"{num:4d}" for num in linha))

# ============================================================
# EXERCÍCIO 3
# ============================================================
print("\n" + "=" * 50)
print("EXERCÍCIO 3")
print("=" * 50)

matriz = [
    [2, 4, 6],
    [8, 10, 12],
]

soma = 0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        soma += matriz[i][j]

print(f"Soma de todos os elementos: {soma}")

# ============================================================
# EXERCÍCIO 4
# ============================================================
print("\n" + "=" * 50)
print("EXERCÍCIO 4")
print("=" * 50)

matriz_zeros = [[0 for j in range(3)] for i in range(3)]

print("Matriz 3x3 de zeros:")
for linha in matriz_zeros:
    print("  " + "  ".join(f"{num:4d}" for num in linha))

# ============================================================
# EXERCÍCIO 5
# ============================================================
print("\n" + "=" * 50)
print("EXERCÍCIO 5")
print("=" * 50)

A = [[1, 0, 2],
     [3, 1, 0],
     [2, 4, 1]]

B = [[3, 3, 1],
     [0, 2, 4],
     [1, 0, 3]]

C = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

print("\nMatriz A:")
for linha in A:
    print("  " + "  ".join(f"{num:4d}" for num in linha))

print("\nMatriz B:")
for linha in B:
    print("  " + "  ".join(f"{num:4d}" for num in linha))

print("\nMatriz C = A + B:")
for linha in C:
    print("  " + "  ".join(f"{num:4d}" for num in linha))

# ============================================================
# EXERCÍCIO 6
# ============================================================
print("\n" + "=" * 50)
print("EXERCÍCIO 6")
print("=" * 50)

matriz = [
    [7, 14],
    [21, 28],
    [35, 42],
]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f"  Elemento [{i}][{j}] = {matriz[i][j]}")

# ============================================================
# EXERCÍCIO 7
# ============================================================
print("\n" + "=" * 50)
print("EXERCÍCIO 7")
print("=" * 50)

A = [[1, 2, 3, 4],
     [5, 6, 7, 8]]

B = [[9, 8, 7, 6],
     [5, 4, 3, 2]]

C = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

print("Matriz C = A + B (2x4):")
for linha in C:
    print("  " + "  ".join(f"{num:4d}" for num in linha))

# ============================================================
# EXERCÍCIO 8
# ============================================================
print("\n" + "=" * 50)
print("EXERCÍCIO 8")
print("=" * 50)

matriz = [
    [3, 17, 5],
    [42, 8, 11],
    [6, 29, 4],
]

maior = matriz[0][0]
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] > maior:
            maior = matriz[i][j]

print(f"Maior elemento: {maior}")

# ============================================================
# EXERCÍCIO 9
# ============================================================
print("\n" + "=" * 50)
print("EXERCÍCIO 9")
print("=" * 50)

matriz = [
    [1, 6, 3],
    [8, 2, 7],
    [4, 9, 5],
]

contagem = 0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] > 5:
            contagem += 1

print(f"Elementos maiores que 5: {contagem}")

# ============================================================
# EXERCÍCIO 10
# ============================================================
print("\n" + "=" * 50)
print("EXERCÍCIO 10")
print("=" * 50)

A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

C = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

soma_A = 0
for i in range(len(A)):
    for j in range(len(A[i])):
        soma_A += A[i][j]

soma_C = 0
for i in range(len(C)):
    for j in range(len(C[i])):
        soma_C += C[i][j]

print(f"Soma de A: {soma_A}")
print(f"Soma de C: {soma_C}")
print(f"C é o dobro de A? {soma_C == soma_A * 2}")
