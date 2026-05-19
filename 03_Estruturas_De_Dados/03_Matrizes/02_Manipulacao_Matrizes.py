"""
Manipulação de Matrizes

Objetivo: Demonstrar diferentes formas de criar e manipular matrizes em Python,
utilizando tanto listas aninhadas quanto a biblioteca NumPy.

Conceito:
    Python oferece duas formas principais de trabalhar com matrizes:

    1. Listas aninhadas (nativo):
       - Sem dependências externas
       - Estrutura flexível
       - Sintaxe: matriz[linha][coluna]

    2. NumPy arrays (biblioteca):
       - Otimizado para cálculos matemáticos
       - Muito mais rápido para matrizes grandes
       - Mesma sintaxe de acesso: matriz[linha][coluna]
       - Inclui informações como shape (dimensões)

Tarefas:
1. Criar uma matriz 3x3 usando listas aninhadas e acessar elementos
2. Criar a mesma matriz usando NumPy e acessar elementos
3. Comparar as duas representações
"""

import numpy as np

# ============================================================
#  PARTE 1 — Listas Python puras (sem bibliotecas)
# ============================================================
print("=" * 50)
print("  PARTE 1 — Matriz com Listas Python")
print("=" * 50)

matriz_lista = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print("\nRepresentação completa (lista de listas):")
print(f"  {matriz_lista}")

print("\nExibição linha a linha:")
for i, linha in enumerate(matriz_lista):
    print(f"  linha {i}: {linha}")

print("\nAcesso por índice [linha][coluna]:")
print(f"  matriz[0][0] → {matriz_lista[0][0]}   (linha 0, coluna 0)")
print(f"  matriz[1][2] → {matriz_lista[1][2]}   (linha 1, coluna 2)")
print(f"  matriz[2][1] → {matriz_lista[2][1]}   (linha 2, coluna 1)")

# ============================================================
#  PARTE 2 — NumPy (biblioteca para computação numérica)
# ============================================================
print("\n" + "=" * 50)
print("  PARTE 2 — Matriz com NumPy")
print("=" * 50)

matriz_numpy = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])

print(
    f"\nDimensões (shape): {matriz_numpy.shape}  → {matriz_numpy.shape[0]} linhas x {matriz_numpy.shape[1]} colunas")
print(f"Tipo dos dados:    {matriz_numpy.dtype}")

print("\nRepresentação NumPy (exibição formatada automaticamente):")
print(matriz_numpy)

print("\nAcesso por índice [linha][coluna] — mesma sintaxe:")
print(f"  matriz[0][0] → {matriz_numpy[0][0]}   (linha 0, coluna 0)")
print(f"  matriz[1][2] → {matriz_numpy[1][2]}   (linha 1, coluna 2)")
print(f"  matriz[2][1] → {matriz_numpy[2][1]}   (linha 2, coluna 1)")

# ============================================================
#  COMPARAÇÃO
# ============================================================
print("\n" + "=" * 50)
print("  COMPARAÇÃO")
print("=" * 50)
print()
print("  Característica       Lista Python    NumPy")
print("  " + "-" * 44)
print("  Dependência          Nenhuma         import numpy")
print("  Acesso [i][j]        Sim             Sim")
print("  Info de dimensões    manual          .shape automático")
print("  Velocidade           Normal          Muito mais rápida")
print("  Uso ideal            Flexibilidade   Cálculos matemáticos")
