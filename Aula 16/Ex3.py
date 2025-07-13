# Enunciado 1: Crie um programa que leia 5 números inteiros e os armazene em uma lista. 
# Em seguida, exiba a lista na ordem inversa.

# Criação da lista usando list comprehension:
# - Executa o loop 5 vezes (range(5))
# - Para cada iteração, solicita um número via input()
# - Converte a entrada para inteiro com int()
# - Armazena cada número na lista 'numeros'
numeros = [int(input("Digite um número: ")) for _ in range(5)]

# Exibe a lista na ordem inversa:
# - numeros[::-1] usa slice com passo -1 para inverter a lista
# - O primeiro : significa "do início"
# - O segundo : significa "até o fim"
# - O -1 significa "ande para trás"
print("Números na ordem inversa:", numeros[::-1])
