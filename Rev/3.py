# Seção 3: List Comprehensions
# Filtro de Pares/Ímpares: Use list comprehension para filtrar números pares e ímpares de uma lista.

import random


def filtrar_pares_impares(numeros):
    """
    Filtra números pares e ímpares de uma lista usando list comprehension.
    """
    pares = [num for num in numeros if num % 2 == 0]
    impares = [num for num in numeros if num % 2 != 0]
    return pares, impares

# Exemplo de uso:
numeros_exemplo = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares, impares = filtrar_pares_impares(numeros_exemplo)
print(f"Números originais: {numeros_exemplo}")
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")

# Criação de uma matriz 3x3 usando list comprehension
matriz_3x3 = [[col for col in range(1, 4)] for _ in range(3)]
print("Matriz 3x3:")
for linha in matriz_3x3:
    print(linha)

matriz = [[random.randint(1, 100) for _ in range(3)] for _ in range(3)] 

for linha in matriz:
    print(linha) 