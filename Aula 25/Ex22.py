"""
Exercício 4 - Matriz Espelhada

Objetivo: Criar uma matriz e gerar sua versão espelhada horizontalmente.

Tarefas:
1. Criar uma matriz 3x4 com valores fornecidos pelo usuário
2. Gerar uma nova matriz espelhada horizontalmente (invertendo a ordem das colunas)
3. Exibir ambas as matrizes lado a lado
4. Verificar se o espelhamento foi feito corretamente

Exemplo:
Original (3x4):    Espelhada (3x4):
[1  2  3  4]      [4  3  2  1]
[5  6  7  8]  →   [8  7  6  5]
[9 10 11 12]      [12 11 10 9]
"""


def criar_matriz():
    matriz = []
    print("Digite os valores para a matriz 3x4:")
    for i in range(3):
        linha = []
        for j in range(4):
            valor = int(input(f"Digite o valor para posição [{i}][{j}]: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz


def espelhar_matriz(matriz):
    matriz_espelhada = []
    for linha in matriz:
        matriz_espelhada.append(linha[::-1])
    return matriz_espelhada


def exibir_matrizes(original, espelhada):
    print("\nMatriz Original:")
    for linha in original:
        print([f"{num:2d}" for num in linha])

    print("\nMatriz Espelhada:")
    for linha in espelhada:
        print([f"{num:2d}" for num in linha])


def main():
    matriz_original = criar_matriz()
    matriz_espelhada = espelhar_matriz(matriz_original)
    exibir_matrizes(matriz_original, matriz_espelhada)


if __name__ == "__main__":
    main()
