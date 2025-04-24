"""
Exercício 3 - Matriz Transposta

Objetivo: Criar a transposta de uma matriz (trocar linhas por colunas).

Tarefas:
1. Criar uma matriz 2x3
2. Gerar sua transposta (3x2)
3. Exibir ambas as matrizes de forma organizada
4. Verificar se os elementos foram corretamente transpostos

Exemplo:
Original (2x3):    Transposta (3x2):
[1 2 3]            [1 4]
[4 5 6]      →     [2 5]
                   [3 6]
"""

def criar_matriz(linhas, colunas):
    matriz = []
    valor = 1
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(valor)
            valor += 1
        matriz.append(linha)
    return matriz

def transpor_matriz(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    transposta = []
    
    for j in range(colunas):
        nova_linha = []
        for i in range(linhas):
            nova_linha.append(matriz[i][j])
        transposta.append(nova_linha)
    
    return transposta

def imprimir_matriz(matriz):
    for linha in matriz:
        print([f"{num:2d}" for num in linha])
    print()

# Criar matriz original 2x3
matriz_original = criar_matriz(2, 3)

# Gerar matriz transposta
matriz_transposta = transpor_matriz(matriz_original)

# Exibir resultados
print("Matriz Original (2x3):")
imprimir_matriz(matriz_original)

print("Matriz Transposta (3x2):")
imprimir_matriz(matriz_transposta)