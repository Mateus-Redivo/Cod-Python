"""
Exercício 26 - Multiplicação por Escalar com Menu Interativo

Objetivo: Criar um programa que multiplique cada elemento de uma matriz por um número,
com interface de menu para o usuário.
"""


def criar_matriz():
    linhas = int(input("Digite o número de linhas da matriz: "))
    colunas = int(input("Digite o número de colunas da matriz: "))

    if linhas <= 0 or colunas <= 0:
        print("Erro: As dimensões devem ser maiores que zero!")
        return None

    matriz = []
    print(f"\nDigite os valores para a matriz {linhas}x{colunas}:")
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            valor = int(input(f"Digite o valor para posição [{i}][{j}]: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz


def multiplicar_por_escalar(matriz, escalar):
    if not matriz:
        return None
    resultado = []
    for i in range(3):
        linha = []
        for j in range(3):
            linha.append(matriz[i][j] * escalar)
        resultado.append(linha)
    return resultado


def exibir_matriz(matriz):
    if not matriz:
        print("A matriz está vazia!")
        return
    for linha in matriz:
        print(linha)


def mostrar_menu():
    print("\n=== Menu de Operações ===")
    print("1. Criar nova matriz")
    print("2. Multiplicar matriz por escalar")
    print("3. Exibir matriz atual")
    print("4. Sair")
    return input("Escolha uma opção: ")


def main():
    matriz_atual = None
    
    while True:
        if matriz_atual is not None:
            print("\nMatriz atual:")
            exibir_matriz(matriz_atual)

        opcao = mostrar_menu()

        match opcao:
            case "1":
                print("\nCriando nova matriz...")
                matriz_atual = criar_matriz()
                print("\nMatriz criada com sucesso!")
                print("\nNova matriz:")
                exibir_matriz(matriz_atual)

            case "2":
                if matriz_atual is None:
                    print("\nERRO: Primeiro crie uma matriz (opção 1)!")
                else:
                    print("\nMatriz atual para multiplicação:")
                    exibir_matriz(matriz_atual)
                    escalar = int(
                        input("\nDigite o número escalar para multiplicação: "))
                    matriz_atual = multiplicar_por_escalar(
                        matriz_atual, escalar)
                    print("\nResultado da multiplicação:")
                    exibir_matriz(matriz_atual)

            case "3":
                print("\nMatriz atual:")
                exibir_matriz(matriz_atual)

            case "4":
                if matriz_atual is not None:
                    print("\nMatriz final:")
                    exibir_matriz(matriz_atual)
                print("\nEncerrando o programa...")
                break

            case _:
                print("\nOpção inválida! Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()
