"""
Multiplicação por Escalar com Menu Interativo

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


matriz_atual = None

while True:
    # --- Menu ---
    print("\n=== Menu de Operações ===")
    print("  1. Criar nova matriz")
    print("  2. Multiplicar matriz por escalar")
    print("  3. Exibir matriz atual")
    print("  4. Sair")
    opcao = input("Escolha uma opção: ").strip()

    match opcao:
        case "1":
            print("\n--- Criando nova matriz ---")
            linhas = int(input("Número de linhas: "))
            colunas = int(input("Número de colunas: "))
            if linhas <= 0 or colunas <= 0:
                print("  Erro: dimensões devem ser maiores que zero!")
            else:
                matriz_atual = []
                print(f"\nDigite os valores para a matriz {linhas}x{colunas}:")
                for i in range(linhas):
                    linha = []
                    for j in range(colunas):
                        valor = int(input(f"  Posição [{i}][{j}]: "))
                        linha.append(valor)
                    matriz_atual.append(linha)
                print("\nMatriz criada:")
                for linha in matriz_atual:
                    print("  " + "  ".join(f"{num:4d}" for num in linha))

        case "2":
            if matriz_atual is None:
                print("\n  Primeiro crie uma matriz (opção 1)!")
            else:
                print("\nMatriz atual:")
                for linha in matriz_atual:
                    print("  " + "  ".join(f"{num:4d}" for num in linha))
                escalar = int(input("\nDigite o escalar: "))
                resultado = []
                for i in range(len(matriz_atual)):
                    linha = []
                    for j in range(len(matriz_atual[0])):
                        linha.append(matriz_atual[i][j] * escalar)
                    resultado.append(linha)
                matriz_atual = resultado
                print(f"\nMatriz após multiplicar por {escalar}:")
                for linha in matriz_atual:
                    print("  " + "  ".join(f"{num:4d}" for num in linha))

        case "3":
            print("\nMatriz atual:")
            if matriz_atual is None:
                print("  (nenhuma matriz criada)")
            else:
                for linha in matriz_atual:
                    print("  " + "  ".join(f"{num:4d}" for num in linha))

        case "4":
            if matriz_atual is not None:
                print("\nMatriz final:")
                for linha in matriz_atual:
                    print("  " + "  ".join(f"{num:4d}" for num in linha))
            print("\nEncerrando o programa.")
            break

        case _:
            print("\n  Opção inválida! Escolha entre 1 e 4.")
