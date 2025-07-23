"""
Exercício 19 - Multiplicação por Escalar

Objetivo: Criar um programa que multiplique cada elemento de uma matriz por um número.

Tarefas:
1. Criar uma matriz 3x3 com valores fornecidos pelo usuário
2. Solicitar um número (escalar) para multiplicação
3. Multiplicar cada elemento da matriz pelo escalar
4. Exibir a matriz original e o resultado

Exemplo:
Matriz:     Escalar: 2    Resultado:
[1 2 3]                   [2  4  6]
[4 5 6]        →         [8  10 12]
[7 8 9]                   [14 16 18]
"""

def criar_matriz():
    matriz = []
    print("Digite os valores para a matriz 3x3:")
    for i in range(3):
        linha = []
        for j in range(3):
            valor = int(input(f"Digite o valor para posição [{i}][{j}]: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz


def multiplicar_por_escalar(matriz, escalar):
    resultado = []
    for i in range(3):
        linha = []
        for j in range(3):
            linha.append(matriz[i][j] * escalar)
        resultado.append(linha)
    return resultado


def exibir_matriz(matriz):
    for linha in matriz:
        print(linha)


def main():
    # Criar matriz original
    print("Vamos criar a matriz 3x3")
    matriz_original = criar_matriz()

    # Solicitar o escalar
    escalar = int(input("\nDigite o número escalar para multiplicação: "))

    # Calcular o resultado
    matriz_resultado = multiplicar_por_escalar(matriz_original, escalar)

    # Exibir resultados
    print("\nMatriz Original:")
    exibir_matriz(matriz_original)

    print(f"\nEscalar: {escalar}")

    print("\nMatriz Resultado:")
    exibir_matriz(matriz_resultado)

if __name__ == "__main__":
    main()
