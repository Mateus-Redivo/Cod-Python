"""
Módulo 01 — Tipos e variáveis
Exemplo 04: o mesmo "+" faz coisas diferentes

Este arquivo mostra:
  - "+" entre números soma
  - "+" entre textos gruda (concatena)
  - "+" entre texto e número dá TypeError

Este é o erro que mais vai te encontrar no módulo 03, quando tudo que
vem do teclado chegar como texto.

Como executar:
  python 04_somando_tipos.py
"""

# Com números, soma.
print("2 + 3       =", 2 + 3)
print("1.5 + 2.5   =", 1.5 + 2.5)
print()

# Com textos, gruda um no outro. Nenhum espaço é acrescentado.
print('"2" + "3"       =', "2" + "3")
print('"bom" + "dia"   =', "bom" + "dia")
print('"bom" + " dia"  =', "bom" + " dia")
print()

# int + float dá float: o Python promove para o tipo mais amplo.
resultado = 10 + 1.5
print(f"10 + 1.5 = {resultado} (tipo {type(resultado).__name__})")
print()

# Multiplicar texto por número repete o texto. Útil para separadores.
print("-" * 40)
print("ha" * 3)
print("-" * 40)
print()

# --- O erro que importa ---------------------------------------------
# Descomente a linha abaixo e rode:
#
# print("2" + 3)
#
# Você vai ver:
#   TypeError: can only concatenate str (not "int") to str
#
# Tradução: "só sei grudar texto com texto". O Python não adivinha se
# você queria a soma 5 ou a concatenação "23" — ele para e pergunta.
#
# A saída é converter antes. int("2") vira o número 2; str(3) vira o
# texto "3". As duas linhas abaixo funcionam:
print("convertendo para número:", int("2") + 3)
print("convertendo para texto: ", "2" + str(3))


# --- Experimento ---------------------------------------------------
# 1. Descomente o print("2" + 3), leia a mensagem inteira e comente
#    de novo.
#
# 2. Rode print(int("2.5")). Por que quebra, se "2.5" é um número?
#    Dica: leia o nome da função. Tente float("2.5").
#
# 3. Rode print(True + True). O resultado é 2. Em Python, bool é um
#    int disfarçado: True vale 1 e False vale 0. Curiosidade que
#    aparece no módulo 05, quando você for contar quantas vezes uma
#    condição foi verdadeira.
