"""
Módulo 00 — Preparação
Exemplo 01: o menor programa possível

Este arquivo mostra:
  - o print com um texto
  - o print com vários valores separados por vírgula
  - o print vazio, que só pula uma linha

Como executar:
  python 01_ola_mundo.py
"""

# O programa inteiro cabe nesta linha.
print("Olá, mundo!")

# As aspas dizem "isto é texto". Sem elas, o Python procuraria
# variáveis com esses nomes e reclamaria que não existem.
print("Meu nome é Maria e estou aprendendo Python.")

# print() sem nada dentro pula uma linha. Serve para dar respiro.
print()

# Com vírgula, o print aceita vários valores e separa com um espaço.
print("Ano:", 2026)
print("A soma de 2 + 3 é", 2 + 3)

# Repare: o número 2026 e a conta 2 + 3 estão FORA das aspas.
# O que está fora das aspas o Python calcula; o que está dentro,
# ele mostra literalmente.
print("2 + 3")          # mostra o texto 2 + 3
print(2 + 3)            # mostra o resultado 5


# --- Experimento ---------------------------------------------------
# 1. Troque o nome na segunda linha pelo seu e rode de novo.
#
# 2. Apague uma das aspas de qualquer print e rode.
#    Leia a mensagem: qual linha ela aponta? Conserte depois.
#
# 3. Escreva print(2 + 3 * 4) e tente adivinhar o resultado antes
#    de rodar. É 20 ou 14? O módulo 02 explica por quê.
