"""
Módulo 03 — Entrada e saída
Exemplo 04: convertendo entre tipos

Este arquivo mostra:
  - int(), float() e str() nas conversões que funcionam
  - as conversões que quebram, e por quê
  - o caminho de duas etapas para "3.14" virar inteiro

Este exemplo não pede nada digitado: os valores são fixos para você
prever a saída antes de rodar.

Como executar:
  python 04_conversoes.py
"""

# --- Para inteiro: int() --------------------------------------------
print("--- int() ---")
print(f'int("123")   = {int("123")}')
print(f"int(45.89)   = {int(45.89)}      <- CORTA a parte decimal, não arredonda")
print(f"int(45.99)   = {int(45.99)}      <- continua cortando")
print(f"int(True)    = {int(True)}")
print()

# --- Para decimal: float() ------------------------------------------
print("--- float() ---")
print(f'float("3.14") = {float("3.14")}')
print(f'float("7")    = {float("7")}      <- texto de inteiro vira decimal numa boa')
print(f"float(42)     = {float(42)}")
print()

# --- Para texto: str() ----------------------------------------------
print("--- str() ---")
print(f"str(456)   = '{str(456)}'")
print(f"str(78.9)  = '{str(78.9)}'")
print(f"str(True)  = '{str(True)}'")
print()


# --- As conversões que quebram --------------------------------------
print("--- as que quebram ---")
print("int('abc')    -> ValueError: invalid literal for int() with base 10: 'abc'")
print("float('texto')-> ValueError: could not convert string to float: 'texto'")
print("int('3.14')   -> ValueError: invalid literal for int() with base 10: '3.14'")
print()
print("O terceiro é o que surpreende: '3.14' É um número, mas não é a")
print("escrita de um INTEIRO. O Python não arredonda por conta própria,")
print("porque arredondar seria adivinhar sua intenção: 3 ou 4?")
print()

# O caminho quando você precisa mesmo do inteiro:
texto = "3.14"
como_decimal = float(texto)
como_inteiro = int(como_decimal)
print(f"'{texto}' -> float {como_decimal} -> int {como_inteiro}")
print(f"em uma linha só: int(float('{texto}')) = {int(float(texto))}")


# --- Experimento ---------------------------------------------------
# 1. Descomente e rode, uma por vez, para ver os erros de verdade:
#
#    print(int("abc"))
#    print(int("3.14"))
#    print(float("texto"))
#
# 2. Rode print(int(-45.89)). O resultado é -45, não -46: int() corta
#    em direção ao ZERO, diferente do // que arredonda para baixo.
#    Compare com print(-45.89 // 1).
#
# 3. Rode print(int("  42  ")). Funciona, apesar dos espaços?
#    E print(int("4 2"))?
