"""
Exercício 18 - Soma de Matrizes com NumPy

Objetivo: Implementar a soma de duas matrizes 2x2 utilizando a biblioteca NumPy.

Descrição:
- Criar duas matrizes A e B de dimensão 2x2 usando NumPy arrays
- Realizar a soma das matrizes utilizando operadores NumPy
- Comparar a simplicidade em relação à implementação com list comprehension

Conceitos abordados:
- NumPy arrays
- Operações matriciais com NumPy
- Vantagens do NumPy sobre listas puras Python
"""

import numpy as np

# Criação das matrizes usando np.array
A = np.array([[1, 2], [3, 4]])  # Matriz A 2x2
B = np.array([[5, 6], [7, 8]])  # Matriz B 2x2

# Soma das matrizes A e B
# NumPy permite soma direta de arrays usando o operador +
soma = A + B

print("Resultado da soma das matrizes A e B:")
print(soma)  # Resultado esperado: [[6 8], [10 12]]
