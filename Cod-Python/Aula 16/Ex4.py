# Enunciado 2: Desenvolva um programa que leia 10 números e exiba apenas os números pares.

# ========== Entrada de Dados ==========
# Utiliza list comprehension para criar uma lista de 10 números
# List comprehension é uma forma concisa de criar listas em Python
# O loop range(10) executa 10 vezes, gerando índices de 0 a 9
# O underscore (_) é usado como variável descartável já que não utilizamos o índice
# int(input()) converte a entrada do usuário de string para número inteiro
# A lista final 'numeros' armazenará os 10 valores fornecidos pelo usuário
numeros = [int(input("Digite um número: ")) for _ in range(10)]

# ========== Processamento ==========
# Filtra apenas os números pares
pares = [n for n in numeros if n % 2 == 0]

# ========== Saída ==========
# Exibe os números pares
print("Números pares:", pares)