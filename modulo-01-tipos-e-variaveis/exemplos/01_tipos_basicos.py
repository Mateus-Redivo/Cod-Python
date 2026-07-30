"""
Módulo 01 — Tipos e variáveis
Exemplo 01: os quatro tipos básicos

Este arquivo mostra:
  - int, float, str e bool
  - como descobrir o tipo de um valor com type()

Como executar:
  python 01_tipos_basicos.py
"""

# int — número inteiro, sem casas decimais
idade = 25
saldo_devedor = -150
zero = 0

# float — número com casas decimais. O separador é PONTO.
altura = 1.75
preco = 49.90

# str — texto. Aspas simples ou duplas, tanto faz.
nome = "Maria Silva"
cidade = 'Cascavel'
vazio = ""

# bool — só dois valores possíveis, e ambos com letra maiúscula.
aprovado = True
tem_desconto = False

print(f"idade         = {idade}")
print(f"altura        = {altura}")
print(f"nome          = {nome}")
print(f"aprovado      = {aprovado}")
print()

# type() responde qual é o tipo de um valor.
print(f"type(idade)    -> {type(idade)}")
print(f"type(altura)   -> {type(altura)}")
print(f"type(nome)     -> {type(nome)}")
print(f"type(aprovado) -> {type(aprovado)}")
print()

# Cuidado com estes dois: parecem iguais na tela, mas não são.
numero_de_verdade = 25
numero_de_mentira = "25"

print(f"{numero_de_verdade} é do tipo {type(numero_de_verdade).__name__}")
print(f"{numero_de_mentira} é do tipo {type(numero_de_mentira).__name__}")


# --- Experimento ---------------------------------------------------
# 1. Acrescente print(numero_de_verdade + 5) e depois
#    print(numero_de_mentira + 5). O segundo quebra. Leia o erro.
#
# 2. Troque "altura = 1.75" por "altura = 1,75" e rode. O type() muda
#    para algo inesperado: a vírgula criou uma tupla, não um número.
#
# 3. Escreva "ligado = true" (minúsculo) e rode. Que erro aparece?
