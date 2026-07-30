"""
Módulo 10 — Tratamento de erros
Exemplo 01: o primeiro try/except

Este arquivo mostra:
  - o programa morrendo, e depois sobrevivendo
  - que o try ABANDONA as linhas restantes quando dá erro
  - por que capturar o tipo específico

Como executar:
  python 01_try_except.py
"""

# --- Sem try: o programa morre ---------------------------------------
# Descomente as duas linhas para ver:
#
# idade = int(input("Idade: "))     # digite "abc" aqui
# print(f"Você tem {idade} anos.")
#
#   ValueError: invalid literal for int() with base 10: 'abc'
#
# O print nunca roda. O programa inteiro encerra.

print("--- Com try/except: o programa sobrevive ---")

try:
    idade = int(input("Idade: "))
    print(f"  Você tem {idade} anos.")
except ValueError:
    print("  Isso não é um número inteiro.")

print("  ...e o programa continua daqui.")
print()


# --- O try ABANDONA o resto ------------------------------------------
print("--- O que acontece dentro do try quando dá erro ---")

try:
    print("  linha 1: sempre roda")
    resultado = 10 / 0                      # explode aqui
    print("  linha 3: NUNCA roda")
    print("  linha 4: NUNCA roda")
except ZeroDivisionError:
    print("  fui parar no except, pulando as linhas 3 e 4")

print()


# --- Vários except: cada erro com sua mensagem -----------------------
print("--- Tratando dois erros diferentes ---")

numerador = input("  Numerador: ")
denominador = input("  Denominador: ")

try:
    resultado = int(numerador) / int(denominador)
    print(f"  Resultado: {resultado}")
except ValueError:
    print("  Digite apenas números inteiros.")
except ZeroDivisionError:
    print("  Não dá para dividir por zero.")

print()


# --- Por que NÃO usar except pelado ----------------------------------
print("--- except pelado engole tudo ---")

try:
    valor = int("abc")
except:                                     # nunca faça isso
    print("  deu algum erro... mas qual? Ninguém sabe.")

print("  Com 'except ValueError' você saberia exatamente o quê.")
print("  E um erro de digitação SEU também seria engolido em silêncio.")


# --- Experimento ---------------------------------------------------
# 1. Descomente as duas primeiras linhas e digite "abc". Veja o
#    programa morrer de verdade. Comente de novo.
#
# 2. No bloco dos dois except, digite "abc" no numerador. Depois rode
#    de novo e digite 10 e 0. Duas mensagens diferentes, dois problemas
#    diferentes.
#
# 3. Troque "except ZeroDivisionError" por "except ValueError" no
#    segundo bloco e rode. O erro não é capturado e o programa morre:
#    capturar o tipo errado é o mesmo que não capturar.
