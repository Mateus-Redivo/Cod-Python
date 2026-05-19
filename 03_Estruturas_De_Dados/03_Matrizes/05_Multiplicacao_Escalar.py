"""
Exercício 19 - Multiplicação por Escalar

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


def criar_matriz():
    """Lê os valores do usuário e retorna uma matriz 3x3."""
    matriz = []
    print("Digite os valores para a matriz 3x3:")
    for i in range(3):
        linha = []
        for j in range(3):
            valor = int(input(f"  Posição [{i}][{j}]: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz


def multiplicar_por_escalar(matriz, escalar):
    """Retorna uma nova matriz com cada elemento multiplicado pelo escalar."""
    resultado = []
    for i in range(len(matriz)):
        linha = []
        for j in range(len(matriz[i])):
            linha.append(matriz[i][j] * escalar)
        resultado.append(linha)
    return resultado


def exibir_matriz(matriz):
    """Exibe a matriz com alinhamento de colunas."""
    for linha in matriz:
        print("  " + "  ".join(f"{num:4d}" for num in linha))


def main():
    print("=== Multiplicação de Matriz por Escalar ===\n")

    matriz_original = criar_matriz()
    escalar = int(input("\nDigite o escalar: "))

    matriz_resultado = multiplicar_por_escalar(matriz_original, escalar)

    print("\nMatriz Original:")
    exibir_matriz(matriz_original)

    print(f"\nMatriz × {escalar}:")
    exibir_matriz(matriz_resultado)


if __name__ == "__main__":
    main()
