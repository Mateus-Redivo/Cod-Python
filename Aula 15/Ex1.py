# Enunciado 1: Escreva um programa que solicite um número inteiro positivo N ao usuário e imprima os N primeiros números da sequência de Fibonacci.

def fibonacci(n: int) -> None:
    """
    Função que imprime os N primeiros números da sequência de Fibonacci
    Args:
        n (int): Quantidade de números da sequência a serem impressos
    Returns:
        None: A função apenas imprime os valores
    """
    
    # Verifica se o número é positivo
    if n <= 0:
        print("Por favor, digite um número inteiro positivo.")
        return

    # Inicializa as variáveis para os dois primeiros números da sequência
    a, b = 0, 1  # a é o número atual, b é o próximo número
    
    # Loop que executa N vezes para gerar a sequência
    for _ in range(n):
        print(a, end=" ")  # Imprime o número atual sem quebrar a linha
        a, b = b, a + b    # Atualiza os valores: a recebe b, b recebe a soma dos anteriores
    
    print()  # Adiciona uma nova linha ao final da sequência


# Bloco principal do programa
try:
    # Solicita e converte a entrada do usuário para inteiro
    n = int(input("Digite um número inteiro positivo: "))
    fibonacci(n)  # Chama a função fibonacci com o número informado
except ValueError:
    # Trata o erro caso o usuário digite algo que não seja um número
    print("Entrada inválida. Por favor, digite um número inteiro.")
