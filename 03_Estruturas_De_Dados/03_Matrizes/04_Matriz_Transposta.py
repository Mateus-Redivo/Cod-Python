"""
Exercício 21 - Matriz Transposta

Objetivo: Criar a transposta de uma matriz (trocar linhas por colunas).

Conceito:
    A transposta de uma matriz A é obtida refletindo os elementos
    ao longo da diagonal principal: o elemento A[i][j] vai para Aᵀ[j][i].

    Se A tem dimensão M x N, então Aᵀ (transposta) tem dimensão N x M.

    Exemplo:
    A (2x3):             Aᵀ (3x2):
    [ 1   2   3 ]        [ 1   4 ]
    [ 4   5   6 ]   →    [ 2   5 ]
                         [ 3   6 ]

    Regra: Aᵀ[j][i] = A[i][j]

Tarefas:
1. Criar uma matriz 2x3 com valores sequenciais
2. Gerar sua transposta (3x2)
3. Exibir ambas as matrizes de forma organizada
4. Verificar que cada elemento foi corretamente transposto
"""


def criar_matriz(linhas, colunas):
    """Cria uma matriz M x N com valores sequenciais a partir de 1."""
    matriz = []
    valor = 1
    for _ in range(linhas):
        linha = []
        for _ in range(colunas):
            linha.append(valor)
            valor += 1
        matriz.append(linha)
    return matriz


def transpor_matriz(matriz):
    """Retorna a transposta: A[i][j] → Aᵀ[j][i]."""
    linhas = len(matriz)
    colunas = len(matriz[0])
    transposta = []

    for j in range(colunas):
        nova_linha = []
        for i in range(linhas):
            nova_linha.append(matriz[i][j])
        transposta.append(nova_linha)

    return transposta


def exibir_matriz(matriz):
    """Exibe a matriz com alinhamento de colunas."""
    for linha in matriz:
        print("  " + "  ".join(f"{num:4d}" for num in linha))
    print()


# --- Criar e exibir a matriz original 2x3 ---
matriz_original = criar_matriz(2, 3)

print("Matriz Original (2 linhas x 3 colunas):")
exibir_matriz(matriz_original)

# --- Gerar e exibir a transposta 3x2 ---
matriz_transposta = transpor_matriz(matriz_original)

print("Matriz Transposta (3 linhas x 2 colunas):")
exibir_matriz(matriz_transposta)

# --- Verificação: Aᵀ[j][i] deve ser igual a A[i][j] ---
print("Verificação da regra  Aᵀ[j][i] == A[i][j]:")
linhas = len(matriz_original)
colunas = len(matriz_original[0])
for i in range(linhas):
    for j in range(colunas):
        original = matriz_original[i][j]
        transposto = matriz_transposta[j][i]
        print(f"  A[{i}][{j}] = {original}  →  Aᵀ[{j}][{i}] = {transposto}  ✓")
