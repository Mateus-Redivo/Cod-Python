"""
Módulo 02 — Operadores
Exemplo 04: operadores lógicos

Este arquivo mostra:
  - and, or e not nas quatro combinações possíveis
  - a armadilha do intervalo: quando é and e quando é or
  - o atalho de Python para intervalos

Como executar:
  python 04_logicos.py
"""

# and: só é True quando as DUAS pontas são True.
print("--- and ---")
print(f"True  and True   -> {True and True}")
print(f"True  and False  -> {True and False}")
print(f"False and True   -> {False and True}")
print(f"False and False  -> {False and False}")
print()

# or: basta UMA ponta ser True.
print("--- or ---")
print(f"True  or True    -> {True or True}")
print(f"True  or False   -> {True or False}")
print(f"False or True    -> {False or True}")
print(f"False or False   -> {False or False}")
print()

# not: inverte.
print("--- not ---")
print(f"not True   -> {not True}")
print(f"not False  -> {not False}")
print()


# --- Na prática ------------------------------------------------------
idade = 20
tem_carteira = True
usuario_logado = False

pode_dirigir = idade >= 18 and tem_carteira
precisa_login = not usuario_logado

print(f"pode_dirigir  = {pode_dirigir}")
print(f"precisa_login = {precisa_login}")
print()


# --- A armadilha do intervalo ---------------------------------------
numero = 99

# "Está DENTRO de 1 a 5?" -> intervalo permitido -> and
dentro = numero >= 1 and numero <= 5

# "Está FORA de 1 a 5?" -> intervalo proibido -> or
fora = numero < 1 or numero > 5

# E o erro: nada é menor que 1 E maior que 5 ao mesmo tempo.
nunca = numero < 1 and numero > 5

print(f"numero = {numero}")
print(f"dentro (>=1 and <=5) -> {dentro}")
print(f"fora   (<1  or  >5)  -> {fora}")
print(f"nunca  (<1  and >5)  -> {nunca}    <- é SEMPRE False, para qualquer número")
print()

# Python tem um atalho que quase nenhuma linguagem tem, e ele lê melhor:
print(f"1 <= numero <= 5     -> {1 <= numero <= 5}")
print()


# --- Precedência: not > and > or ------------------------------------
print(f"True or False and False    -> {True or False and False}    <- o and resolve primeiro")
print(f"(True or False) and False  -> {(True or False) and False}")
print(f"not True and False         -> {not True and False}")
print(f"not (True and False)       -> {not (True and False)}")


# --- Experimento ---------------------------------------------------
# 1. Troque "numero" por 3 e rode. Agora "dentro" é True e "fora" é
#    False. E "nunca"? Continua False — teste com outros valores até
#    se convencer de que ele nunca muda.
#
# 2. Escreva a condição "a idade está entre 13 e 19" (inclusive) das
#    duas formas: com "and" e com o atalho.
#
# 3. Sem rodar, diga o valor de: not (5 > 3) or (2 == 2) and False
#    Depois confira.
