"""
Módulo 09 — Matrizes
Exemplo 04: criando do tamanho certo, e a armadilha do * 3

Este arquivo mostra:
  - montar uma matriz do tamanho que o programa precisar
  - por que [[0] * 3] * 3 NÃO funciona
  - preencher com valores calculados

Como executar:
  python 04_criando_dinamicamente.py
"""

LINHAS = 3
COLUNAS = 4

# --- A forma segura: uma lista NOVA a cada volta ---------------------
matriz = []
for i in range(LINHAS):
    nova_linha = []             # nasce uma lista nova aqui, a cada volta
    for j in range(COLUNAS):
        nova_linha.append(0)
    matriz.append(nova_linha)

print(f"Matriz {LINHAS}x{COLUNAS} de zeros:")
for linha in matriz:
    print(f"  {linha}")
print()

# Alterar um elemento afeta só ele:
matriz[0][0] = 9
print("Após matriz[0][0] = 9:")
for linha in matriz:
    print(f"  {linha}")
print()


# --- A ARMADILHA -----------------------------------------------------
print("=" * 52)
print("A armadilha do * 3")
print("=" * 52)

armadilha = [[0] * 3] * 3

print("armadilha = [[0] * 3] * 3")
print(f"parece certa: {armadilha}")

armadilha[0][0] = 9

print("depois de armadilha[0][0] = 9:")
print(f"  {armadilha}")
print()
print("Mudou as TRÊS linhas! O * 3 não fez três cópias da lista:")
print("fez três referências À MESMA lista. Alterar uma altera todas,")
print("porque são a mesma lista.")
print()

# A prova: os três "id" são idênticos.
print("Prova — o endereço de memória das três linhas:")
for i in range(3):
    print(f"  armadilha[{i}] -> id {id(armadilha[i])}")
print()
print("Na matriz criada com laço, os ids são diferentes:")
for i in range(LINHAS):
    print(f"  matriz[{i}] -> id {id(matriz[i])}")
print()


# --- Preenchendo com valores calculados ------------------------------
tabuada = []
for i in range(1, 4):
    linha = []
    for j in range(1, 5):
        linha.append(i * j)
    tabuada.append(linha)

print("Matriz de multiplicação (linha x coluna):")
for linha in tabuada:
    print("  " + "".join(f"{v:4d}" for v in linha))


# --- Experimento ---------------------------------------------------
# 1. Troque a criação segura pela armadilha ([[0] * COLUNAS] * LINHAS)
#    e rode o programa inteiro. Quantas linhas ficam com o 9?
#
# 2. Rode [0] * 3 sozinho. Para uma lista de NÚMEROS, o * 3 funciona
#    perfeitamente — o problema só aparece quando o elemento repetido
#    é ele mesmo uma lista.
#
# 3. Mude LINHAS e COLUNAS para 5 e 2. Todo o resto continua
#    funcionando? É o ganho de não ter números fixos no código.
