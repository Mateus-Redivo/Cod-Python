"""
Módulo 10 — Tratamento de erros
Exemplo 02: as cinco exceções mais comuns

Este arquivo mostra:
  - as cinco que você já encontrou nos módulos anteriores
  - a mensagem exata de cada uma
  - como capturar o objeto do erro para ler a mensagem

Nada é digitado: os erros são provocados de propósito e capturados.

Como executar:
  python 02_excecoes_comuns.py
"""

# O "as erro" guarda o objeto da exceção, e print(erro) mostra a
# mensagem que apareceria na tela se ninguém capturasse.

print("--- ValueError: texto que não vira número (módulo 03) ---")
try:
    int("abc")
except ValueError as erro:
    print(f"  {type(erro).__name__}: {erro}")
print()

print("--- ValueError também com decimal em int() ---")
try:
    int("3.14")
except ValueError as erro:
    print(f"  {type(erro).__name__}: {erro}")
print()

print("--- ZeroDivisionError: divisão por zero (módulo 03) ---")
try:
    10 / 0
except ZeroDivisionError as erro:
    print(f"  {type(erro).__name__}: {erro}")
print()

print("--- IndexError: índice que não existe (módulo 06) ---")
try:
    lista = [1, 2, 3]
    lista[10]
except IndexError as erro:
    print(f"  {type(erro).__name__}: {erro}")
print()

print("--- TypeError: tipos incompatíveis (módulo 01) ---")
try:
    "3" + 5
except TypeError as erro:
    print(f"  {type(erro).__name__}: {erro}")
print()

print("--- NameError: variável que não existe (módulo 00) ---")
try:
    print(variavel_que_nao_existe)
except NameError as erro:
    print(f"  {type(erro).__name__}: {erro}")
print()


# --- Capturando mais de um tipo no mesmo except ----------------------
print("--- Vários tipos, um except só ---")
for valor in ["abc", 0]:
    try:
        resultado = 10 / int(valor)
        print(f"  10 / {valor} = {resultado}")
    except (ValueError, ZeroDivisionError) as erro:
        print(f"  '{valor}' falhou -> {type(erro).__name__}: {erro}")
print()
print("  Use a tupla quando a REAÇÃO for a mesma para os dois erros.")
print("  Se as mensagens precisam ser diferentes, use except separados.")


# --- Experimento ---------------------------------------------------
# 1. Troque int("abc") por int("  42  ") e veja que não dá erro:
#    espaços em volta são tolerados, letras não.
#
# 2. Acrescente um bloco que provoque KeyError. (dica: você ainda não
#    viu dicionários — pule se não souber; é conteúdo além da trilha.)
#
# 3. No último bloco, troque a tupla por "except ValueError" apenas.
#    O valor 0 deixa de ser capturado e o programa morre.
