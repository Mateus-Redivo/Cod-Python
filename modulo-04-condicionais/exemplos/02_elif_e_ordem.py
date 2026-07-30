"""
Módulo 04 — Condicionais
Exemplo 02: elif e a ordem das faixas

Este arquivo mostra:
  - a cadeia if/elif/else testando de cima para baixo
  - que o primeiro True encerra a cadeia
  - o elif inalcançável, que roda sem erro e responde errado

Como executar:
  python 02_elif_e_ordem.py
"""

nota = 7.5
print(f"nota = {nota}")
print()

# --- A ordem certa: da faixa mais alta para a mais baixa ------------
print("Ordem correta:")
if nota >= 9:
    print("  Conceito A")
elif nota >= 7:
    print("  Conceito B")
elif nota >= 5:
    print("  Conceito C")
else:
    print("  Conceito D (reprovado)")
print()

# Repare que o segundo teste é só "nota >= 7", sem repetir "e < 9".
# Se o programa chegou no elif, o if de cima JÁ foi falso — o "senão"
# está embutido na palavra elif.


# --- A ordem errada: tudo cai no primeiro ---------------------------
print("Ordem invertida (errada):")
if nota >= 5:
    print("  Conceito C")
elif nota >= 7:
    print("  Conceito B      <- nunca executa, para nota nenhuma")
elif nota >= 9:
    print("  Conceito A      <- nunca executa, para nota nenhuma")
else:
    print("  Conceito D")
print()

print("Com nota 7.5 — e também com 9, com 10, com qualquer nota >= 5 —")
print("a cadeia errada sempre para no primeiro teste. Os dois elifs")
print("abaixo dele são código morto: rodam zero vezes, sempre.")
print()


# --- O elif não é a mesma coisa que vários ifs ----------------------
numero = 15
print(f"numero = {numero}")

print("Com elif (para no primeiro):")
if numero % 3 == 0:
    print("  múltiplo de 3")
elif numero % 5 == 0:
    print("  múltiplo de 5")

print("Com ifs separados (testa todos):")
if numero % 3 == 0:
    print("  múltiplo de 3")
if numero % 5 == 0:
    print("  múltiplo de 5")

print()
print("15 é múltiplo dos dois. O elif mostra só o primeiro;")
print("os ifs separados mostram os dois. Nenhum está errado —")
print("são perguntas diferentes.")


# --- Experimento ---------------------------------------------------
# 1. Troque nota para 10 e rode. A cadeia errada ainda diz "Conceito C"?
#
# 2. Na cadeia correta, troque o último "else" por "elif nota >= 0".
#    O que acontece com uma nota negativa? O else é a rede de segurança
#    que garante que algum ramo sempre rode.
#
# 3. Escreva a cadeia de conceitos na ordem crescente (D, C, B, A),
#    usando <= em vez de >=. É possível e fica correta — a regra não é
#    "sempre decrescente", é "sem sobreposição na ordem errada".
