"""
Módulo 06 — Listas
Exemplo 02: percorrendo com for

Este arquivo mostra:
  - percorrer por valor (a forma padrão)
  - percorrer por índice (quando a posição importa)
  - o acumulador do módulo 05 aplicado a listas

Como executar:
  python 02_percorrendo.py
"""

notas = [8.0, 7.5, 9.0, 6.5, 10.0]
print(f"notas = {notas}")
print()

# --- Por valor: a forma padrão ---------------------------------------
# Use esta sempre que você só precisar do conteúdo.
print("Por valor:")
for nota in notas:
    print(f"  {nota}")
print()


# --- Por índice: quando a posição importa ----------------------------
# len(notas) dá 5, e range(5) produz 0,1,2,3,4 — exatamente os
# índices válidos. Não é coincidência: é o motivo do índice começar
# em zero.
print("Por índice:")
for i in range(len(notas)):
    print(f"  Nota {i + 1}: {notas[i]}")
print()


# --- O acumulador do módulo 05, agora com lista ---------------------
soma = 0
for nota in notas:
    soma += nota

print(f"soma pelo acumulador = {soma}")
print(f"soma pelo sum()      = {sum(notas)}")
print(f"média                = {soma / len(notas):.2f}")
print()

# sum() resolve a soma simples. O acumulador continua necessário
# quando a soma tem CONDIÇÃO:
soma_dos_aprovados = 0
quantidade_aprovados = 0

for nota in notas:
    if nota >= 7.0:
        soma_dos_aprovados += nota
        quantidade_aprovados += 1

print(f"notas >= 7.0: {quantidade_aprovados} notas, média {soma_dos_aprovados / quantidade_aprovados:.2f}")
print()


# --- Achando o maior, do jeito manual --------------------------------
# max() faz isso numa palavra. Vale ver o mecanismo uma vez.
maior = notas[0]            # começa com o PRIMEIRO, não com zero
for nota in notas:
    if nota > maior:
        maior = nota

print(f"maior pelo laço  = {maior}")
print(f"maior pelo max() = {max(notas)}")


# --- Experimento ---------------------------------------------------
# 1. Troque "for i in range(len(notas))" por "for i in range(5)".
#    Funciona igual — até você acrescentar uma nota na lista. Por que
#    o len() é a forma certa?
#
# 2. No bloco dos aprovados, troque o 7.0 por 11.0 (nenhuma nota
#    passa). O programa quebra com ZeroDivisionError: quantidade
#    ficou zero. Conserte com um if antes da divisão.
#
# 3. Troque "maior = notas[0]" por "maior = 0" e rode com a lista
#    [-5, -2, -9]. A resposta sai errada. Por quê?
