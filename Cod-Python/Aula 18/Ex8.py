# Enunciado 2: Peça ao usuário para digitar 6 números inteiros e mostre apenas os ímpares.

# Usando list comprehension para solicitar 6 números ao usuário
# O loop range(6) executa 6 vezes
# Cada número digitado é convertido para inteiro com int()
numeros = [int(input("Digite um número: ")) for _ in range(6)]

# Criando uma nova lista apenas com os números ímpares
# Usa list comprehension para filtrar os números
# A condição num % 2 != 0 verifica se o número é ímpar
# Se o resto da divisão por 2 é diferente de 0, o número é ímpar
impares = [num for num in numeros if num % 2 != 0]

# Exibe a lista de números ímpares
print("Números ímpares:", impares)
