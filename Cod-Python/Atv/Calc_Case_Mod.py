def exibir_menu():
    """Exibe o menu de opções da calculadora."""
    print("Calculadora Simples")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Raiz Quadrada")
    print("6. Potência")
    print("0. Sair")


def obter_operacao():
    """Obtém a escolha de operação do usuário com tratamento de erro."""
    try:
        opcao = int(input("Escolha a operação (0-6): "))
        if opcao < 0 or opcao > 6:
            print("Operação inválida! Escolha entre 0 e 6.")
            return None
        return opcao
    except ValueError:
        print("Entrada inválida! Digite um número.")
        return None


def obter_numeros():
    """Obtém os números de entrada com tratamento de erro."""
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        return num1, num2
    except ValueError:
        print("Entrada inválida! Digite apenas números.")
        return None, None


def soma(a, b):
    """Realiza a operação de soma."""
    return a + b


def subtracao(a, b):
    """Realiza a operação de subtração."""
    return a - b


def multiplicacao(a, b):
    """Realiza a operação de multiplicação."""
    return a * b


def divisao(a, b):
    """Realiza a operação de divisão com verificação de divisão por zero."""
    if b == 0:
        print("Erro: Divisão por zero não é permitida!")
        return None
    return a / b


def raiz(a):
    """Calcula a raiz quadrada de um número."""
    if a < 0:
        print("Erro: Não é possível calcular a raiz de um número negativo!")
        return None
    return a ** 0.5


def potencia(a, b):
    """Calcula a potência de um número elevado a outro."""
    return a ** b


def exibir_resultado(a, b, operacao, resultado):
    """Exibe o resultado formatado da operação."""
    operadores = {
        1: '+',
        2: '-',
        3: '*',
        4: '/',
        5: '√',
        6: '^'
    }
    operador = operadores.get(operacao)
    if operacao == 5:  # Raiz quadrada
        print(f"Resultado: √{a} = {resultado}")
    else:
        print(f"Resultado: {a} {operador} {b} = {resultado}")


def obter_entrada_para_operacao(opcao):
    """Obtém os números necessários para a operação escolhida."""
    if opcao == 5:  # Raiz quadrada só precisa de um número
        try:
            num1 = float(input("Digite o número para cálculo da raiz: "))
            num2 = None
        except ValueError:
            print("Entrada inválida! Digite apenas números.")
            return None, None
    else:
        num1, num2 = obter_numeros()
    return num1, num2

def executar_operacao(opcao, num1, num2):
    """Executa a operação escolhida."""
    match opcao:
        case 1:
            return soma(num1, num2)
        case 2:
            return subtracao(num1, num2)
        case 3:
            return multiplicacao(num1, num2)
        case 4:
            return divisao(num1, num2)
        case 5:
            return raiz(num1)
        case 6:
            return potencia(num1, num2)
    return None

def calculadora():
    """Função principal da calculadora."""
    while True:
        exibir_menu()

        opcao = obter_operacao()
        if opcao is None:
            continue
        if opcao == 0:
            print("Encerrando calculadora...")
            break

        num1, num2 = obter_entrada_para_operacao(opcao)
        if num1 is None or (opcao != 5 and num2 is None):
            continue

        resultado = executar_operacao(opcao, num1, num2)

        if resultado is not None:
            exibir_resultado(num1, num2, opcao, resultado)
        print()  # Linha em branco para separar as operações


if __name__ == "__main__":
    calculadora()
