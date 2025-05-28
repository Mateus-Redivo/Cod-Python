import random

# Seção 2: Matrizes e Listas

# Criação de Matriz: matriz 3x3 com números aleatórios entre 1 e 100


def criar_matriz():
    matriz = [[random.randint(1, 100) for _ in range(3)] for _ in range(3)]
    return matriz

# Manipulação de Elementos: acessa e modifica elementos específicos em uma matriz


def manipular_elementos(matriz):
    print("Matriz original:")
    for linha in matriz:
        print(linha)

    # Acessando elemento na posição [1][1] (centro da matriz 3x3)
    elemento_central = matriz[1][1]
    print(f"\nElemento central [1][1]: {elemento_central}")

    # Modificando o elemento na posição [0][2] (canto superior direito)
    matriz[0][2] = 999
    print("\nMatriz após modificação:")
    for linha in matriz:
        print(linha)

    return matriz

# Soma Diagonal: calcula a soma da diagonal principal


def soma_diagonal(matriz):
    soma = sum(matriz[i][i] for i in range(len(matriz)))
    return soma

# Transposição de Matriz: troca linhas por colunas


def transpor_matriz(matriz):
    transposta = [[matriz[j][i]
                   for j in range(len(matriz))] for i in range(len(matriz[0]))]
    return transposta


# Demonstração das funções
if __name__ == "__main__":
    print("=== Demonstração da Seção 2: Matrizes e Listas ===\n")

    # Criar matriz
    print("1. Criação de Matriz:")
    matriz = criar_matriz()
    for linha in matriz:
        print(linha)
    print()

    # Manipular elementos
    print("2. Manipulação de Elementos:")
    matriz = manipular_elementos(matriz)
    print()

    # Soma diagonal
    print("3. Soma da Diagonal Principal:")
    soma = soma_diagonal(matriz)
    print(f"A soma da diagonal principal é: {soma}")
    print()

    # Transposição
    print("4. Transposição de Matriz:")
    transposta = transpor_matriz(matriz)
    print("Matriz original:")
    for linha in matriz:
        print(linha)
    print("Matriz transposta:")
    for linha in transposta:
        print(linha) 
