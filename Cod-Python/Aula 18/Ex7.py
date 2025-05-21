# Enunciado 1: Leia um vetor de 8 números inteiros e exiba a soma de seus elementos.

# Cria uma lista de 8 números inteiros usando list comprehension
# [int(input("Digite um número: ")) for _ in range(8)] faz o seguinte:
# 1. range(8) gera uma sequência de 0 a 7
# 2. for _ in range(8) itera 8 vezes (o _ é usado quando não precisamos da variável de iteração)
# 3. int(input("Digite um número: ")) em cada iteração:
#    - Solicita um número ao usuário
#    - Converte a entrada de string para inteiro
numeros = [int(input("Digite um número: ")) for _ in range(8)]

# Exibe a soma de todos os elementos do vetor usando a função sum()
# sum() soma todos os valores da lista 'numeros'
print("Soma dos elementos:", sum(numeros))
