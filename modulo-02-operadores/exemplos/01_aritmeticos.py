"""
Módulo 02 — Operadores
Exemplo 01: operadores aritméticos

Este arquivo mostra:
  - os sete operadores aritméticos com os mesmos dois números
  - a diferença entre / e //
  - três usos do resto da divisão (%)

Como executar:
  python 01_aritmeticos.py
"""

a = 10
b = 3

print(f"a = {a}, b = {b}")
print()

print(f"a + b   = {a + b}")
print(f"a - b   = {a - b}")
print(f"a * b   = {a * b}")
print(f"a / b   = {a / b}       <- divisão real, sempre float")
print(f"a // b  = {a // b}                  <- divisão inteira, descarta o resto")
print(f"a % b   = {a % b}                  <- só o resto")
print(f"a ** b  = {a ** b}               <- potência: 10 elevado a 3")
print()

# Repare: mesmo quando a conta é exata, / devolve float.
print(f"4 / 2  = {4 / 2}   (tipo {type(4 / 2).__name__})")
print(f"4 // 2 = {4 // 2}     (tipo {type(4 // 2).__name__})")
print()


# --- Os três usos do % que você vai repetir a vida toda -------------
numero = 17

print(f"{numero} é par?          {numero % 2 == 0}")
print(f"{numero} é múltiplo de 3? {numero % 3 == 0}")
print()

# Quebrar uma quantidade em unidades maiores e menores
total_de_segundos = 3725
horas = total_de_segundos // 3600
resto = total_de_segundos % 3600
minutos = resto // 60
segundos = resto % 60

print(f"{total_de_segundos} segundos = {horas}h {minutos}min {segundos}s")


# --- Experimento ---------------------------------------------------
# 1. Troque b por 0 e rode. O erro é ZeroDivisionError: dividir por
#    zero não é possível nem no Python. Desfaça depois.
#
# 2. Rode print(-7 // 2). O resultado é -4, não -3: a divisão inteira
#    arredonda para BAIXO, não em direção ao zero.
#
# 3. Mude total_de_segundos para 7325 e confira a conta na mão.
#    A dupla // e % é o jeito padrão de quebrar quantidades assim.
