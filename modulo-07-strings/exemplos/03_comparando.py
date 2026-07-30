"""
Módulo 07 — Strings
Exemplo 03: comparando texto

Este arquivo mostra:
  - por que "Sim" != "sim" derruba o programa
  - a receita .strip().lower() para entrada de usuário
  - a cilada da ordem alfabética com maiúsculas

Como executar:
  python 03_comparando.py
"""

# --- O problema -------------------------------------------------------
# Suponha que o usuário digitou cada uma destas respostas.
# Todas significam "sim", mas só uma passa no teste ingênuo.
print("Teste ingênuo: resposta == 'sim'")
print(f"  'sim'   -> {'sim' == 'sim'}")
print(f"  'Sim'   -> {'Sim' == 'sim'}")
print(f"  'SIM'   -> {'SIM' == 'sim'}")
print(f"  ' sim ' -> {' sim ' == 'sim'}")
print()
print("Três em quatro usuários seriam ignorados pelo programa.")
print()


# --- A receita --------------------------------------------------------
print("Com .strip().lower():")
print(f"  'sim'   -> {'sim'.strip().lower() == 'sim'}")
print(f"  'Sim'   -> {'Sim'.strip().lower() == 'sim'}")
print(f"  'SIM'   -> {'SIM'.strip().lower() == 'sim'}")
print(f"  ' sim ' -> {' sim '.strip().lower() == 'sim'}")
print()
print("Os quatro passam. Adote isso como padrão para TODA comparação")
print("de texto que veio do usuário.")
print()


# --- Na prática, com input --------------------------------------------
resposta = input("Deseja continuar? (sim/nao) ").strip().lower()

if resposta == "sim":
    print("  Continuando...")
elif resposta == "nao":
    print("  Encerrando.")
else:
    print(f"  Não entendi '{resposta}'.")
print()


# --- A cilada da ordem alfabética -------------------------------------
print("Comparação de ordem:")
print(f"  'Ana' < 'Bruno'  -> {'Ana' < 'Bruno'}     (como no dicionário)")
print(f"  'Zebra' < 'ana'  -> {'Zebra' < 'ana'}     <- surpresa!")
print()
print("Motivo: a comparação usa a tabela de caracteres, e nela TODAS")
print("as maiúsculas vêm antes de TODAS as minúsculas.")
print(f"  'Z' vale {ord('Z')}, 'a' vale {ord('a')}")
print()

print("Mesma receita resolve:")
print(f"  'Zebra'.lower() < 'ana'.lower() -> {'Zebra'.lower() < 'ana'.lower()}")
print()

# E na ordenação de uma lista de nomes, o efeito é visível:
nomes = ["bruno", "Ana", "carlos", "Diana"]
print(f"nomes = {nomes}")
print(f"sorted(nomes)            = {sorted(nomes)}")
print(f"sorted(nomes, key=str.lower) = {sorted(nomes, key=str.lower)}")


# --- Experimento ---------------------------------------------------
# 1. Rode o programa e responda "  SIM  ", com espaços e maiúsculas.
#    Funciona?
#
# 2. Responda "s". O programa cai no else. Como você aceitaria "s" e
#    "sim" como a mesma coisa? (dica: operador "or", ou o "in" com
#    uma lista de respostas aceitas)
#
# 3. Compare 'ana' == 'ANA'.lower() e 'ana'.upper() == 'ANA'.
#    As duas funcionam. Existe motivo para preferir lower()?
