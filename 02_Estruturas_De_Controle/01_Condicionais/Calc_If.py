# Desenvolva uma calculadora utilizando estruturas condicionais if-elif com os seguintes requisitos:

# 1. O programa deve oferecer as mesmas 4 operações básicas:
#  - Soma
#  - Subtração
#  - Multiplicação
# - Divisão
# 2. Utilize if-elif para controle do fluxo do programa
# 3. Implemente validações para:
#  - Entradas numéricas válidas
#  - Prevenção de divisão por zero
#  - Opções de menu dentro do intervalo permitido
# 4. Formate a saída usando f-strings para mostrar a operação completa e seu resultado


def calculadora():
    print("=== Calculadora Simples ===")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    # Input da operação
    try: 
        opcao = int(input("Escolha a operação (1-4): "))
        if opcao < 1 or opcao > 4:
            print("Operação inválida! Escolha entre 1 e 4.")
            return
    except ValueError:
        print("Entrada inválida! Digite um número.")
        return

    # Input dos números
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida! Digite apenas números.")
        return

    # Operações
    if opcao == 1:
        resultado = num1 + num2
        print(f"Resultado: {num1} + {num2} = {resultado}")

    elif opcao == 2:
        resultado = num1 - num2
        print(f"Resultado: {num1} - {num2} = {resultado}")

    elif opcao == 3:
        resultado = num1 * num2
        print(f"Resultado: {num1} * {num2} = {resultado}")

    elif opcao == 4:
        if num2 == 0:
            print("Erro: Divisão por zero não é permitida!")
            return
        resultado = num1 / num2
        print(f"Resultado: {num1} / {num2} = {resultado}")


# Executar a calculadora
if __name__ == "__main__":
    calculadora()
