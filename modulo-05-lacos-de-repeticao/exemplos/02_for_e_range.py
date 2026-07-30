"""
Módulo 05 — Laços de repetição
Exemplo 02: for e range()

Este arquivo mostra:
  - range() com um, dois e três argumentos
  - por que o limite final NÃO aparece na saída
  - o mesmo laço escrito com while e com for, lado a lado

Como executar:
  python 02_for_e_range.py
"""

# range(n) -> começa em 0 e para ANTES de n
print("range(5):", end=" ")
for i in range(5):
    print(i, end=" ")
print()

# range(inicio, fim) -> o "fim" é exclusivo: range(1, 6) vai até o 5
print("range(1, 6):", end=" ")
for i in range(1, 6):
    print(i, end=" ")
print()

# range(inicio, fim, passo) -> pula de "passo" em "passo"
print("range(0, 11, 2):", end=" ")
for i in range(0, 11, 2):
    print(i, end=" ")
print()

# passo negativo conta para trás
print("range(10, 0, -1):", end=" ")
for i in range(10, 0, -1):
    print(i, end=" ")
print()
print()


# --- O mesmo resultado, dois jeitos ---------------------------------
# Com while: você cuida de inicializar, testar e atualizar.
i = 1
while i <= 3:
    print(f"  while: {i}")
    i += 1

# Com for: as três responsabilidades cabem em uma linha.
for i in range(1, 4):
    print(f"  for:   {i}")


# --- Experimento ---------------------------------------------------
# 1. Troque "range(1, 6)" por "range(1, 5)".
#    O 5 sumiu da saída? Esse é o erro mais comum do módulo:
#    para ir ATÉ 10, escreva range(1, 11).
#
# 2. Escreva um for que imprima os múltiplos de 5 entre 5 e 50.
#    Dica: você precisa dos três argumentos do range.
#
# 3. Troque o passo de "range(10, 0, -1)" para -3. Qual o último
#    número impresso? Confira antes de rodar.
