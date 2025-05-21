"""
Exercício 16 - Introdução a Matrizes

Objetivo: Criar, acessar e modificar elementos de uma matriz simples.

Tarefas:
1. Criar uma matriz 3x3 com valores numéricos sequenciais
2. Acessar um elemento específico da matriz e exibi-lo
3. Modificar o valor de um elemento da matriz
4. Exibir o elemento modificado para verificar a alteração
5. Calcular a soma de todos os elementos

Conceitos abordados:
- Representação de matrizes como listas aninhadas
- Acesso a elementos por índice
- Modificação de elementos de matrizes
"""

# Criação da matriz 3x3
matriz = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]

# Exibição da matriz original de forma estruturada
print("Matriz original:")
for linha in matriz:
    print(linha)

# Acessando e exibindo um elemento específico
print("\nElemento na posição [0][0]:", matriz[0][0])

# Modificando um elemento
matriz[0][0] = 10
print("Elemento modificado [0][0]:", matriz[0][0])

# Matriz após modificação
print("\nMatriz após modificação:")
for linha in matriz:
    print(linha)

# Calculando a soma de todos os elementos
soma = 0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        soma += matriz[i][j]
print("\nSoma de todos os elementos:", soma)
