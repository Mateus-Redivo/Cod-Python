# Seção 4: Estruturas de Controle e Funções

# Match-Case: Implemente um programa que utiliza a estrutura match-case (Python 3.10+) para diferentes opções de menu.
def menu_com_match_case():
    print("\n===== Menu de Opções =====")
    print("1. Calcular área de um círculo")
    print("2. Verificar se número é par ou ímpar")
    print("3. Converter temperatura para Fahrenheit")
    print("4. Sair")
    
    opcao = input("Escolha uma opção (1-4): ")
    
    match opcao:
        case "1":
            raio = float(input("Digite o raio do círculo: "))
            area = 3.14159 * raio * raio
            print(f"A área do círculo é: {area:.2f}")
        case "2":
            num = int(input("Digite um número inteiro: "))
            resultado = "par" if num % 2 == 0 else "ímpar"
            print(f"O número {num} é {resultado}.")
        case "3":
            celsius = float(input("Digite a temperatura em Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius}°C equivale a {fahrenheit:.1f}°F")
        case "4":
            print("Saindo do programa...")
            return False
        case _:
            print("Opção inválida! Tente novamente.")
    return True

# Função com Tratamento de Erros: Crie uma função de divisão que trata adequadamente possíveis divisões por zero.
def divisao_segura(numerador, denominador):
    try:
        resultado = numerador / denominador
        return resultado
    except ZeroDivisionError:
        return "Erro: Divisão por zero não é permitida"
    except TypeError:
        return "Erro: Os valores fornecidos devem ser numéricos"

# Estrutura Principal: Implemente um programa que usa a estrutura if __name__ == "__main__" corretamente.
def calcular_media(numeros):
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)

def obter_lista_numeros():
    entrada = input("Digite números separados por espaço: ")
    try:
        return [float(num) for num in entrada.split()]
    except ValueError:
        print("Entrada inválida. Use apenas números.")
        return []

if __name__ == "__main__":
    print("Executando o programa como script principal")
    
    # Demonstração da função divisão segura
    print(f"10 / 2 = {divisao_segura(10, 2)}")
    print(f"10 / 0 = {divisao_segura(10, 0)}")
    
    # Demonstração do cálculo de média
    numeros = obter_lista_numeros()
    if numeros:
        print(f"A média dos números é: {calcular_media(numeros):.2f}")
    
    # Demonstração do menu com match-case
    executando = True
    while executando:
        executando = menu_com_match_case()
else:
    print("Este módulo foi importado por outro script") 