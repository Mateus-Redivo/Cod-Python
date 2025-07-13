# Código para criação e manipulação de elementos de uma matriz

def criar_matriz():
    # Solicita as dimensões da matriz
    linhas = int(input("Digite o número de linhas: "))
    colunas = int(input("Digite o número de colunas: "))

    # Cria a matriz vazia
    matriz = []

    # Preenche a matriz com valores informados pelo usuário
    print("\nDigite os valores para a matriz:")
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            valor = int(input(f"Digite o valor para posição [{i}][{j}]: "))
            linha.append(valor)
        matriz.append(linha)

    return matriz


def mostrar_matriz(matriz):
    print("\nSua matriz:")
    for linha in matriz:
        for elemento in linha:
            print(f"{elemento:4}", end="")
        print()


def alterar_elemento(matriz, linha, coluna, valor):
    """Altera o valor de um elemento da matriz.
    Verifica se a posição especificada é válida antes de realizar a alteração.
    """
    if 0 <= linha < len(matriz) and 0 <= coluna < len(matriz[0]):
        matriz[linha][coluna] = valor
    else:
        # Exibe uma mensagem de erro se a posição for inválida.
        print("Posição inválida!")


def somar_linhas(matriz):
    """Retorna uma lista com a soma de cada linha da matriz.
    Cada elemento da lista corresponde à soma dos elementos de uma linha.
    """
    return [sum(linha) for linha in matriz]


def somar_colunas(matriz):
    """Retorna uma lista com a soma de cada coluna da matriz.
    Cada elemento da lista corresponde à soma dos elementos de uma coluna.
    """
    return [sum(matriz[i][j] for i in range(len(matriz))) for j in range(len(matriz[0]))]


# Programa principal
matriz = criar_matriz()
mostrar_matriz(matriz)

# Altera o elemento na posição (1, 1) para o valor 5.
alterar_elemento(matriz, 1, 1, -1)
print("\nMatriz após alteração:")  # Exibe a matriz após a alteração.
mostrar_matriz(matriz)

# Calcula e exibe a soma de cada linha.
print("\nSoma das linhas:", somar_linhas(matriz))
# Calcula e exibe a soma de cada coluna.
print("Soma das colunas:", somar_colunas(matriz))
