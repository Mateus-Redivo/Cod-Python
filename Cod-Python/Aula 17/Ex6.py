# Programa para contar números positivos e negativos em uma sequência de 10 números

# Cria uma lista com 10 números usando list comprehension:
# - Solicita entrada do usuário 10 vezes através do range(10)
# - Converte cada entrada para inteiro usando int()
numeros = [int(input("Digite um número: ")) for _ in range(10)]

# Conta números positivos usando sum() e generator expression:
# - Para cada número na lista, retorna 1 se for positivo (>0)
# - sum() soma todos os 1s, resultando no total de positivos
positivos = sum(1 for num in numeros if num > 0)

# Conta números negativos de forma similar:
# - Para cada número na lista, retorna 1 se for negativo (<0)
# - sum() soma todos os 1s, resultando no total de negativos
negativos = sum(1 for num in numeros if num < 0)

# Exibe o resultado formatado usando f-string
print(f"Positivos: {positivos}, Negativos: {negativos}")
