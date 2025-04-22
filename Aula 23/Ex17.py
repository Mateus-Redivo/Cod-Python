"""
Exercício 17 - Soma de Matrizes

Objetivo: Implementar a soma de duas matrizes 2x2 utilizando list comprehension.

Descrição:
- Criar duas matrizes A e B de dimensão 2x2
- Realizar a soma elemento por elemento das matrizes
- Utilizar list comprehension para uma implementação concisa
- Exibir o resultado da soma

Conceitos abordados:
- Matrizes como listas aninhadas
- List comprehension
- Operações com matrizes
"""

# Definição das matrizes de entrada
A = [[1, 2, 3],  
     [4, 5, 6], 
     [7, 8, 9]]  # Matriz A 2x2

B = [[9, 8, 7],  
     [6, 5, 4], 
     [3, 2, 1]]  # Matriz B 2x2

# Soma das matrizes usando list comprehension
# Para cada linha i e coluna j, soma os elementos correspondentes de A e B
# O primeiro loop (i) percorre as linhas
# O segundo loop (j) percorre as colunas


soma = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# soma = [A[i][j] + B[i][j] for i in range(1) for j in range(2)]

# Exibe o resultado da soma das matrizes
print("Resultado da soma das matrizes:")
print(soma)  # Resultado esperado: [[6, 8], [10, 12]]



for i in range(len(A)):
    for j in range(len(A[0])):
     print(f"A[{i}][{j}] + B[{i}][{j}] = {A[i][j]} + {B[i][j]}")

