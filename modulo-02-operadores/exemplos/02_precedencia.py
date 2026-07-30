"""
Módulo 02 — Operadores
Exemplo 02: ordem de precedência

Este arquivo mostra:
  - que a conta não é resolvida da esquerda para a direita
  - o erro clássico da média
  - por que parênteses valem mais que memorizar a ordem

Como executar:
  python 02_precedencia.py
"""

# A multiplicação acontece antes da soma.
print(f"2 + 3 * 4    = {2 + 3 * 4}      <- 14, não 20")
print(f"(2 + 3) * 4  = {(2 + 3) * 4}      <- os parênteses mudam tudo")
print()

# A potência vem antes da multiplicação.
print(f"2 ** 3 * 4   = {2 ** 3 * 4}      <- (2**3) * 4")
print(f"2 * 3 + 4 / 2 = {2 * 3 + 4 / 2}     <- (2*3) + (4/2)")
print()

# E a potência resolve da DIREITA para a esquerda, ao contrário do resto.
print(f"2 ** 3 ** 2  = {2 ** 3 ** 2}     <- 2**(3**2) = 2**9, não (2**3)**2")
print()


# --- O erro clássico da média ---------------------------------------
nota1 = 8.0
nota2 = 6.0

media_errada = nota1 + nota2 / 2
media_certa = (nota1 + nota2) / 2

print(f"notas: {nota1} e {nota2}")
print(f"nota1 + nota2 / 2   = {media_errada}   <- dividiu SÓ a nota2")
print(f"(nota1 + nota2) / 2 = {media_certa}    <- certo")
print()

# O programa errado roda sem reclamar e devolve um número plausível.
# É o pior tipo de erro: silencioso. Parênteses são o antídoto barato.


# --- Experimento ---------------------------------------------------
# 1. Cubra a tela com a mão e calcule 10 - 2 * 3 + 1 de cabeça.
#    Depois acrescente um print para conferir.
#
# 2. Escreva a média de TRÊS notas. Onde vão os parênteses?
#
# 3. Reescreva "2 ** 3 ** 2" com parênteses para que dê 64.
