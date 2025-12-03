"""
Exercício 15 - Manipulação de Matrizes

Objetivo: Demonstrar diferentes formas de criar e manipular matrizes em Python,
utilizando tanto listas aninhadas quanto a biblioteca NumPy.

Tarefas:
1. Criar uma matriz 3x3 usando listas aninhadas
2. Acessar elementos específicos da matriz
3. Criar a mesma matriz usando NumPy
4. Comparar as diferentes representações

Obs: Este exercício ilustra as diferenças entre matrizes implementadas com
listas Python puras e arrays NumPy.
"""

import numpy as np

matriz = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9]
]

print(matriz)  # Saida: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Saida: 1 Acessa o elemento na primeira linha e primeira coluna
print(matriz[0][0])
# Saida: 6 Acessa o elemento na segunda linha e terceira coluna
print(matriz[1][2])


matriz2 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(matriz2)
