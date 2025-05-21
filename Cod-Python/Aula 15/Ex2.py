# Enunciado 2: Escreva um programa que leia um número inteiro e exiba sua tabuada de 1 a 10.

# Solicita ao usuário que digite um número e armazena em 'n'
# A função input() captura a entrada como string
# int() converte a string para um número inteiro
n = int(input("Digite um número: "))

# Utiliza um loop for com a função range()
# range(1, 11) cria uma sequência de números de 1 até 10
# O primeiro parâmetro (1) é inclusivo
# O segundo parâmetro (11) é exclusivo
for i in range(1, 11):
    # Para cada valor de i no loop:
    # - Usa f-string (formatted string) para criar a saída
    # - {n} representa o número escolhido pelo usuário
    # - {i} representa o multiplicador atual (1 a 10)
    # - {n * i} calcula e mostra o resultado da multiplicação
    print(f"{n} x {i} = {n * i}")
