"""
Gabarito — Módulo 01, Exercício 03: Simulador de troco

Enunciado:
  modulo-01-tipos-e-variaveis/exercicios/EXERCICIO-03-simulador-de-troco.md

Como executar:
  python simulador_de_troco.py
"""

# Denominações EM CENTAVOS, como inteiros. Nenhum float no cálculo.
NOTA_50 = 5000
NOTA_20 = 2000
NOTA_10 = 1000
NOTA_5 = 500
NOTA_2 = 200
MOEDA_1_REAL = 100
MOEDA_50_CENTAVOS = 50
MOEDA_25_CENTAVOS = 25
MOEDA_10_CENTAVOS = 10
MOEDA_5_CENTAVOS = 5
MOEDA_1_CENTAVO = 1

CENTAVOS_POR_REAL = 100

# Os valores também entram em centavos, já como inteiros.
valor_da_compra = 3745      # R$ 37,45
valor_pago = 5000           # R$ 50,00

troco = valor_pago - valor_da_compra

print(f"Compra:  R$ {valor_da_compra / CENTAVOS_POR_REAL:.2f}")
print(f"Pago:    R$ {valor_pago / CENTAVOS_POR_REAL:.2f}")
print(f"Troco:   R$ {troco / CENTAVOS_POR_REAL:.2f}")
print()

# O padrão de sempre: // pega quantas cabem, % guarda o que sobra.
resto = troco

qtd_50 = resto // NOTA_50
resto = resto % NOTA_50

qtd_20 = resto // NOTA_20
resto = resto % NOTA_20

qtd_10 = resto // NOTA_10
resto = resto % NOTA_10

qtd_5 = resto // NOTA_5
resto = resto % NOTA_5

qtd_2 = resto // NOTA_2
resto = resto % NOTA_2

qtd_1_real = resto // MOEDA_1_REAL
resto = resto % MOEDA_1_REAL

qtd_50c = resto // MOEDA_50_CENTAVOS
resto = resto % MOEDA_50_CENTAVOS

qtd_25c = resto // MOEDA_25_CENTAVOS
resto = resto % MOEDA_25_CENTAVOS

qtd_10c = resto // MOEDA_10_CENTAVOS
resto = resto % MOEDA_10_CENTAVOS

qtd_5c = resto // MOEDA_5_CENTAVOS
resto = resto % MOEDA_5_CENTAVOS

qtd_1c = resto // MOEDA_1_CENTAVO

# Sem if, todas as denominações aparecem — inclusive as zeradas.
print("R$ 50 x", qtd_50)
print("R$ 20 x", qtd_20)
print("R$ 10 x", qtd_10)
print("R$  5 x", qtd_5)
print("R$  2 x", qtd_2)
print("R$  1 x", qtd_1_real)
print("50c   x", qtd_50c)
print("25c   x", qtd_25c)
print("10c   x", qtd_10c)
print(" 5c   x", qtd_5c)
print(" 1c   x", qtd_1c)
print()

conferencia = (qtd_50 * NOTA_50 + qtd_20 * NOTA_20 + qtd_10 * NOTA_10
               + qtd_5 * NOTA_5 + qtd_2 * NOTA_2 + qtd_1_real * MOEDA_1_REAL
               + qtd_50c * MOEDA_50_CENTAVOS + qtd_25c * MOEDA_25_CENTAVOS
               + qtd_10c * MOEDA_10_CENTAVOS + qtd_5c * MOEDA_5_CENTAVOS
               + qtd_1c * MOEDA_1_CENTAVO)

print(f"Conferência: R$ {conferencia / CENTAVOS_POR_REAL:.2f}")


# --- Por que assim -------------------------------------------------
# 1. TUDO em centavos inteiros. Esta é a decisão que o exercício
#    inteiro existe para ensinar. Com float, "19.99 * 100" dá
#    1998.9999999999998 e o int() corta para 1998 — some um centavo,
#    sem erro, sem aviso.
#
#    Confira você mesmo:
#      print(int(19.99 * 100))   -> 1998
#      print(int(12.55 * 100))   -> 1255   (este funciona!)
#
#    O bug aparecer em alguns valores e não em outros é o que o torna
#    perigoso: testar com um número só não pega nada.
#
# 2. O float só aparece na EXIBIÇÃO, dividindo por 100 dentro da
#    f-string. Calcule com inteiro, formate no fim. É assim que
#    sistemas financeiros de verdade trabalham.
#
# 3. A variável "resto" é reaproveitada a cada etapa. Poderia haver
#    uma variável por degrau (resto_apos_50, resto_apos_20...), mas
#    seriam onze nomes para um valor que é sempre "o que ainda falta
#    distribuir".
#
# 4. Repetitivo? Muito. São 11 pares de // e % quase idênticos —
#    exatamente o sintoma que o módulo 05 vai curar com um laço, e o
#    módulo 06 com uma lista de denominações. Sentir a repetição
#    doendo agora é o que faz o laço parecer alívio depois.


# --- Conferência ----------------------------------------------------
# Troco de 1255 centavos (R$ 12,55):
#   1255 // 5000 = 0      resto 1255
#   1255 // 2000 = 0      resto 1255
#   1255 // 1000 = 1      resto  255
#    255 //  500 = 0      resto  255
#    255 //  200 = 1      resto   55
#     55 //  100 = 0      resto   55
#     55 //   50 = 1      resto    5
#      5 //   25 = 0      resto    5
#      5 //   10 = 0      resto    5
#      5 //    5 = 1      resto    0
#      0 //    1 = 0
#
#   Uma nota de 10, uma de 2, uma moeda de 50c e uma de 5c.
#   10.00 + 2.00 + 0.50 + 0.05 = 12.55. Bate.
#
# Teste com 19.99 -> 20.00 (compra 1999, pago 2000, troco 1 centavo):
#   só a moeda de 1 centavo. É o caso que o float erraria.


# --- Sobre o requisito 5 e o desafio ---------------------------------
# Esconder as linhas zeradas exige if, do módulo 04:
#
#   if qtd_50 > 0:
#       print("R$ 50 x", qtd_50)
#
# E onze ifs quase iguais é o mesmo cheiro de repetição do item 4 —
# a solução boa mesmo junta lista (módulo 06) e laço (módulo 05).
#
# Sobre o pagamento insuficiente: hoje, com valor_pago menor que a
# compra, o troco fica negativo e as divisões inteiras produzem
# quantidades negativas — o programa "distribui" -1 notas de 10 sem
# reclamar. Tratar isso exige testar antes de calcular, o que também
# é o if do módulo 04:
#
#   if valor_pago < valor_da_compra:
#       print("Pagamento insuficiente.")
#   else:
#       ... todo o cálculo ...
