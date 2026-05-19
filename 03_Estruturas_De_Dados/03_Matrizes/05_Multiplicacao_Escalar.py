"""
Multiplicação por Escalar

Objetivo: Multiplicar cada elemento de uma matriz por um número (escalar).

Conceito:
    Um escalar é um número simples (sem direção ou dimensão).
    Na multiplicação por escalar, CADA elemento da matriz é multiplicado
    pelo mesmo valor.

    Fórmula:  (k × A)[i][j] = k × A[i][j]

    Exemplo com escalar k = 2:
    A:                k × A:
    [  1   2   3 ]    [  2   4   6 ]
    [  4   5   6 ]  → [  8  10  12 ]
    [  7   8   9 ]    [ 14  16  18 ]

Tarefas:
1. Criar uma matriz 3x3 com valores fornecidos pelo usuário
2. Solicitar um escalar para multiplicação
3. Multiplicar cada elemento da matriz pelo escalar
4. Exibir a matriz original e o resultado
"""

print("=== Multiplicação de Matriz por Escalar ===\n")

# --- Leitura da matriz 3x3 ---
matriz_original = []
print("Digite os valores para a matriz 3x3:")
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"  Posição [{i}][{j}]: "))
        linha.append(valor)
    matriz_original.append(linha)

escalar = int(input("\nDigite o escalar: "))

# --- Multiplicação por escalar ---
matriz_resultado = []
for i in range(len(matriz_original)):
    linha = []
    for j in range(len(matriz_original[i])):
        linha.append(matriz_original[i][j] * escalar)
    matriz_resultado.append(linha)

# --- Exibição dos resultados ---
print("\nMatriz Original:")
for linha in matriz_original:
    print("  " + "  ".join(f"{num:4d}" for num in linha))

print(f"\nMatriz × {escalar}:")
for linha in matriz_resultado:
    print("  " + "  ".join(f"{num:4d}" for num in linha))
