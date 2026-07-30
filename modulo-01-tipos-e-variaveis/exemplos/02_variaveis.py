"""
Módulo 01 — Tipos e variáveis
Exemplo 02: criar, reatribuir e trocar

Este arquivo mostra:
  - que o "=" guarda um valor, não afirma uma igualdade
  - que a variável pode receber outro valor, e até outro tipo
  - a troca de duas variáveis em uma linha

Como executar:
  python 02_variaveis.py
"""

# O valor da direita é calculado primeiro; só depois recebe o nome.
preco = 49.90
print(f"Preço: {preco}")

# Reatribuir: o valor antigo é descartado, sem aviso.
preco = 39.90
print(f"Preço na promoção: {preco}")
print()


# Esta linha parece uma contradição matemática, mas não é uma
# afirmação: é uma ordem. "Pegue o contador, some 1, guarde de volta."
contador = 0
print(f"contador começa em {contador}")

contador = contador + 1
print(f"depois de somar 1: {contador}")

contador += 1               # atalho para a mesma coisa
print(f"depois do atalho +=: {contador}")
print()


# O tipo acompanha o valor, e ninguém reclama se ele mudar.
dado = 25
print(f"dado = {dado} ({type(dado).__name__})")

dado = "vinte e cinco"
print(f"dado = {dado} ({type(dado).__name__})")
print()


# Trocar duas variáveis de lugar, em uma linha só.
primeiro = "A"
segundo = "B"
print(f"antes:  primeiro = {primeiro}, segundo = {segundo}")

primeiro, segundo = segundo, primeiro
print(f"depois: primeiro = {primeiro}, segundo = {segundo}")


# --- Experimento ---------------------------------------------------
# 1. Tente fazer a troca do jeito ingênuo, sem o truque:
#       primeiro = segundo
#       segundo = primeiro
#    Rode e veja o resultado. Por que as duas ficam com o mesmo valor?
#
# 2. Depois de "dado" virar texto, acrescente print(dado + 1).
#    O erro que aparece é o assunto do exemplo 04.
#
# 3. Escreva "contador += 1" ANTES da linha "contador = 0" e rode.
#    Qual erro aparece, e por quê?
