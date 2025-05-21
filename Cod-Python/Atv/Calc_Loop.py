#  Crie uma calculadora que execute em loop contínuo com as seguintes características:

# 1. O programa deve apresentar 5 opções:
#  - Soma
#  - Subtração
#  - Multiplicação
#  - Divisão
#  - Sair
# 2. O programa deve continuar executando até que o usuário escolha sair
# 3. Utilize a estrutura match-case para processar as escolhas
# 4. Implemente tratamento de erros para todas as entradas
# 5. Adicione a opção de sair do programa (opção 5)
# 6. O programa deve limpar a tela ou mostrar o menu novamente após cada operação
# 7. Use f-strings para mostrar os resultados das operações


def calculadora():
    print("=== Calculadora Simples ===")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    # Input da operação
    try:
        opcao = int(input("Escolha a operação (1-5): "))
        if opcao < 1 or opcao > 5:
            print("Operação inválida! Escolha entre 1 e 5.")
            return False
        if opcao == 5:
            print("Programa encerrado!")
            return True
    except ValueError:
        print("Entrada inválida! Digite um número.")
        return False

    # Input dos números
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida! Digite apenas números.")
        return False

    # Operações usando match case
    match opcao:
        case 1:
            resultado = num1 + num2
            print(f"Resultado: {num1} + {num2} = {resultado}")

        case 2:
            resultado = num1 - num2
            print(f"Resultado: {num1} - {num2} = {resultado}")

        case 3:
            resultado = num1 * num2
            print(f"Resultado: {num1} * {num2} = {resultado}")

        case 4:
            if num2 == 0:
                print("Erro: Divisão por zero não é permitida!")
                return False
            resultado = num1 / num2
            print(f"Resultado: {num1} / {num2} = {resultado}")

        case _:
            print("Operação inválida!")

    return False


# Executar a calculadora
if __name__ == "__main__":
    sair = False
    while not sair:
        sair = calculadora()
