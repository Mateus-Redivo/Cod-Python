"""
Exercício 24 - Matriz Aleatória
Desenvolva um programa em Python que:
1. Crie uma matriz 3x3
2. Preencha a matriz com números inteiros aleatórios entre 1 e 100
3. Exiba a matriz na tela de forma organizada, com cada elemento entre colchetes
"""

# Importando o módulo random para gerar números aleatórios
import random

# Criando uma matriz 3x3 usando compreensão de lista aninhada:
# - A compreensão externa cria 3 linhas
# - A compreensão interna cria 3 colunas para cada linha
# - random.randint(1, 100) gera números inteiros aleatórios entre 1 e 100
# - _ é usado como variável descartável já que não precisamos da variável do loop
matrix = [[random.randint(1, 100) for _ in range(3)] for _ in range(3)]

for i in range(3):
    ale= random.randint(1,100)
    print(ale)
    for j in range(3):
        matrix[i][j] = ale

# Exibindo a matriz em formato de grade:
print("Matriz 3x3 em grade:")
for row in matrix:
    for num in row:
        print(f"[{num:3d}]", end=" ")
    print()
    

# Exibindo a matriz em linha, sem formatação:
print("\nMatriz 3x3 em linha, sem formatação: ")
for row in matrix:
    for num in row:
        print(f"[{num:3d}]", end=" ")
