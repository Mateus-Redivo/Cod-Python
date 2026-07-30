"""
Módulo 09 — Matrizes
Exemplo 02: percorrendo com laços aninhados

Este arquivo mostra:
  - o laço de fora nas linhas, o de dentro nas colunas
  - onde vai o print() que quebra a linha
  - percorrer por valor, quando o índice não interessa

Como executar:
  python 02_percorrendo.py
"""

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# --- Por índice: quando você precisa saber a posição -----------------
print("Por índice:")
for linha in range(len(matriz)):
    for coluna in range(len(matriz[0])):
        print(f"{matriz[linha][coluna]:4d}", end="")
    print()        # <- pertence ao laço EXTERNO: quebra a linha
print()


# --- O mesmo, sem o print() do fim -----------------------------------
print("Sem o print() vazio (tudo numa linha só):")
for linha in range(len(matriz)):
    for coluna in range(len(matriz[0])):
        print(f"{matriz[linha][coluna]:4d}", end="")
print()
print("^ é o print() vazio que transforma a saída em tabela")
print()


# --- Por valor: quando o índice não interessa ------------------------
print("Por valor (mais limpo):")
for linha in matriz:
    for valor in linha:
        print(f"{valor:4d}", end="")
    print()
print()


# --- Mostrando a posição de cada elemento ----------------------------
print("Cada elemento com sua posição:")
for linha in range(len(matriz)):
    for coluna in range(len(matriz[0])):
        print(f"  matriz[{linha}][{coluna}] = {matriz[linha][coluna]}")
print()


# --- Contando quantas vezes o laço interno roda ----------------------
execucoes = 0
for linha in range(len(matriz)):
    for coluna in range(len(matriz[0])):
        execucoes += 1

print(f"O laço interno rodou {execucoes} vezes")
print(f"= {len(matriz)} linhas x {len(matriz[0])} colunas")


# --- Experimento ---------------------------------------------------
# 1. Mova o print() vazio para DENTRO do laço interno (mais quatro
#    espaços). O que acontece com a saída? Por quê?
#
# 2. Troque a matriz por uma 2x4 e rode de novo. Tudo continua
#    funcionando? Esse é o motivo de usar len() em vez de números
#    fixos como 3.
#
# 3. Inverta os dois laços: coloque as colunas por fora e as linhas
#    por dentro, mantendo matriz[linha][coluna]. A saída sai
#    transposta. Esse é o truque do exercício 01.
