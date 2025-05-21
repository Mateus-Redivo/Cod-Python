# Implemente uma calculadora simples utilizando a estrutura match-case do Python 
# 3.10+ com as seguintes especificações:

# 1. O programa deve apresentar um menu com 4 operações básicas:
#  - Soma
#  - Subtração
#  - Multiplicação
#  - Divisão
# 2. O usuário deve poder escolher a operação através de números (1-4)
# 3. O programa deve solicitar dois números para realizar a operação
# 4. Implemente tratamento de erros para:
#  - Entradas não numéricas
#  - Divisão por zero
#  - Opções de menu inválidas
# 5. Use f-strings para formatar a saída dos resultados


def calculadora():
    print("Calculadora Simples")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    try:
        opcao = int(input("Escolha a operação (1-4): "))
        if opcao < 1 or opcao > 4:
            print("Operação inválida! Escolha entre 1 e 4.")
            return
    except ValueError:
        print("Entrada inválida! Digite um número.")
        return

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 =float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida! Digite apenas números .")
        return
    
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
                return

            resultado = num1 / num2
            print(f"Resultado: {num1} / {num2} = {resultado}")

        case _:
            print("Operação inválida!")

if __name__ == "__main__":
    calculadora()