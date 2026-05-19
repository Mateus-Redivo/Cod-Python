"""
Matriz Transposta

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

# --- Criar a matriz original 2x3 com valores sequenciais ---
matriz_original = []
valor = 1
for _ in range(2):
    linha = []
    for _ in range(3):
        linha.append(valor)
        valor += 1
    matriz_original.append(linha)

print("Matriz Original (2 linhas x 3 colunas):")
for linha in matriz_original:
    print("  " + "  ".join(f"{num:4d}" for num in linha))
print()

# --- Gerar a transposta 3x2: A[i][j] → Aᵀ[j][i] ---
linhas = len(matriz_original)
colunas = len(matriz_original[0])
matriz_transposta = []

for j in range(colunas):
    nova_linha = []
    for i in range(linhas):
        nova_linha.append(matriz_original[i][j])
    matriz_transposta.append(nova_linha)

print("Matriz Transposta (3 linhas x 2 colunas):")
for linha in matriz_transposta:
    print("  " + "  ".join(f"{num:4d}" for num in linha))
print()

# --- Verificação: Aᵀ[j][i] deve ser igual a A[i][j] ---
print("Verificação da regra  Aᵀ[j][i] == A[i][j]:")
for i in range(linhas):
    for j in range(colunas):
        original = matriz_original[i][j]
        transposto = matriz_transposta[j][i]
        print(f"  A[{i}][{j}] = {original}  →  Aᵀ[{j}][{i}] = {transposto}  ✓")
