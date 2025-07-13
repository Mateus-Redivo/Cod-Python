# Enunciado 1: Leia uma lista de 10 números e exiba o menor e o maior valor encontrado.

# Cria uma lista com 10 números fornecidos pelo usuário usando list comprehension

#  numeros = [int(input("Digite um número: ")) for _ in range(10)]

# Usa as funções min() e max() para encontrar o menor e maior valor
# Exibe os resultados usando f-string

#  print(f"Menor valor: {min(numeros)}, Maior valor: {max(numeros)}")


# Enunciado 1: Leia uma lista de 10 números e exiba o menor e o maior valor encontrado.

# Cria uma lista com 10 números fornecidos pelo usuário usando list comprehension
numeros = [int(input("Digite um número: ")) for _ in range(10)]

# Inicializa menor e maior com o primeiro elemento da lista
menor = numeros[0]
maior = numeros[0]

# Percorre a lista para encontrar o menor e maior valor
for num in numeros:
    if num < menor:
        menor = num
    if num > maior:
        maior = num

# Exibe os resultados usando f-string
print(f"Menor valor: {menor}, Maior valor: {maior}")