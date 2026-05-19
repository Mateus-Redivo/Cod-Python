"""
Exercício 26 - Multiplicação por Escalar com Menu Interativo

Objetivo: Multiplicar cada elemento de uma matriz por um número (escalar),
com uma interface de menu que permite ao usuário escolher as operações.

Conceito:
    Extensão do exercício anterior (05_Multiplicacao_Escalar.py):
    - O usuário define as dimensões da matriz (não fixadas em 3x3)
    - Um menu interativo guia as operações disponíveis
    - A matriz pode ser multiplicada por escalar múltiplas vezes

    ATENÇÃO: ao multiplicar por escalar, a matriz atual é atualizada.
    Multiplicar duas vezes equivale a aplicar o produto dos escalares.
"""


def criar_matriz():
    """Lê dimensões e valores do usuário, retorna a matriz criada."""
    linhas = int(input("Número de linhas: "))
    colunas = int(input("Número de colunas: "))

    if linhas <= 0 or colunas <= 0:
        print("  Erro: dimensões devem ser maiores que zero!")
        return None

    matriz = []
    print(f"\nDigite os valores para a matriz {linhas}x{colunas}:")
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            valor = int(input(f"  Posição [{i}][{j}]: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz


def multiplicar_por_escalar(matriz, escalar):
    """Retorna nova matriz com cada elemento multiplicado pelo escalar."""
    resultado = []
    for i in range(len(matriz)):
        linha = []
        for j in range(len(matriz[0])):
            linha.append(matriz[i][j] * escalar)
        resultado.append(linha)
    return resultado


def exibir_matriz(matriz):
    """Exibe a matriz com alinhamento de colunas, ou mensagem se vazia."""
    if not matriz:
        print("  (nenhuma matriz criada)")
        return
    for linha in matriz:
        print("  " + "  ".join(f"{num:4d}" for num in linha))


def mostrar_menu():
    print("\n=== Menu de Operações ===")
    print("  1. Criar nova matriz")
    print("  2. Multiplicar matriz por escalar")
    print("  3. Exibir matriz atual")
    print("  4. Sair")
    return input("Escolha uma opção: ").strip()


def main():
    matriz_atual = None

    while True:
        opcao = mostrar_menu()

        match opcao:
            case "1":
                print("\n--- Criando nova matriz ---")
                matriz_atual = criar_matriz()
                if matriz_atual:
                    print("\nMatriz criada:")
                    exibir_matriz(matriz_atual)

            case "2":
                if matriz_atual is None:
                    print("\n  Primeiro crie uma matriz (opção 1)!")
                else:
                    print("\nMatriz atual:")
                    exibir_matriz(matriz_atual)
                    escalar = int(input("\nDigite o escalar: "))
                    matriz_atual = multiplicar_por_escalar(matriz_atual, escalar)
                    print(f"\nMatriz após multiplicar por {escalar}:")
                    exibir_matriz(matriz_atual)

            case "3":
                print("\nMatriz atual:")
                exibir_matriz(matriz_atual)

            case "4":
                if matriz_atual is not None:
                    print("\nMatriz final:")
                    exibir_matriz(matriz_atual)
                print("\nEncerrando o programa.")
                break

            case _:
                print("\n  Opção inválida! Escolha entre 1 e 4.")


if __name__ == "__main__":
    main()
